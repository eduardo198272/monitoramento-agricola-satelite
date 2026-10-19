"""In-memory CSV ZIP export for normalized multi-index analysis snapshots."""

import csv
from datetime import date, datetime
from io import BytesIO, StringIO
import json
import math
from typing import Any
import zipfile

import pandas as pd

from src.app.export_context import SUPPORTED_INDICES
from src.app.export_xlsx import _to_iso_date

CSV_SCHEMAS = {
    "resumo.csv": ("campo", "valor", "unidade"),
    "ndvi.csv": ("date", "value", "trend", "anomaly"),
    "ndwi.csv": ("date", "value", "trend", "anomaly"),
    "ndmi.csv": ("date", "value", "trend", "anomaly"),
    "clima.csv": (
        "date", "precipitation_mm", "temperature_c",
        "solar_radiation_mj_m2_day",
    ),
    "anomalias.csv": ("index", "date", "value", "anomaly", "classification"),
    "geografia.csv": ("field", "value", "unit"),
}


def _number(value: Any) -> int | float | None:
    """Keep finite numeric values numeric in CSV; represent missing/invalid as empty."""
    if value is None or isinstance(value, bool):
        return None
    if not isinstance(value, (int, float)):
        try:
            value = float(value)
        except (TypeError, ValueError):
            return None
    return value if math.isfinite(value) else None


def _cell(value: Any) -> Any:
    """Convert values to stable CSV scalar representations."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        number = _number(value)
        return "" if number is None else number
    if isinstance(value, (date, datetime)):
        return value.date().isoformat() if isinstance(value, datetime) else value.isoformat()
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass
    return str(value)


def _records(value: Any) -> list[dict]:
    if value is None:
        return []
    if isinstance(value, pd.DataFrame):
        return value.to_dict(orient="records")
    if isinstance(value, dict):
        return [value]
    if isinstance(value, (list, tuple)):
        return [record for record in value if isinstance(record, dict)]
    return []


def _csv_bytes(headers: tuple[str, ...], rows: list[dict]) -> bytes:
    text = StringIO(newline="")
    writer = csv.DictWriter(text, fieldnames=headers, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({key: _cell(row.get(key)) for key in headers})
    return text.getvalue().encode("utf-8")


def _summary_rows(context: dict, generated_at: date | datetime) -> list[dict]:
    period = context.get("period") or {}
    climate = context.get("climate_summary") or {}
    values = [
        ("periodo_inicial", period.get("start_date"), ""),
        ("periodo_final", period.get("end_date"), ""),
        ("area_ha", context.get("area_ha"), "ha" if context.get("area_ha") is not None else ""),
        ("imagens_analisadas", context.get("image_count"), "imagens" if context.get("image_count") is not None else ""),
        ("data_geracao", generated_at.date().isoformat() if isinstance(generated_at, datetime) else generated_at.isoformat(), ""),
        ("precipitacao_total_mm", climate.get("total_precipitation_mm", climate.get("precipitation_mm")), "mm"),
        ("temperatura_media_c", climate.get("mean_temperature_c", climate.get("temperature_c")), "C"),
        ("radiacao_solar_media_mj_m2_dia", climate.get("mean_solar_radiation_mj_m2_day", climate.get("solar_radiation_mj_m2_day")), "MJ/m2/dia"),
    ]
    return [{"campo": field, "valor": value, "unidade": unit} for field, value, unit in values]


def _index_rows(index_data: dict) -> list[dict]:
    anomaly_dates = {
        _to_iso_date(item.get("date"))
        for item in _records(index_data.get("anomalies"))
        if item.get("anomaly") is True and item.get("date") is not None
    }
    trend = index_data.get("trend")
    return [
        {
            "date": _to_iso_date(record.get("date")),
            "value": _number(record.get("value")),
            "trend": trend,
            "anomaly": _to_iso_date(record.get("date")) in anomaly_dates,
        }
        for record in _records(index_data.get("time_series"))
    ]


def _climate_rows(climate_data: Any) -> list[dict]:
    """Map pipeline NASA POWER names to the stable export schema."""
    result = []
    for record in _records(climate_data):
        radiation = record.get("solar_radiation_mj_m2_day")
        if radiation is None:
            raw_radiation = record.get("solar_radiation")
            radiation = _number(raw_radiation)
            # NASA POWER source values are kWh/m²/day; export contract is MJ/m²/day.
            if radiation is not None:
                radiation *= 3.6
        result.append({
            "date": _to_iso_date(record.get("date")),
            "precipitation_mm": _number(record.get("precipitation_mm", record.get("precipitation"))),
            "temperature_c": _number(record.get("temperature_c", record.get("temperature"))),
            "solar_radiation_mj_m2_day": _number(radiation),
        })
    return result


def _anomaly_rows(indices: dict) -> list[dict]:
    rows = []
    for index_name in SUPPORTED_INDICES:
        for item in _records(indices[index_name].get("anomalies")):
            if item.get("anomaly") is not True:
                continue
            rows.append({
                "index": index_name,
                "date": _to_iso_date(item.get("date")),
                "value": _number(item.get("value")),
                "anomaly": True,
                "classification": item.get("classification"),
            })
    return rows


def _geography_rows(context: dict) -> list[dict]:
    geometry = context.get("geometry_geojson") or {}
    center = context.get("map_center")
    rows = [{"field": "area_ha", "value": context.get("area_ha"), "unit": "ha" if context.get("area_ha") is not None else ""}]
    if isinstance(center, (list, tuple)) and len(center) >= 2:
        rows.extend([
            {"field": "centroid_latitude", "value": center[0], "unit": "graus"},
            {"field": "centroid_longitude", "value": center[1], "unit": "graus"},
        ])
    crs = (geometry.get("crs") or {}).get("properties", {}).get("name", "EPSG:4326")
    rows.extend([
        {"field": "crs", "value": crs, "unit": ""},
        {"field": "geojson", "value": json.dumps(geometry, ensure_ascii=False, separators=(",", ":")), "unit": ""},
    ])
    return rows


def render_analysis_csv_zip(
    export_context: dict,
    *,
    generated_at: date | datetime | None = None,
) -> bytes:
    """Return a ZIP with the seven CSV datasets for a complete multi-index analysis."""
    if not isinstance(export_context, dict):
        raise ValueError("O contexto de exportacao deve ser um dicionario")
    indices = export_context.get("indices")
    if not isinstance(indices, dict) or any(
        name not in indices or not isinstance(indices[name], dict)
        for name in SUPPORTED_INDICES
    ):
        raise ValueError("O contexto deve conter NDVI, NDWI e NDMI")

    generated_at = generated_at or datetime.now()
    datasets = {
        "resumo.csv": _summary_rows(export_context, generated_at),
        "ndvi.csv": _index_rows(indices["NDVI"]),
        "ndwi.csv": _index_rows(indices["NDWI"]),
        "ndmi.csv": _index_rows(indices["NDMI"]),
        "clima.csv": _climate_rows(export_context.get("climate_data")),
        "anomalias.csv": _anomaly_rows(indices),
        "geografia.csv": _geography_rows(export_context),
    }
    output = BytesIO()
    with zipfile.ZipFile(output, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for filename, rows in datasets.items():
            archive.writestr(filename, _csv_bytes(CSV_SCHEMAS[filename], rows))
    return output.getvalue()
