from contextlib import ExitStack
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
import plotly.graph_objects as go

from src.app.main import run_analysis


@pytest.fixture
def main_analysis_mocks():
    with ExitStack() as stack:
        mocks = {
            name: stack.enter_context(patch(f"src.app.main.{name}"))
            for name in (
                "get_image_collection",
                "mask_clouds",
                "calculate_ndvi",
                "calculate_ndwi",
                "calculate_ndmi",
                "compute_time_series",
                "plot_time_series",
                "detect_anomalies",
                "generate_alert",
                "fetch_climate_data",
                "plot_climate_data",
                "ee",
            )
        }

        geometry = MagicMock(name="geometry")
        geometry.area.return_value.divide.return_value.getInfo.return_value = 12.5

        collection = MagicMock(name="collection")
        masked_collection = MagicMock(name="masked_collection")
        index_collection = MagicMock(name="index_collection")
        index_image = MagicMock(name="index_image")
        collection.map.side_effect = [masked_collection, index_collection]
        masked_collection.map.return_value = index_collection
        index_collection.median.return_value = index_image
        index_image.select.return_value.reduceRegion.return_value.getInfo.return_value = {
            "NDVI": 0.65,
            "NDWI": 0.25,
            "NDMI": 0.35,
        }
        collection.size.return_value.getInfo.return_value = 3

        mocks["get_image_collection"].return_value = collection
        mocks["compute_time_series"].return_value = []
        mocks["detect_anomalies"].return_value = []
        mocks["generate_alert"].return_value = None
        mocks["fetch_climate_data"].return_value = pd.DataFrame()
        mocks["ee"].Reducer.mean.return_value = "mean_reducer"
        mocks["plot_time_series"].return_value = go.Figure()
        mocks["plot_climate_data"].return_value = go.Figure()

        yield mocks, geometry, collection, masked_collection, index_collection, index_image


@pytest.mark.parametrize(
    "index_name, calculation_name, mean_value",
    [
        ("NDVI", "calculate_ndvi", 0.65),
        ("NDWI", "calculate_ndwi", 0.25),
        ("NDMI", "calculate_ndmi", 0.35),
    ],
)
def test_run_analysis_supports_all_indices(
    main_analysis_mocks, index_name, calculation_name, mean_value
):
    mocks, geometry, collection, masked_collection, _, index_image = main_analysis_mocks
    result = run_analysis(geometry, "2026-01-01", "2026-01-31", index_name)

    assert result["success"] is True
    assert result["index_name"] == index_name
    assert result["mean_value"] == mean_value
    assert result["area_ha"] == 12.5
    assert result["time_series"] == []
    assert result["time_series_plot"] is None
    assert result["climate_data"].empty
    assert result["climate_plot"] is None
    mocks["get_image_collection"].assert_called_once_with(
        geometry, "2026-01-01", "2026-01-31"
    )
    collection.map.assert_any_call(mocks["mask_clouds"])
    masked_collection.map.assert_called_once_with(mocks[calculation_name])
    index_image.select.assert_called_once_with(index_name)
    mocks["compute_time_series"].assert_called_once_with(
        masked_collection.map.return_value, geometry, index_name, scale=10
    )


def test_run_analysis_returns_error_for_empty_collection(main_analysis_mocks):
    mocks, geometry, collection, *_ = main_analysis_mocks
    collection.size.return_value.getInfo.return_value = 0

    result = run_analysis(geometry, "2026-01-01", "2026-01-31", "NDVI")

    assert result == {
        "success": False,
        "error": "Nenhuma imagem encontrada para o período e área selecionados",
    }
    collection.map.assert_not_called()
    mocks["compute_time_series"].assert_not_called()


def test_run_analysis_returns_error_for_unsupported_index(main_analysis_mocks):
    _, geometry, collection, masked_collection, *_ = main_analysis_mocks

    result = run_analysis(geometry, "2026-01-01", "2026-01-31", "INVALID")

    assert result == {
        "success": False,
        "error": "Índice não suportado: INVALID",
    }
    collection.map.assert_called_once()
    masked_collection.map.assert_not_called()


def test_run_analysis_returns_error_when_processing_fails(main_analysis_mocks):
    mocks, geometry, *_ = main_analysis_mocks
    mocks["get_image_collection"].side_effect = RuntimeError("Earth Engine error")

    result = run_analysis(geometry, "2026-01-01", "2026-01-31", "NDVI")

    assert result == {"success": False, "error": "Earth Engine error"}


def test_run_analysis_includes_time_series_and_climate_plots(main_analysis_mocks):
    mocks, geometry, *_ = main_analysis_mocks
    time_series = [
        {"date": "2026-01-01", "value": 0.5},
        {"date": "2026-01-02", "value": 0.7},
    ]
    climate_data = pd.DataFrame(
        {"date": ["2026-01-01"], "precipitation": [4.0], "temperature": [25.0]}
    )
    anomalies = [{"date": "2026-01-02", "value": 0.7}]
    alert = "ALERTA: queda detectada"
    time_series_plot = go.Figure()
    climate_plot = go.Figure()
    mocks["compute_time_series"].return_value = time_series
    mocks["plot_time_series"].return_value = time_series_plot
    mocks["detect_anomalies"].return_value = anomalies
    mocks["generate_alert"].return_value = alert
    mocks["fetch_climate_data"].return_value = climate_data
    mocks["plot_climate_data"].return_value = climate_plot

    result = run_analysis(geometry, "2026-01-01", "2026-01-31", "NDVI")

    assert result["time_series"] == time_series
    assert result["time_series_plot"] is time_series_plot
    assert result["anomalies"] == anomalies
    assert result["alert"] == alert
    assert result["climate_data"] is climate_data
    assert result["climate_plot"] is climate_plot
    mocks["plot_time_series"].assert_called_once_with(time_series, "NDVI")
    mocks["detect_anomalies"].assert_called_once_with(
        time_series, window_size=3, std_threshold=1.0
    )
    mocks["generate_alert"].assert_called_once_with(anomalies, "NDVI")
    mocks["fetch_climate_data"].assert_called_once_with(
        geometry, "2026-01-01", "2026-01-31"
    )
    mocks["plot_climate_data"].assert_called_once_with(climate_data)


def test_run_analysis_continues_when_climate_fetch_fails(main_analysis_mocks):
    mocks, geometry, *_ = main_analysis_mocks
    mocks["fetch_climate_data"].side_effect = RuntimeError("Climate API error")

    result = run_analysis(geometry, "2026-01-01", "2026-01-31", "NDVI")

    assert result["success"] is True
    assert result["climate_data"] is None
    assert result["climate_plot"] is None
    mocks["plot_climate_data"].assert_not_called()
