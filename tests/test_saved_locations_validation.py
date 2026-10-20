from copy import deepcopy

import pytest

from src.app.saved_locations_repository import SavedLocationsRepository
from src.app.saved_locations_validation import (
    SavedLocationValidationError,
    normalize_location_name,
    prepare_saved_location,
    validate_saved_location_geojson,
)


POLYGON = {
    "type": "Polygon",
    "coordinates": [[[1.123456789012345, 2], [3, 2], [3, 4], [1.123456789012345, 2]]],
}


def test_name_is_trimmed_and_comparison_key_collapses_spaces_and_case():
    assert normalize_location_name("  Área   Norte  ") == ("Área   Norte", "área norte")
    assert normalize_location_name("CAMPO	A") == ("CAMPO\tA", "campo a")


@pytest.mark.parametrize("value", ["", "   ", "\t\n"])
def test_blank_name_is_rejected(value):
    with pytest.raises(SavedLocationValidationError, match="Informe"):
        normalize_location_name(value)


def test_name_over_100_characters_is_rejected_after_trim():
    with pytest.raises(SavedLocationValidationError, match="100"):
        normalize_location_name(" " + "x" * 101 + " ")


def test_name_exactly_100_characters_is_allowed():
    display_name, normalized_name = normalize_location_name("x" * 100)

    assert len(display_name) == 100
    assert normalized_name == "x" * 100


@pytest.mark.parametrize("value", [None, 123, ["field"]])
def test_non_string_name_is_rejected(value):
    with pytest.raises(SavedLocationValidationError, match="texto"):
        normalize_location_name(value)


def test_valid_polygon_is_detached_and_precision_is_preserved():
    source = deepcopy(POLYGON)

    result = validate_saved_location_geojson(source)

    assert result == source
    assert result is not source
    assert result["coordinates"] is not source["coordinates"]
    assert result["coordinates"][0][0][0] == 1.123456789012345


def test_feature_polygon_is_supported_and_properties_are_preserved():
    feature = {
        "type": "Feature",
        "properties": {"description": "área agrícola"},
        "geometry": POLYGON,
    }

    result = validate_saved_location_geojson(feature)

    assert result["type"] == "Feature"
    assert result["geometry"] == POLYGON
    assert result["properties"] == feature["properties"]


@pytest.mark.parametrize("value", [None, "polygon", []])
def test_non_object_geojson_is_rejected(value):
    with pytest.raises(SavedLocationValidationError, match="objeto GeoJSON"):
        validate_saved_location_geojson(value)


def test_feature_without_geometry_is_rejected():
    with pytest.raises(SavedLocationValidationError, match="Feature"):
        validate_saved_location_geojson({"type": "Feature", "geometry": None})


@pytest.mark.parametrize(
    "value",
    [
        {"type": "Point", "coordinates": [1, 2]},
        {"type": "Feature", "geometry": {"type": "Point", "coordinates": [1, 2]}},
    ],
)
def test_non_polygon_geojson_is_rejected(value):
    with pytest.raises(SavedLocationValidationError, match="Polygon"):
        validate_saved_location_geojson(value)


@pytest.mark.parametrize("coordinates", [None, [], "not-rings"])
def test_missing_or_invalid_polygon_rings_are_rejected(coordinates):
    with pytest.raises(SavedLocationValidationError, match="anel"):
        validate_saved_location_geojson({"type": "Polygon", "coordinates": coordinates})


@pytest.mark.parametrize(
    "ring",
    [
        None,
        [],
        [[0, 0], [1, 0], [0, 0]],
        [[0, 0], [1, 0], [1, 1], [2, 2]],  # open ring
        [[0, 0], [1, 1], [0, 0], [0, 0]],  # fewer than three unique points
        [[0, 0], [1, 1], [2, 2], [0, 0]],  # zero area
    ],
)
def test_invalid_rings_are_rejected(ring):
    with pytest.raises(SavedLocationValidationError):
        validate_saved_location_geojson({"type": "Polygon", "coordinates": [ring]})


@pytest.mark.parametrize(
    "position",
    [
        [181, 0],
        [-181, 0],
        [0, 91],
        [0, -91],
        [float("nan"), 0],
        [0, float("inf")],
        [True, 0],
        ["1", 0],
        [0],
        None,
    ],
)
def test_invalid_coordinate_positions_are_rejected(position):
    coordinates = [position, [3, 2], [3, 4], position]
    with pytest.raises(SavedLocationValidationError):
        validate_saved_location_geojson({"type": "Polygon", "coordinates": [coordinates]})


def test_unserializable_feature_properties_are_rejected():
    feature = {
        "type": "Feature",
        "geometry": POLYGON,
        "properties": {"not_json": object()},
    }

    with pytest.raises(SavedLocationValidationError, match="serializados"):
        validate_saved_location_geojson(feature)


def test_prepared_values_can_be_persisted_and_duplicate_keys_match(tmp_path):
    prepared = prepare_saved_location("  Fazenda   São José ", POLYGON)
    repository = SavedLocationsRepository(tmp_path / "saved.sqlite3")
    repository.initialize()
    repository.insert_location({
        **prepared,
        "id": "location-1",
        "center_lat": 3.0,
        "center_lon": 2.0,
        "created_at": "2026-10-20T10:00:00+00:00",
        "updated_at": "2026-10-20T10:00:00+00:00",
    })

    assert prepared["name"] == "Fazenda   São José"
    assert prepared["normalized_name"] == "fazenda são josé"
    assert repository.get_location("location-1")["geojson"] == POLYGON
    assert normalize_location_name("FAZENDA SÃO JOSÉ")[1] == prepared["normalized_name"]


@pytest.mark.parametrize(
    "value",
    [
        {"type": "Polygon", "coordinates": [[[0, 0], [1, 0], [1, 1], [0, 0]]], "extra": object()},
        {"type": "Polygon", "coordinates": [[[0, 0], [1, 0], [1, 1], [0, 0]]], "extra": float("nan")},
    ],
)
def test_non_json_geojson_metadata_is_rejected(value):
    with pytest.raises(SavedLocationValidationError, match="serializados"):
        validate_saved_location_geojson(value)
