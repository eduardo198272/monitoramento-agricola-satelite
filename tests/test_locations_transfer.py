import json
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from src.app.locations_geojson import (
    MAX_FILE_BYTES,
    export_locations_geojson,
    parse_locations_geojson,
)
from src.app.saved_locations_repository import (
    SavedLocationConflictError,
    SavedLocationsRepository,
    SavedLocationStorageError,
)
from src.app.saved_locations_service import (
    SavedLocationDuplicateError,
    SavedLocationServiceError,
    SavedLocationsService,
)
from src.app.saved_locations_session import SessionLocationsRepository
from src.app.saved_locations_validation import SavedLocationValidationError
from src.app.locations_transfer_ui import render_locations_transfer
import src.app.locations_transfer_ui as transfer_ui


POLYGON = {
    "type": "Polygon",
    "coordinates": [[[-45, -20], [-44, -20], [-44, -19], [-45, -20]]],
}


def feature(name="Área agrícola"):
    return {"type": "Feature", "properties": {"name": name}, "geometry": POLYGON}


def collection(*names):
    return json.dumps({
        "type": "FeatureCollection",
        "features": [feature(name) for name in names],
    }).encode()


@pytest.fixture(params=["sqlite", "session"])
def service(request, tmp_path):
    if request.param == "sqlite":
        repository = SavedLocationsRepository(tmp_path / "test.sqlite3")
    else:
        repository = SessionLocationsRepository({})
    return SavedLocationsService(repository)


def test_roundtrip_preserves_names_and_geometries(service):
    service.save_location("Área agrícola", POLYGON)
    service.save_location("Outra área", feature())
    payload = service.export_locations()
    receiver = SavedLocationsService(SessionLocationsRepository({}))
    assert receiver.import_locations(payload) == 2
    assert [record["name"] for record in receiver.list_saved_locations()] == [
        "Outra área", "Área agrícola",
    ]
    for summary in receiver.list_saved_locations():
        assert receiver.get_saved_location(summary["id"])["geojson"] == POLYGON
    document = json.loads(payload)
    assert document["features"][0]["properties"] == {"name": "Outra área"}
    assert "id" not in document["features"][0]


def test_import_conflict_rolls_back_whole_batch(service):
    service.save_location("Existente", POLYGON)
    with pytest.raises(SavedLocationDuplicateError, match="Nenhuma"):
        service.import_locations(collection("Nova", " EXISTENTE "))
    assert [record["name"] for record in service.list_saved_locations()] == ["Existente"]


def test_invalid_last_feature_leaves_repository_unchanged(service):
    document = json.loads(collection("Nova", "Inválida"))
    document["features"][-1]["geometry"] = {"type": "Point", "coordinates": [1, 2]}
    with pytest.raises(SavedLocationValidationError):
        service.import_locations(json.dumps(document).encode())
    assert service.list_saved_locations() == []


def test_single_feature_and_utf8_bom_are_supported():
    records = parse_locations_geojson(b"\xef\xbb\xbf" + json.dumps(feature()).encode())
    assert records[0]["name"] == "Área agrícola"


@pytest.mark.parametrize("payload", [
    b"x" * (MAX_FILE_BYTES + 1),
    b"\xff",
    b"not JSON",
    b"[" * 2000,
    b"[]",
    b"{}",
    b'{"type":"FeatureCollection"}',
    b'{"type":"FeatureCollection","features":[]}',
    b'{"type":"FeatureCollection","features":{}}',
    collection(*[str(index) for index in range(101)]),
    collection("Duplicada", " DUPLICADA "),
    b'{"type":"FeatureCollection","features":[null]}',
    b'{"type":"FeatureCollection","features":[{"type":"Polygon"}]}',
    b'{"type":"Feature","properties":null}',
    json.dumps({**feature(), "properties": {}}).encode(),
    json.dumps({**feature(), "geometry": None}).encode(),
])
def test_rejects_invalid_files(payload):
    with pytest.raises(SavedLocationValidationError):
        parse_locations_geojson(payload)


def test_export_empty_or_oversized_set_is_not_downloadable():
    with pytest.raises(SavedLocationValidationError):
        export_locations_geojson([])
    with pytest.raises(SavedLocationValidationError):
        export_locations_geojson([
            {"name": str(index), "geojson": POLYGON} for index in range(101)
        ])


def test_sessions_are_isolated_and_reads_detached():
    first_state, second_state = {}, {}
    first = SavedLocationsService(SessionLocationsRepository(first_state))
    second = SavedLocationsService(SessionLocationsRepository(second_state))
    saved = first.save_location("Privada", POLYGON)
    assert second.list_saved_locations() == []
    assert second.get_saved_location(saved["id"]) is None
    saved["geojson"]["coordinates"].clear()
    assert first.get_saved_location(saved["id"])["geojson"] == POLYGON
    assert first.delete_saved_location(saved["id"]) is True
    assert first.delete_saved_location(saved["id"]) is False


