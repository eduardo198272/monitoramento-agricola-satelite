import pytest
from unittest.mock import MagicMock, patch
import pandas as pd
import plotly.graph_objects as go

from src.app.pipeline import run_analysis


class TestRunAnalysis:
    @patch("src.app.pipeline.ee")
    @patch("src.app.pipeline.get_image_collection")
    @patch("src.app.pipeline.mask_clouds")
    @patch("src.app.pipeline.compute_time_series")
    @patch("src.app.pipeline.plot_time_series")
    @patch("src.app.pipeline.detect_anomalies")
    @patch("src.app.pipeline.generate_alert")
    @patch("src.app.pipeline.fetch_climate_data")
    @patch("src.app.pipeline.plot_climate_data")
    def test_run_analysis_success(
        self,
        mock_climate_plot,
        mock_fetch_climate,
        mock_generate_alert,
        mock_detect_anomalies,
        mock_plot_ts,
        mock_compute_ts,
        mock_mask_clouds,
        mock_get_col,
        mock_ee
    ):
        mock_geometry = MagicMock()
        mock_geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-45.0, -20.0]
        mock_geometry.area.return_value.divide.return_value.getInfo.return_value = 100.0

        mock_collection = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 5
        mock_get_col.return_value = mock_collection
        mock_mask_clouds.return_value = mock_collection

        mock_ts_data = [
            {"date": "2024-01-01", "value": 0.5},
            {"date": "2024-01-02", "value": 0.55},
            {"date": "2024-01-03", "value": 0.45},
        ]
        mock_compute_ts.return_value = mock_ts_data
        mock_plot_ts.return_value = go.Figure()
        mock_detect_anomalies.return_value = mock_ts_data
        mock_generate_alert.return_value = None

        mock_climate_df = pd.DataFrame({
            "date": ["2024-01-01", "2024-01-02"],
            "precipitation": [5.0, 3.5],
            "temperature": [25.0, 26.5],
        })
        mock_fetch_climate.return_value = mock_climate_df
        mock_climate_plot.return_value = go.Figure()

        mock_index_map = MagicMock()
        mock_collection.map.return_value.median.return_value = mock_index_map
        mock_index_map.select.return_value.reduceRegion.return_value.getInfo.return_value = {"NDVI": 0.65}

        result = run_analysis(mock_geometry, "2024-01-01", "2024-01-31", "NDVI")

        assert result["success"] is True
        assert "index_map" in result
        assert "time_series" in result
        assert "time_series_plot" in result
        assert "anomalies" in result
        assert "alert" in result
        assert "climate_data" in result
        assert "climate_plot" in result
        assert "mean_value" in result
        assert "area_ha" in result

    @patch("src.app.pipeline.ee")
    @patch("src.app.pipeline.get_image_collection")
    def test_run_analysis_no_images(self, mock_get_col, mock_ee):
        mock_geometry = MagicMock()

        mock_collection = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 0
        mock_get_col.return_value = mock_collection

        result = run_analysis(mock_geometry, "2024-01-01", "2024-01-31", "NDVI")

        assert result["success"] is False
        assert "error" in result
        assert "Nenhuma imagem encontrada" in result["error"]

    @patch("src.app.pipeline.ee")
    @patch("src.app.pipeline.get_image_collection")
    def test_run_analysis_invalid_index(self, mock_get_col, mock_ee):
        mock_geometry = MagicMock()

        mock_collection = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 5
        mock_get_col.return_value = mock_collection

        result = run_analysis(mock_geometry, "2024-01-01", "2024-01-31", "INVALID")

        assert result["success"] is False
        assert "error" in result
        assert "Índice não suportado" in result["error"]

    @patch("src.app.pipeline.get_image_collection")
    def test_run_analysis_exception_handling(self, mock_get_col):
        mock_geometry = MagicMock()

        mock_get_col.side_effect = Exception("Connection error")

        result = run_analysis(mock_geometry, "2024-01-01", "2024-01-31", "NDVI")

        assert result["success"] is False
        assert "error" in result
        assert "Connection error" in result["error"]

    @patch("src.app.pipeline.ee")
    @patch("src.app.pipeline.get_image_collection")
    @patch("src.app.pipeline.mask_clouds")
    @patch("src.app.pipeline.compute_time_series")
    @patch("src.app.pipeline.plot_time_series")
    @patch("src.app.pipeline.detect_anomalies")
    @patch("src.app.pipeline.generate_alert")
    @patch("src.app.pipeline.fetch_climate_data")
    @patch("src.app.pipeline.plot_climate_data")
    def test_run_analysis_climate_data_failure_continues(
        self,
        mock_climate_plot,
        mock_fetch_climate,
        mock_generate_alert,
        mock_detect_anomalies,
        mock_plot_ts,
        mock_compute_ts,
        mock_mask_clouds,
        mock_get_col,
        mock_ee
    ):
        mock_geometry = MagicMock()
        mock_geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-45.0, -20.0]
        mock_geometry.area.return_value.divide.return_value.getInfo.return_value = 100.0

        mock_collection = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 5
        mock_get_col.return_value = mock_collection
        mock_mask_clouds.return_value = mock_collection

        mock_ts_data = [{"date": "2024-01-01", "value": 0.5}]
        mock_compute_ts.return_value = mock_ts_data
        mock_plot_ts.return_value = go.Figure()
        mock_detect_anomalies.return_value = mock_ts_data
        mock_generate_alert.return_value = None
        mock_fetch_climate.side_effect = Exception("Climate API error")

        mock_index_map = MagicMock()
        mock_collection.map.return_value.median.return_value = mock_index_map
        mock_index_map.select.return_value.reduceRegion.return_value.getInfo.return_value = {"NDVI": 0.65}

        result = run_analysis(mock_geometry, "2024-01-01", "2024-01-31", "NDVI")

        assert result["success"] is True
        assert result["climate_data"].empty
        assert result["climate_plot"] is None

    @patch("src.app.pipeline.ee")
    @patch("src.app.pipeline.get_image_collection")
    @patch("src.app.pipeline.mask_clouds")
    @patch("src.app.pipeline.compute_time_series")
    @patch("src.app.pipeline.plot_time_series")
    @patch("src.app.pipeline.detect_anomalies")
    @patch("src.app.pipeline.generate_alert")
    @patch("src.app.pipeline.fetch_climate_data")
    @patch("src.app.pipeline.plot_climate_data")
    def test_run_analysis_mean_value_and_alert(
        self,
        mock_climate_plot,
        mock_fetch_climate,
        mock_generate_alert,
        mock_detect_anomalies,
        mock_plot_ts,
        mock_compute_ts,
        mock_mask_clouds,
        mock_get_col,
        mock_ee
    ):
        mock_geometry = MagicMock()
        mock_geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-45.0, -20.0]
        mock_geometry.area.return_value.divide.return_value.getInfo.return_value = 100.0

        mock_index_image = MagicMock()
        mock_index_image.select.return_value.reduceRegion.return_value.getInfo.return_value = {"NDVI": 0.65}

        mock_index_collection = MagicMock()
        mock_index_collection.median.return_value = mock_index_image

        mock_masked_collection = MagicMock()
        mock_masked_collection.map.return_value = mock_index_collection

        mock_collection = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 5
        mock_collection.map.return_value = mock_masked_collection
        mock_get_col.return_value = mock_collection

        mock_ts_data = [
            {"date": "2024-01-01", "value": 0.5},
            {"date": "2024-01-02", "value": 0.55},
            {"date": "2024-01-03", "value": 0.45},
        ]
        mock_compute_ts.return_value = mock_ts_data
        mock_plot_ts.return_value = go.Figure()
        mock_detect_anomalies.return_value = mock_ts_data
        mock_generate_alert.return_value = "ALERTA: 1 anomalia(s) detectada(s) no NDVI em: 2024-01-03"

        mock_climate_df = pd.DataFrame({
            "date": ["2024-01-01", "2024-01-02"],
            "precipitation": [5.0, 3.5],
            "temperature": [25.0, 26.5],
        })
        mock_fetch_climate.return_value = mock_climate_df
        mock_climate_plot.return_value = go.Figure()

        result = run_analysis(mock_geometry, "2024-01-01", "2024-01-31", "NDVI")

        assert result["success"] is True
        assert result["mean_value"] == 0.65
        assert result["alert"] is not None
        assert "ALERTA" in result["alert"]

    @patch("src.app.pipeline.ee")
    @patch("src.app.pipeline.get_image_collection")
    @patch("src.app.pipeline.mask_clouds")
    @patch("src.app.pipeline.compute_time_series")
    @patch("src.app.pipeline.plot_time_series")
    @patch("src.app.pipeline.detect_anomalies")
    @patch("src.app.pipeline.generate_alert")
    @patch("src.app.pipeline.fetch_climate_data")
    @patch("src.app.pipeline.plot_climate_data")
    def test_run_analysis_area_hectares(
        self,
        mock_climate_plot,
        mock_fetch_climate,
        mock_generate_alert,
        mock_detect_anomalies,
        mock_plot_ts,
        mock_compute_ts,
        mock_mask_clouds,
        mock_get_col,
        mock_ee
    ):
        mock_geometry = MagicMock()
        mock_geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-45.0, -20.0]
        mock_geometry.area.return_value.divide.return_value.getInfo.return_value = 100.0

        mock_collection = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 5
        mock_get_col.return_value = mock_collection
        mock_mask_clouds.return_value = mock_collection

        mock_ts_data = [{"date": "2024-01-01", "value": 0.5}]
        mock_compute_ts.return_value = mock_ts_data
        mock_plot_ts.return_value = go.Figure()
        mock_detect_anomalies.return_value = mock_ts_data
        mock_generate_alert.return_value = None
        mock_fetch_climate.return_value = pd.DataFrame()
        mock_climate_plot.return_value = None

        mock_index_map = MagicMock()
        mock_collection.map.return_value.median.return_value = mock_index_map
        mock_index_map.select.return_value.reduceRegion.return_value.getInfo.return_value = {"NDVI": 0.65}

        result = run_analysis(mock_geometry, "2024-01-01", "2024-01-31", "NDVI")

        assert result["success"] is True
        assert result["area_ha"] == 100.0
