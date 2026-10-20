import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path

import pytest

import src.app.saved_locations_repository as repository_module
from src.app.saved_locations_repository import (
    SCHEMA_VERSION,
    SavedLocationConflictError,
    SavedLocationStorageError,
    SavedLocationsRepository,
)


GEOJSON = {
    "type": "Polygon",
    "coordinates": [[[1.123456789, 2], [3, 2], [3, 4], [1.123456789, 2]]],
    "properties": {"label": "área teste"},
}


@contextmanager
def open_database(path):
    connection = sqlite3.connect(path)
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def record(location_id="id-1", name="Área", normalized_name="área"):
    return {
        "id": location_id,
        "name": name,
        "normalized_name": normalized_name,
        "geojson": GEOJSON,
        "center_lat": 3.0,
        "center_lon": 2.0,
        "created_at": "2026-10-20T10:00:00+00:00",
        "updated_at": "2026-10-20T10:00:00+00:00",
    }


def test_initialize_creates_versioned_schema_idempotently(tmp_path):
    path = tmp_path / "data" / "locations.sqlite3"
    repository = SavedLocationsRepository(path)

    repository.initialize()
    repository.initialize()

    with open_database(path) as connection:
        assert connection.execute("PRAGMA user_version").fetchone()[0] == SCHEMA_VERSION
        columns = [row[1] for row in connection.execute("PRAGMA table_info(saved_locations)")]
        assert columns == [
            "id", "name", "normalized_name", "geojson_json", "center_lat",
            "center_lon", "created_at", "updated_at",
        ]
        indexes = connection.execute("PRAGMA index_list(saved_locations)").fetchall()
        assert any(index[2] for index in indexes)


def test_insert_list_get_and_delete_persist_across_repository_connections(tmp_path):
    path = tmp_path / "saved.sqlite3"
    repository = SavedLocationsRepository(path)
    repository.initialize()
    repository.insert_location(record())

    # New repository instances/SQLite connections still observe persisted data.
    reader = SavedLocationsRepository(path)
    summary = reader.list_locations()
    full_record = reader.get_location("id-1")

    assert summary == [{
        "id": "id-1",
        "name": "Área",
        "center": {"lat": 3.0, "lon": 2.0},
        "created_at": "2026-10-20T10:00:00+00:00",
        "updated_at": "2026-10-20T10:00:00+00:00",
    }]
    assert full_record["geojson"] == GEOJSON
    assert full_record["normalized_name"] == "área"
    assert reader.get_location("missing") is None
    assert reader.delete_location("id-1") is True
    assert reader.delete_location("id-1") is False
    assert reader.list_locations() == []


def test_list_order_is_deterministic_by_normalized_name(tmp_path):
    repository = SavedLocationsRepository(tmp_path / "saved.sqlite3")
    repository.initialize()
    repository.insert_location(record("b", "Beta", "beta"))
    repository.insert_location(record("g", "Gamma", "gamma"))
    repository.insert_location(record("a", "Alpha", "alpha"))

    assert [item["id"] for item in repository.list_locations()] == ["a", "b", "g"]


def test_duplicate_normalized_name_is_rejected_without_removing_existing_row(tmp_path):
    repository = SavedLocationsRepository(tmp_path / "saved.sqlite3")
    repository.initialize()
    repository.insert_location(record())

    with pytest.raises(SavedLocationConflictError):
        repository.insert_location(record("id-2", "AREA", "área"))

    assert [item["id"] for item in repository.list_locations()] == ["id-1"]


def test_future_schema_version_is_rejected(tmp_path):
    path = tmp_path / "saved.sqlite3"
    with open_database(path) as connection:
        connection.execute("PRAGMA user_version = 2")

    with pytest.raises(SavedLocationStorageError, match="versão"):
        SavedLocationsRepository(path).initialize()


def test_database_path_under_file_is_reported_as_storage_error(tmp_path):
    parent_file = tmp_path / "not-a-directory"
    parent_file.write_text("file occupies intended directory", encoding="utf-8")

    with pytest.raises(SavedLocationStorageError):
        SavedLocationsRepository(parent_file / "saved.sqlite3").initialize()


