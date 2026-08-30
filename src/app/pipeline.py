import ee
import pandas as pd

from src.app.earth_engine import (
    get_image_collection,
    calculate_ndvi,
    calculate_ndwi,
    calculate_ndmi,
    mask_clouds,
)
from src.app.time_series import compute_time_series, plot_time_series
from src.app.anomalies import detect_anomalies, generate_alert, compute_trend
from src.app.climate import fetch_climate_data, plot_climate_data


def run_analysis(
    geometry: ee.Geometry,
    start_date: str,
    end_date: str,
    index_name: str
) -> dict:
    try:
        collection = get_image_collection(geometry, start_date, end_date)

        if collection.size().getInfo() == 0:
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

        area_ha = geometry.area().divide(10000).getInfo()

        time_series = compute_time_series(
            index_collection, geometry, index_name, scale=10
        )

        time_series_plot = plot_time_series(time_series, index_name) if time_series else None

        anomalies = detect_anomalies(time_series, window_size=3, std_threshold=1.0)
        alert = generate_alert(anomalies, index_name)

        try:
            climate_df = fetch_climate_data(geometry, start_date, end_date)
        except Exception:
            climate_df = pd.DataFrame()

        climate_plot = plot_climate_data(climate_df) if not climate_df.empty else None

        return {
            "success": True,
            "index_map": index_map,
            "time_series": time_series,
            "time_series_plot": time_series_plot,
            "anomalies": anomalies,
            "alert": alert,
            "climate_data": climate_df,
            "climate_plot": climate_plot,
            "mean_value": mean_value,
            "area_ha": area_ha,
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
