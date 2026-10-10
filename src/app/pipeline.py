import ee
import logging
from datetime import date

import pandas as pd
import plotly.graph_objects as go

from src.app.earth_engine import (
    get_image_collection,
    calculate_ndvi,
    calculate_ndwi,
    calculate_ndmi,
    mask_clouds,
)
from src.app.time_series import compute_time_series, plot_time_series
from src.app.anomalies import compute_trend, detect_anomalies, generate_alert
from src.app.climate import fetch_climate_data, plot_climate_data
from src.app.utils import normalize_date

logger = logging.getLogger(__name__)


def _fetch_climate_context(
    geometry: ee.Geometry,
    start_date: str,
    end_date: str,
    log_message: str,
    log_context: dict,
) -> tuple[pd.DataFrame | None, go.Figure | None, list[float] | None]:
    """Fetch shared climate data and return its centroid for map positioning."""
    map_center = None
    try:
        longitude, latitude = geometry.centroid().coordinates().getInfo()
        map_center = [latitude, longitude]
        coordinates = (longitude, latitude)
        climate_data = fetch_climate_data(
            geometry, start_date, end_date, coordinates=coordinates
        )
    except Exception:
        logger.warning(log_message, exc_info=True, extra=log_context)
        return None, None, map_center

    climate_plot = (
        plot_climate_data(climate_data)
        if climate_data is not None and not climate_data.empty
        else None
    )
    return climate_data, climate_plot, map_center


def run_analysis(
    geometry: ee.Geometry,
    start_date: str | date,
    end_date: str | date,
    index_name: str,
    area_ha: float | None = None,
) -> dict:
    try:
        start_date = normalize_date(start_date)
        end_date = normalize_date(end_date)
        collection = get_image_collection(geometry, start_date, end_date)

        image_count = collection.size().getInfo()
        if image_count == 0:
            return {
                "success": False,
                "error": "Nenhuma imagem encontrada para o período e área selecionados"
            }

        collection = collection.map(mask_clouds)

        if index_name == "NDVI":
            index_collection = collection.map(calculate_ndvi)
        elif index_name == "NDWI":
            index_collection = collection.map(calculate_ndwi)
        elif index_name == "NDMI":
            index_collection = collection.map(calculate_ndmi)
        else:
            return {
                "success": False,
                "error": f"Índice não suportado: {index_name}"
            }

        index_map = index_collection.median()

        band_name = index_name
        stats = index_map.select(band_name).reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=geometry,
            scale=10,
            maxPixels=1e9
        ).getInfo()

        mean_value = stats.get(band_name)

        if area_ha is None:
            area_ha = geometry.area().divide(10000).getInfo()

        time_series = compute_time_series(
            index_collection, geometry, index_name, scale=10,
            image_count=image_count,
        )

        time_series_plot = plot_time_series(time_series, index_name) if time_series else None

        anomalies = detect_anomalies(time_series, window_size=3, std_threshold=1.0)
        alert = generate_alert(anomalies, index_name)

        climate_df, climate_plot, map_center = _fetch_climate_context(
            geometry,
            start_date,
            end_date,
            "Climate data unavailable during single-index analysis",
            {"index_name": index_name},
        )

        return {
            "success": True,
            "index_name": index_name,
            "index_map": index_map,
            "time_series": time_series,
            "time_series_plot": time_series_plot,
            "anomalies": anomalies,
            "alert": alert,
            "climate_data": climate_df,
            "climate_plot": climate_plot,
            "mean_value": mean_value,
            "area_ha": area_ha,
            "map_center": map_center,
        }

    except Exception as e:
        logger.exception(
            "Single-index analysis failed",
            extra={
                "index_name": index_name,
                "start_date": str(start_date),
                "end_date": str(end_date),
            },
        )
        return {
            "success": False,
            "error": str(e)
        }


def run_multi_analysis(
    geometry: ee.Geometry,
    start_date: str | date,
    end_date: str | date,
    index_names: list[str],
    area_ha: float | None = None,
) -> dict:
    index_calculators = {
        "NDVI": calculate_ndvi,
        "NDWI": calculate_ndwi,
        "NDMI": calculate_ndmi,
    }

    if not index_names:
        return {
            "success": False,
            "error": "Selecione ao menos um índice para analisar",
        }

    unsupported_indices = [
        index_name for index_name in index_names
        if index_name not in index_calculators
    ]
    if unsupported_indices:
        return {
            "success": False,
            "error": f"Índice(s) não suportado(s): {', '.join(unsupported_indices)}",
        }

    try:
        start_date = normalize_date(start_date)
        end_date = normalize_date(end_date)
        collection = get_image_collection(geometry, start_date, end_date)
        image_count = collection.size().getInfo()

        if image_count == 0:
            return {
                "success": False,
                "error": "Nenhuma imagem encontrada para o período e área selecionados",
            }

        masked_collection = collection.map(mask_clouds)
        if area_ha is None:
            area_ha = geometry.area().divide(10000).getInfo()

        climate_data, climate_plot, map_center = _fetch_climate_context(
            geometry,
            start_date,
            end_date,
            "Climate data unavailable during multi-index analysis",
            {"index_names": tuple(dict.fromkeys(index_names))},
        )

        index_results = {}
        for index_name in dict.fromkeys(index_names):
            index_collection = masked_collection.map(index_calculators[index_name])
            index_map = index_collection.median()
            stats = index_map.select(index_name).reduceRegion(
                reducer=ee.Reducer.mean(),
                geometry=geometry,
                scale=10,
                maxPixels=1e9,
            ).getInfo()
            time_series = compute_time_series(
                index_collection, geometry, index_name, scale=10,
                image_count=image_count,
            )
            anomalies = detect_anomalies(
                time_series, window_size=3, std_threshold=1.0
            )

            index_results[index_name] = {
                "index_map": index_map,
                "time_series": time_series,
                "time_series_plot": (
                    plot_time_series(time_series, index_name)
                    if time_series
                    else None
                ),
                "anomalies": anomalies,
                "alert": generate_alert(anomalies, index_name),
                "mean_value": stats.get(index_name),
                "trend": compute_trend(time_series),
            }

        return {
            "success": True,
            "indices": index_results,
            "area_ha": area_ha,
            "image_count": image_count,
            "climate_data": climate_data,
            "climate_plot": climate_plot,
            "map_center": map_center,
        }
    except Exception as e:
        logger.exception(
            "Multi-index analysis failed",
            extra={
                "index_names": tuple(dict.fromkeys(index_names)),
                "start_date": str(start_date),
                "end_date": str(end_date),
            },
        )
        return {
            "success": False,
            "error": str(e),
        }
