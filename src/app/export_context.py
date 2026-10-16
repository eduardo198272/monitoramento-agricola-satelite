"""Validation and normalization for a completed multi-index export snapshot."""

from datetime import date
from math import isfinite
from typing import Any

from src.app.utils import normalize_date

SUPPORTED_INDICES = ("NDVI", "NDWI", "NDMI")


class ExportContextError(ValueError):
    """Raised when the current analysis cannot be exported as a full snapshot."""


def _validate_geometry(geometry_geojson: Any) -> dict:
    if not isinstance(geometry_geojson, dict) or geometry_geojson.get("type") != "Polygon":
        raise ExportContextError("A geometria GeoJSON da análise deve ser um Polygon válido")

    rings = geometry_geojson.get("coordinates")
    if not isinstance(rings, list) or not rings:
        raise ExportContextError("A geometria GeoJSON da análise está ausente ou inválida")

    normalized_rings = []
    for ring in rings:
        if not isinstance(ring, list) or len(ring) < 4:
            raise ExportContextError("A geometria GeoJSON contém um anel inválido")
        normalized_ring = []
        for point in ring:
            if (
                not isinstance(point, (list, tuple))
                or len(point) < 2
                or any(
                    isinstance(value, bool)
                    or not isinstance(value, (int, float))
                    or not isfinite(value)
                    for value in point[:2]
                )
            ):
                raise ExportContextError("A geometria GeoJSON contém coordenadas inválidas")
            longitude, latitude = point[:2]
            if not -180 <= longitude <= 180 or not -90 <= latitude <= 90:
                raise ExportContextError("A geometria GeoJSON contém coordenadas fora do WGS84")
            normalized_ring.append(list(point))
        if normalized_ring[0] != normalized_ring[-1]:
            raise ExportContextError("A geometria GeoJSON contém um anel não fechado")
        signed_area = sum(
            normalized_ring[index][0] * normalized_ring[index + 1][1]
            - normalized_ring[index + 1][0] * normalized_ring[index][1]
            for index in range(len(normalized_ring) - 1)
        )
        if signed_area == 0:
            raise ExportContextError("A geometria GeoJSON contém um anel sem área válida")
        normalized_rings.append(normalized_ring)

    result = {"type": "Polygon", "coordinates": normalized_rings}
    if "crs" in geometry_geojson:
        result["crs"] = geometry_geojson["crs"]
    return result


def build_export_context(
    analysis: dict,
    geometry_geojson: dict,
    start_date: str | date,
    end_date: str | date,
) -> dict:
    """Validate and normalize data from a successful three-index analysis.

    This function is deliberately local and side-effect free: it does not invoke
    the analysis pipeline or any remote service, and leaves its inputs untouched.
    """
    if not isinstance(analysis, dict) or analysis.get("success") is not True:
        raise ExportContextError("A exportação exige uma análise concluída com sucesso")

    indices = analysis.get("indices")
    if not isinstance(indices, dict):
        raise ExportContextError("A exportação exige análise multiíndice (Todos)")
    missing = [name for name in SUPPORTED_INDICES if not isinstance(indices.get(name), dict)]
    missing.extend(
        name
        for name in SUPPORTED_INDICES
        if isinstance(indices.get(name), dict)
        and not {"index_map", "time_series", "anomalies"}.issubset(indices[name])
    )
    if missing:
        raise ExportContextError(
            "A análise multiíndice está incompleta; faltam resultados válidos para "
            + ", ".join(missing)
        )

    try:
        normalized_start = normalize_date(start_date)
        normalized_end = normalize_date(end_date)
    except (TypeError, ValueError) as error:
        raise ExportContextError(f"Data inválida no período da análise: {error}") from error
    if normalized_end < normalized_start:
        raise ExportContextError("Período inválido: a data inicial é posterior à data final")

    geometry = _validate_geometry(geometry_geojson)
    return {
        "period": {"start_date": normalized_start, "end_date": normalized_end},
        "geometry_geojson": geometry,
        "area_ha": analysis.get("area_ha"),
        "map_center": list(analysis["map_center"])
        if isinstance(analysis.get("map_center"), (list, tuple))
        else analysis.get("map_center"),
        "indices": {
            name: dict(indices[name]) for name in SUPPORTED_INDICES
        },
        "image_count": analysis.get("image_count"),
        "climate_data": analysis.get("climate_data"),
        "climate_summary": analysis.get("climate_summary"),
    }
