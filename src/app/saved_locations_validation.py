"""Pure input validation for named saved locations."""

import json
import math
from typing import Any


class SavedLocationValidationError(ValueError):
    """A saved-location name or GeoJSON value does not meet the contract."""


def normalize_location_name(name: str) -> tuple[str, str]:
    """Return the display name and case-insensitive duplicate-comparison key."""
    if not isinstance(name, str):
        raise SavedLocationValidationError("O nome da localização deve ser texto.")

    display_name = name.strip()
    if not display_name:
        raise SavedLocationValidationError("Informe um nome para a localização.")
    if len(display_name) > 100:
        raise SavedLocationValidationError("O nome deve ter no máximo 100 caracteres.")

    normalized_name = " ".join(display_name.split()).casefold()
    return display_name, normalized_name


def validate_saved_location_geojson(geojson: Any) -> dict:
    """Validate and detach a Polygon Geometry or Feature without remote services."""
    if not isinstance(geojson, dict):
        raise SavedLocationValidationError("A geometria deve ser um objeto GeoJSON.")

    geometry = geojson
    if geojson.get("type") == "Feature":
        geometry = geojson.get("geometry")
        if not isinstance(geometry, dict):
            raise SavedLocationValidationError("A Feature GeoJSON não contém geometria válida.")

    if geometry.get("type") != "Polygon":
        raise SavedLocationValidationError("A localização deve conter uma geometria Polygon.")

    rings = geometry.get("coordinates")
    if not isinstance(rings, (list, tuple)) or not rings:
        raise SavedLocationValidationError("O polígono deve conter ao menos um anel.")

    for ring in rings:
        _validate_ring(ring)

    try:
        # JSON round-trip gives callers an independent JSON-compatible value,
        # retaining coordinate precision while rejecting NaN and non-JSON data.
        detached_geojson = json.loads(
            json.dumps(geojson, ensure_ascii=False, allow_nan=False)
        )
    except (TypeError, ValueError, OverflowError) as error:
        raise SavedLocationValidationError(
            "A geometria contém valores que não podem ser serializados em JSON."
        ) from error

    # Validate the serialized copy too, so tuples are returned as JSON arrays
    # and all downstream users receive the exact representation to persist.
    if detached_geojson.get("type") == "Feature":
        detached_geometry = detached_geojson["geometry"]
    else:
        detached_geometry = detached_geojson
    detached_geometry["coordinates"] = [
        [list(point) for point in ring] for ring in rings
    ]
    return detached_geojson


def prepare_saved_location(name: str, geojson: Any) -> dict:
    """Validate inputs and return repository-ready name and geometry fields."""
    display_name, normalized_name = normalize_location_name(name)
    validated_geojson = validate_saved_location_geojson(geojson)
    return {
        "name": display_name,
        "normalized_name": normalized_name,
        "geojson": validated_geojson,
    }


def _validate_ring(ring: Any) -> list[list[int | float]]:
    if not isinstance(ring, (list, tuple)) or len(ring) < 4:
        raise SavedLocationValidationError(
            "Cada anel deve conter ao menos quatro posições e estar fechado."
        )

    normalized_ring = []
    for position in ring:
        if not isinstance(position, (list, tuple)) or len(position) < 2:
            raise SavedLocationValidationError("Uma posição do polígono está malformada.")
        if any(
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or (isinstance(value, float) and not math.isfinite(value))
            for value in position
        ):
            raise SavedLocationValidationError("As coordenadas devem ser números finitos.")

        longitude, latitude = position[:2]
        if not -180 <= longitude <= 180 or not -90 <= latitude <= 90:
            raise SavedLocationValidationError(
                "As coordenadas devem estar dentro dos limites geográficos WGS84."
            )
        normalized_ring.append(list(position))

    if normalized_ring[0] != normalized_ring[-1]:
        raise SavedLocationValidationError("O anel do polígono deve estar fechado.")
    if len({tuple(position[:2]) for position in normalized_ring[:-1]}) < 3:
        raise SavedLocationValidationError(
            "O polígono deve conter ao menos três vértices distintos."
        )
    if _signed_ring_area(normalized_ring) == 0:
        raise SavedLocationValidationError("O anel do polígono deve possuir área maior que zero.")
    return normalized_ring


def _signed_ring_area(ring: list[list[int | float]]) -> float:
    return sum(
        ring[index][0] * ring[index + 1][1]
        - ring[index + 1][0] * ring[index][1]
        for index in range(len(ring) - 1)
    )
