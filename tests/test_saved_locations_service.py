import sqlite3

import pytest

from src.app.saved_locations_repository import SavedLocationsRepository
from src.app.saved_locations_service import (
    SavedLocationDuplicateError,
    SavedLocationServiceError,
    SavedLocationsService,
)
from src.app.saved_locations_validation import SavedLocationValidationError


POLYGON = {
    "type": "Polygon",
    "coordinates": [[[-4, -2], [8, -2], [8, 6], [-4, 6], [-4, -2]]],
}


def make_service(tmp_path):
    return SavedLocationsService(SavedLocationsRepository(tmp_path / "locations.sqlite3"))


def test_save_returns_complete_public_record_and_persists_bbox_center(tmp_path):
    service = make_service(tmp_path)

    result = service.save_location("  Fazenda   Norte ", POLYGON)

    assert set(result) == {
        "id", "name", "geojson", "center", "created_at", "updated_at"
    }
    assert result["name"] == "Fazenda   Norte"
    assert result["geojson"] == POLYGON
    assert result["center"] == {"lat": 2.0, "lon": 2.0}
    assert result["id"]
    assert result["created_at"].endswith("+00:00")
    assert result["updated_at"] == result["created_at"]
    assert service.get_saved_location(result["id"]) == result


def test_feature_center_uses_bbox_and_returns_detached_geojson(tmp_path):
    feature = {"type": "Feature", "properties": {"name": "área"}, "geometry": POLYGON}

    result = make_service(tmp_path).save_location("Área", feature)

    assert result["center"] == {"lat": 2.0, "lon": 2.0}
    assert result["geojson"] == feature
    assert result["geojson"] is not feature


def test_invalid_name_or_geometry_is_rejected_before_repository_write(tmp_path):
    repository = SavedLocationsRepository(tmp_path / "locations.sqlite3")
    service = SavedLocationsService(repository)

    with pytest.raises(SavedLocationValidationError):
        service.save_location("  ", POLYGON)
    with pytest.raises(SavedLocationValidationError):
        service.save_location("Valid", {"type": "Point", "coordinates": [0, 0]})

    repository.initialize()
    assert repository.list_locations() == []


def test_duplicate_normalized_name_has_domain_error_and_preserves_original(tmp_path):
    service = make_service(tmp_path)
    first = service.save_location("Fazenda   Sul", POLYGON)

    with pytest.raises(SavedLocationDuplicateError, match="Já existe"):
        service.save_location(" FAZENDA SUL ", POLYGON)

    assert service.get_saved_location(first["id"]) == first
    assert len(service.list_saved_locations()) == 1


def test_list_is_deterministically_ordered_and_only_contains_summaries(tmp_path):
    service = make_service(tmp_path)
    service.save_location("Zeta", POLYGON)
    service.save_location("Beta", POLYGON)
    service.save_location("Alfa", POLYGON)

    results = service.list_saved_locations()

    assert [item["name"] for item in results] == ["Alfa", "Beta", "Zeta"]
    assert all("geojson" not in item for item in results)


def test_get_and_delete_missing_id_semantics(tmp_path):
    service = make_service(tmp_path)

    assert service.get_saved_location("missing") is None
    assert service.delete_saved_location("missing") is False


def test_delete_existing_id_returns_true_and_removes_record(tmp_path):
    service = make_service(tmp_path)
    saved = service.save_location("Área", POLYGON)

    assert service.delete_saved_location(saved["id"]) is True
    assert service.get_saved_location(saved["id"]) is None


def test_save_is_persistent_across_service_instances(tmp_path):
    database_path = tmp_path / "locations.sqlite3"
    first_service = SavedLocationsService(SavedLocationsRepository(database_path))
    saved = first_service.save_location("Persistente", POLYGON)
    second_service = SavedLocationsService(SavedLocationsRepository(database_path))

    assert second_service.list_saved_locations()[0]["id"] == saved["id"]
    assert second_service.get_saved_location(saved["id"]) == saved


def test_duplicate_error_does_not_hide_non_conflict_storage_errors(tmp_path, monkeypatch):
    repository = SavedLocationsRepository(tmp_path / "locations.sqlite3")
    service = SavedLocationsService(repository)
    repository.initialize()

    def fail_insert(record):
        raise sqlite3.OperationalError("disk is unavailable")

    monkeypatch.setattr(repository, "insert_location", fail_insert)

    with pytest.raises(sqlite3.OperationalError):
        service.save_location("Área", POLYGON)


def test_save_reports_unexpected_missing_read_after_insert(tmp_path, monkeypatch):
    repository = SavedLocationsRepository(tmp_path / "locations.sqlite3")
    service = SavedLocationsService(repository)
    monkeypatch.setattr(repository, "get_location", lambda location_id: None)

    with pytest.raises(SavedLocationServiceError, match="gravada"):
        service.save_location("Área", POLYGON)
