"""Portable, bounded GeoJSON location files with no remote dependencies."""

import json

from src.app.saved_locations_validation import (
    SavedLocationValidationError,
    prepare_saved_location,
)

MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_LOCATIONS = 100


def parse_locations_geojson(payload: bytes) -> list[dict]:
    """Validate the entire file before allowing any repository write."""
    if len(payload) > MAX_FILE_BYTES:
        raise SavedLocationValidationError("O arquivo deve ter no máximo 2 MB.")
    try:
        document = json.loads(payload.decode("utf-8-sig"))
    except (UnicodeError, ValueError, RecursionError) as error:
        raise SavedLocationValidationError("O arquivo não contém JSON UTF-8 válido.") from error
    if not isinstance(document, dict):
        raise SavedLocationValidationError("Envie uma Feature ou FeatureCollection GeoJSON.")
    if document.get("type") == "Feature":
        features = [document]
    elif document.get("type") == "FeatureCollection":
        features = document.get("features")
    else:
        raise SavedLocationValidationError("Envie uma Feature ou FeatureCollection GeoJSON.")
    if not isinstance(features, list) or not 1 <= len(features) <= MAX_LOCATIONS:
        raise SavedLocationValidationError("O arquivo deve conter entre 1 e 100 localizações.")

    prepared = []
    names = set()
    for feature in features:
        if not isinstance(feature, dict) or feature.get("type") != "Feature":
            raise SavedLocationValidationError("Cada localização deve ser uma Feature GeoJSON.")
        properties = feature.get("properties")
        if not isinstance(properties, dict):
            raise SavedLocationValidationError("Cada localização deve informar properties.name.")
        # Only import the name and geometry, not arbitrary untrusted metadata.
        record = prepare_saved_location(properties.get("name"), feature.get("geometry"))
        if record["normalized_name"] in names:
            raise SavedLocationValidationError("O arquivo contém nomes de localização repetidos.")
        names.add(record["normalized_name"])
        prepared.append(record)
    return prepared


def export_locations_geojson(locations: list[dict]) -> bytes:
    """Export only portable names and geometries, without internal IDs."""
    features = []
    for location in locations:
        prepared = prepare_saved_location(location["name"], location["geojson"])
        geojson = prepared["geojson"]
        geometry = geojson["geometry"] if geojson.get("type") == "Feature" else geojson
        features.append({
            "type": "Feature",
            "properties": {"name": prepared["name"]},
            "geometry": geometry,
        })
    payload = json.dumps(
        {"type": "FeatureCollection", "features": features},
        ensure_ascii=False,
        allow_nan=False,
        indent=2,
    ).encode("utf-8")
    # Guarantee that downloaded files can be imported with the same limits.
    parse_locations_geojson(payload)
    return payload
