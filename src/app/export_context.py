"""Validation and normalization for a completed multi-index export snapshot."""

from copy import deepcopy
from datetime import date, datetime
from math import isfinite
from typing import Any

import pandas as pd

from src.app.utils import normalize_date

SUPPORTED_INDICES = ("NDVI", "NDWI", "NDMI")


class ExportContextError(ValueError):
    """Raised when the current analysis cannot be exported as a full snapshot."""


_NON_COPYABLE_FIELDS = {"index_map", "time_series_plot", "climate_plot"}


def _normalize_tabular_date(value: Any) -> Any:
    if value is None:
        return value
    if not isinstance(value, str):
        try:
            if bool(pd.isna(value)):
                return value
        except (TypeError, ValueError):
            pass
    if isinstance(value, str) and len(value) == 8 and value.isdigit():
        try:
            return datetime.strptime(value, "%Y%m%d").date().isoformat()
        except ValueError as error:
            raise ExportContextError(f"Data tabular inválida: {value}") from error
    try:
        return normalize_date(value)
    except (TypeError, ValueError) as error:
        raise ExportContextError(f"Data tabular inválida: {value}") from error


def _copy_export_value(value: Any, field_name: str | None = None) -> Any:
    """Detach mutable data while retaining opaque pipeline/rendering objects."""
    if field_name in _NON_COPYABLE_FIELDS:
        return value
    if isinstance(value, pd.DataFrame):
        result = value.copy(deep=True)
        if "date" in result.columns:
            result["date"] = result["date"].map(_normalize_tabular_date)
        return result
    if field_name == "date":
        return _normalize_tabular_date(value)
    if isinstance(value, dict):
        return {
            key: _copy_export_value(item, key if isinstance(key, str) else None)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_copy_export_value(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_copy_export_value(item) for item in value)
    return deepcopy(value)


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

    geometry = _copy_export_value(_validate_geometry(geometry_geojson))
    context = {
        "period": {"start_date": normalized_start, "end_date": normalized_end},
        "geometry_geojson": geometry,
        "area_ha": _copy_export_value(analysis.get("area_ha")),
        "map_center": _copy_export_value(analysis.get("map_center")),
        "indices": {
            name: _copy_export_value(indices[name]) for name in SUPPORTED_INDICES
        },
        "image_count": _copy_export_value(analysis.get("image_count")),
        "climate_data": _copy_export_value(analysis.get("climate_data")),
        "climate_summary": _copy_export_value(analysis.get("climate_summary")),
    }
    if "collection_metadata" in analysis:
        context["collection_metadata"] = _copy_export_value(
            analysis["collection_metadata"]
        )
    return context