def test_session_insert_conflicts_on_ids_without_partial_write():
    repository = SessionLocationsRepository({})
    service = SavedLocationsService(repository)
    saved = service.save_location("Primeira", POLYGON)
    record = dict(repository.records[saved["id"]], normalized_name="segunda")
    with pytest.raises(SavedLocationConflictError):
        repository.insert_locations([record])
    assert len(repository.records) == 1


def test_session_cannot_grow_beyond_a_downloadable_file():
    service = SavedLocationsService(SessionLocationsRepository({}))
    service.import_locations(collection(*[str(index) for index in range(100)]))
    with pytest.raises(SavedLocationValidationError):
        service.save_location("101st", POLYGON)
    assert len(service.list_saved_locations()) == 100
    assert len(parse_locations_geojson(service.export_locations())) == 100


def test_storage_selection_defaults_to_sqlite_and_reuses_only_current_session(monkeypatch):
    import streamlit

    monkeypatch.delenv("SAVED_LOCATIONS_STORAGE", raising=False)
    assert isinstance(SavedLocationsService().repository, SavedLocationsRepository)
    monkeypatch.setenv("SAVED_LOCATIONS_STORAGE", "session")
    monkeypatch.setattr(streamlit, "session_state", {})
    first = SavedLocationsService()
    saved = first.save_location("Sessão", POLYGON)
    assert SavedLocationsService().get_saved_location(saved["id"]) == saved
    monkeypatch.setattr(streamlit, "session_state", {})
    assert SavedLocationsService().list_saved_locations() == []
    monkeypatch.setenv("SAVED_LOCATIONS_STORAGE", "typo")
    with pytest.raises(SavedLocationServiceError):
        SavedLocationsService()


def test_export_handles_location_removed_during_read(monkeypatch):
    service = SavedLocationsService(SessionLocationsRepository({}))
    service.save_location("Área", POLYGON)
    monkeypatch.setattr(service, "get_saved_location", lambda location_id: None)
    with pytest.raises(SavedLocationServiceError):
        service.export_locations()


@pytest.fixture
def ui(monkeypatch):
    st = MagicMock()
    st.session_state = SimpleNamespace(show_saved_locations=False)
    st.file_uploader.return_value = None
    st.button.return_value = False
    service = MagicMock()
    monkeypatch.setattr(transfer_ui, "SavedLocationsService", lambda: service)
    return st, service


def test_transfer_ui_idle_and_session_warning(ui, monkeypatch):
    st, service = ui
    monkeypatch.setenv("SAVED_LOCATIONS_STORAGE", "sqlite")
    render_locations_transfer(st)
    st.warning.assert_not_called()
    service.import_locations.assert_not_called()
    monkeypatch.setenv("SAVED_LOCATIONS_STORAGE", "session")
    render_locations_transfer(st)
    st.warning.assert_called_once()


def test_transfer_ui_import_success(ui):
    st, service = ui
    upload = st.file_uploader.return_value = MagicMock()
    upload.getvalue.return_value = collection("Importada")
    st.button.side_effect = [True, False]
    service.import_locations.return_value = 1
    render_locations_transfer(st)
    service.import_locations.assert_called_once_with(upload.getvalue.return_value)
    assert st.session_state.show_saved_locations is True
    st.success.assert_called_once()


@pytest.mark.parametrize("error", [
    SavedLocationValidationError("Inválido"),
    SavedLocationDuplicateError("Duplicado"),
    SavedLocationStorageError("Disco"),
    SavedLocationServiceError("Serviço"),
])
def test_transfer_ui_import_errors(ui, error):
    st, service = ui
    st.file_uploader.return_value = MagicMock()
    st.button.side_effect = [True, False]
    service.import_locations.side_effect = error
    render_locations_transfer(st)
    st.error.assert_called_once()
    st.success.assert_not_called()


def test_transfer_ui_export_success(ui):
    st, service = ui
    st.button.side_effect = [False, True]
    service.export_locations.return_value = collection("Área")
    render_locations_transfer(st)
    assert st.download_button.call_args.kwargs["data"] == service.export_locations.return_value
    assert st.download_button.call_args.kwargs["on_click"] == "ignore"


@pytest.mark.parametrize("error", [
    SavedLocationValidationError("Vazio"),
    SavedLocationStorageError("Disco"),
    SavedLocationServiceError("Serviço"),
])
def test_transfer_ui_export_errors(ui, error):
    st, service = ui
    st.button.side_effect = [False, True]
    service.export_locations.side_effect = error
    render_locations_transfer(st)
    st.error.assert_called_once()
    st.download_button.assert_not_called()