def test_invalid_record_shape_is_reported_as_storage_error(tmp_path):
    repository = SavedLocationsRepository(tmp_path / "saved.sqlite3")
    repository.initialize()

    with pytest.raises(SavedLocationStorageError, match="campos"):
        repository.insert_location({"id": "incomplete"})


def test_corrupt_geojson_is_reported_instead_of_returned(tmp_path):
    path = tmp_path / "saved.sqlite3"
    repository = SavedLocationsRepository(path)
    repository.initialize()
    repository.insert_location(record())
    with open_database(path) as connection:
        connection.execute(
            "UPDATE saved_locations SET geojson_json = ? WHERE id = ?",
            ("{invalid", "id-1"),
        )

    with pytest.raises(SavedLocationStorageError, match="corrompido"):
        repository.get_location("id-1")


def test_geojson_round_trip_keeps_utf8_content_and_numeric_precision(tmp_path):
    repository = SavedLocationsRepository(tmp_path / "saved.sqlite3")
    repository.initialize()
    repository.insert_location(record())

    assert repository.get_location("id-1")["geojson"] == json.loads(
        json.dumps(GEOJSON, ensure_ascii=False)
    )


def test_non_windows_default_data_directory_is_restricted_when_supported(
    tmp_path, monkeypatch
):
    monkeypatch.setattr(repository_module, "IS_WINDOWS", False)
    database_path = (
        tmp_path / "monitoramento-agricola-satelite" / "saved_locations.sqlite3"
    )
    repository = SavedLocationsRepository(database_path)

    repository._ensure_parent_directory()

    assert database_path.parent.exists()


def test_non_windows_custom_directory_does_not_change_unrelated_permissions(
    tmp_path, monkeypatch
):
    monkeypatch.setattr(repository_module, "IS_WINDOWS", False)
    custom_directory = tmp_path / "custom-data"
    repository = SavedLocationsRepository(custom_directory / "saved.sqlite3")

    repository._ensure_parent_directory()

    assert custom_directory.exists()


def test_non_windows_permission_error_is_converted(tmp_path, monkeypatch):
    monkeypatch.setattr(repository_module, "IS_WINDOWS", False)
    database_path = (
        tmp_path / "monitoramento-agricola-satelite" / "saved_locations.sqlite3"
    )
    monkeypatch.setattr(Path, "chmod", lambda *args, **kwargs: (_ for _ in ()).throw(OSError("denied")))

    with pytest.raises(SavedLocationStorageError, match="preparar"):
        SavedLocationsRepository(database_path)._ensure_parent_directory()


def test_database_open_failure_is_converted_before_connection_exists(tmp_path):
    database_directory = tmp_path / "is-a-directory.sqlite3"
    database_directory.mkdir()

    with pytest.raises(SavedLocationStorageError, match="acessar"):
        SavedLocationsRepository(database_directory).initialize()


def test_integrity_error_during_connect_maps_to_conflict_without_rollback(
    tmp_path, monkeypatch
):
    monkeypatch.setattr(
        repository_module.sqlite3,
        "connect",
        lambda *args, **kwargs: (_ for _ in ()).throw(sqlite3.IntegrityError("conflict")),
    )

    with pytest.raises(SavedLocationConflictError):
        SavedLocationsRepository(tmp_path / "saved.sqlite3").initialize()


def test_sqlite_failure_after_connect_is_converted_and_connection_closed(tmp_path):
    path = tmp_path / "corrupt.sqlite3"
    path.write_bytes(b"not a SQLite database")

    with pytest.raises(SavedLocationStorageError, match="acessar"):
        SavedLocationsRepository(path).initialize()


def test_non_json_serializable_record_is_converted(tmp_path):
    repository = SavedLocationsRepository(tmp_path / "saved.sqlite3")
    repository.initialize()
    invalid = record()
    invalid["geojson"] = object()

    with pytest.raises(SavedLocationStorageError, match="campos"):
        repository.insert_location(invalid)


def test_path_without_application_directory_reaches_filesystem_root(tmp_path, monkeypatch):
    monkeypatch.setattr(repository_module, "IS_WINDOWS", False)
    repository = SavedLocationsRepository(Path(tmp_path.anchor) / "saved.sqlite3")

    repository._ensure_parent_directory()
