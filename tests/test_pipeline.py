import pytest
from unittest.mock import MagicMock, patch
import pandas as pd
import plotly.graph_objects as go
from datetime import date

from src.app.pipeline import run_analysis, run_multi_analysis


def geometry_with_centroid():
    geometry = MagicMock()
    geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [
        -45.0, -20.0
    ]
    return geometry


class TestRunAnalysis:
    @patch("src.app.pipeline.compute_time_series", return_value=[])
    @patch("src.app.pipeline.get_image_collection")
    def test_run_analysis_reuses_image_count_and_precomputed_area(
        self, mock_get_collection, mock_compute_time_series
    ):
        geometry = geometry_with_centroid()
        collection = MagicMock()
        collection.size.return_value.getInfo.return_value = 2
        masked_collection = MagicMock()
        index_collection = MagicMock()
        index_image = MagicMock()
        collection.map.return_value = masked_collection
        masked_collection.map.return_value = index_collection
        index_collection.median.return_value = index_image
        index_image.select.return_value.reduceRegion.return_value.getInfo.return_value = {
            "NDVI": 0.5
        }
        mock_get_collection.return_value = collection

        with patch("src.app.pipeline.ee") as mock_ee, patch(
            "src.app.pipeline.fetch_climate_data", return_value=None
        ), patch("src.app.pipeline.plot_climate_data", return_value=None), patch(
            "src.app.pipeline.plot_time_series", return_value=None
        ), patch("src.app.pipeline.detect_anomalies", return_value=[]), patch(
            "src.app.pipeline.generate_alert", return_value=None
        ):
            mock_ee.Reducer.mean.return_value = "mean_reducer"
            result = run_analysis(
                geometry, "2024-01-01", "2024-01-31", "NDVI", area_ha=12.5
            )

        assert result["success"] is True
        assert result["area_ha"] == 12.5
        assert result["map_center"] == [-20.0, -45.0]
        geometry.area.assert_not_called()
        geometry.centroid.return_value.coordinates.return_value.getInfo.assert_called_once_with()
        collection.size.assert_called_once_with()
        mock_compute_time_series.assert_called_once_with(
            index_collection,
            geometry,
            "NDVI",
            scale=10,
            image_count=2,
        )

    @pytest.mark.parametrize(
        "index_name, calculation_name",
        [("NDWI", "calculate_ndwi"), ("NDMI", "calculate_ndmi")],
    )
    @patch("src.app.pipeline.plot_climate_data")
    @patch("src.app.pipeline.fetch_climate_data")
    @patch("src.app.pipeline.generate_alert")
    @patch("src.app.pipeline.detect_anomalies")
    @patch("src.app.pipeline.plot_time_series")
    @patch("src.app.pipeline.compute_time_series")
    @patch("src.app.pipeline.mask_clouds")
    @patch("src.app.pipeline.get_image_collection")
    @patch("src.app.pipeline.ee")
    def test_run_analysis_supported_non_ndvi_indices(
        self,
        mock_ee,
        mock_get_col,
        mock_mask_clouds,
        mock_compute_ts,
        mock_plot_ts,
        mock_detect_anomalies,
        mock_generate_alert,
        mock_fetch_climate,
        mock_climate_plot,
        index_name,
        calculation_name,
    ):
        geometry = geometry_with_centroid()
        geometry.area.return_value.divide.return_value.getInfo.return_value = 25.0

        collection = MagicMock()
        collection.size.return_value.getInfo.return_value = 1
        masked_collection = MagicMock()
        index_collection = MagicMock()
        index_image = MagicMock()
        collection.map.return_value = masked_collection
        masked_collection.map.return_value = index_collection
        index_collection.median.return_value = index_image
        index_image.select.return_value.reduceRegion.return_value.getInfo.return_value = {
            index_name: 0.4
        }
        mock_get_col.return_value = collection
        mock_compute_ts.return_value = []
        mock_detect_anomalies.return_value = []
        mock_generate_alert.return_value = None
        mock_fetch_climate.return_value = pd.DataFrame()
        mock_ee.Reducer.mean.return_value = "mean_reducer"

        with patch(f"src.app.pipeline.{calculation_name}") as mock_calculation:
            result = run_analysis(
                geometry, date(2024, 1, 1), date(2024, 1, 31), index_name
            )

        assert result["success"] is True
        assert result["index_name"] == index_name
        assert result["mean_value"] == 0.4
        assert result["time_series"] == []
        assert result["time_series_plot"] is None
        assert result["climate_plot"] is None
        masked_collection.map.assert_called_once_with(mock_calculation)
        mock_get_col.assert_called_once_with(geometry, "2024-01-01", "2024-01-31")
        mock_fetch_climate.assert_called_once_with(
            geometry,
            "2024-01-01",
            "2024-01-31",
            coordinates=(-45.0, -20.0),
        )

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
        mock_geometry = geometry_with_centroid()
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
        assert result["index_name"] == "NDVI"
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
    def test_run_analysis_no_images(self, mock_get_col, mock_ee, caplog):
        mock_geometry = MagicMock()

        mock_collection = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 0
        mock_get_col.return_value = mock_collection

        result = run_analysis(mock_geometry, "2024-01-01", "2024-01-31", "NDVI")

        assert result["success"] is False
        assert "error" in result
        assert "Nenhuma imagem encontrada" in result["error"]
        assert not [record for record in caplog.records if record.exc_info]

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
    def test_run_analysis_exception_handling(self, mock_get_col, caplog):
        mock_geometry = MagicMock()

        mock_get_col.side_effect = Exception("Connection error")

        result = run_analysis(mock_geometry, "2024-01-01", "2024-01-31", "NDVI")

        assert result["success"] is False
        assert "error" in result
        assert "Connection error" in result["error"]
        record = next(
            record for record in caplog.records
            if record.name == "src.app.pipeline"
        )
        assert record.getMessage() == "Single-index analysis failed"
        assert record.index_name == "NDVI"
        assert record.exc_info is not None

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
        mock_ee,
        caplog,
    ):
        mock_geometry = geometry_with_centroid()
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

        with caplog.at_level("WARNING", logger="src.app.pipeline"):
            result = run_analysis(mock_geometry, "2024-01-01", "2024-01-31", "NDVI")

        assert result["success"] is True
        assert result["climate_data"] is None
        assert result["climate_plot"] is None
        climate_record = next(
            record for record in caplog.records
            if record.getMessage() == "Climate data unavailable during single-index analysis"
        )
        assert climate_record.exc_info is not None

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
        mock_geometry = geometry_with_centroid()
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
        mock_geometry = geometry_with_centroid()
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


class TestRunMultiAnalysis:
    def test_run_multi_analysis_reuses_shared_inputs_for_selected_indices(self):
        from contextlib import ExitStack

        with ExitStack() as stack:
            patch_names = (
                "get_image_collection",
                "mask_clouds",
                "calculate_ndvi",
                "calculate_ndwi",
                "calculate_ndmi",
                "compute_time_series",
                "fetch_climate_data",
                "plot_climate_data",
                "ee",
            )
            mocks = {
                name: stack.enter_context(patch(f"src.app.pipeline.{name}"))
                for name in patch_names
            }

            geometry = geometry_with_centroid()
            geometry.area.return_value.divide.return_value.getInfo.return_value = 42.5
            collection = MagicMock()
            collection.size.return_value.getInfo.return_value = 7
            mocks["get_image_collection"].return_value = collection
            masked_collection = MagicMock()
            collection.map.return_value = masked_collection
            index_collections = [MagicMock(), MagicMock(), MagicMock()]
            masked_collection.map.side_effect = index_collections

            for index_name, index_collection, mean_value in zip(
                ("NDVI", "NDWI", "NDMI"), index_collections, (0.6, 0.2, 0.4)
            ):
                index_map = MagicMock()
                index_collection.median.return_value = index_map
                index_map.select.return_value.reduceRegion.return_value.getInfo.return_value = {
                    index_name: mean_value
                }

            time_series = [
                {"date": "2024-01-01", "value": 0.2},
                {"date": "2024-01-02", "value": 0.4},
            ]
            mocks["compute_time_series"].return_value = time_series
            climate_data = pd.DataFrame(
                {"date": ["2024-01-01"], "precipitation": [2.0], "temperature": [22.0]}
            )
            mocks["fetch_climate_data"].return_value = climate_data
            mocks["ee"].Reducer.mean.return_value = "mean_reducer"

            result = run_multi_analysis(
                geometry,
                date(2024, 1, 1),
                date(2024, 1, 31),
                ["NDVI", "NDWI", "NDMI", "NDVI"],
                area_ha=42.5,
            )

        assert result["success"] is True
        assert list(result["indices"]) == ["NDVI", "NDWI", "NDMI"]
        assert result["area_ha"] == 42.5
        assert result["image_count"] == 7
        assert result["climate_data"] is climate_data
        assert result["climate_plot"] is not None
        assert result["map_center"] == [-20.0, -45.0]
        assert result["indices"]["NDVI"]["mean_value"] == 0.6
        assert result["indices"]["NDVI"]["trend"] == "crescente"
        assert result["indices"]["NDVI"]["time_series"] == time_series
        mocks["get_image_collection"].assert_called_once_with(
            geometry, "2024-01-01", "2024-01-31"
        )
        collection.map.assert_called_once_with(mocks["mask_clouds"])
        assert masked_collection.map.call_count == 3
        geometry.area.assert_not_called()
        geometry.centroid.return_value.coordinates.return_value.getInfo.assert_called_once_with()
        mocks["fetch_climate_data"].assert_called_once_with(
            geometry,
            "2024-01-01",
            "2024-01-31",
            coordinates=(-45.0, -20.0),
        )
        assert mocks["compute_time_series"].call_count == 3
        assert all(
            call.kwargs["image_count"] == 7
            for call in mocks["compute_time_series"].call_args_list
        )

    @pytest.mark.parametrize("index_names", [[], ["INVALID"], ["NDVI", "INVALID"]])
    def test_run_multi_analysis_rejects_empty_or_unsupported_indices(self, index_names):
        with patch("src.app.pipeline.get_image_collection") as mock_get_collection:
            result = run_multi_analysis(
                MagicMock(), "2024-01-01", "2024-01-31", index_names
            )

        assert result["success"] is False
        assert "error" in result
        mock_get_collection.assert_not_called()

    def test_run_multi_analysis_returns_error_when_no_images_are_found(self):
        collection = MagicMock()
        collection.size.return_value.getInfo.return_value = 0

        with patch(
            "src.app.pipeline.get_image_collection", return_value=collection
        ) as mock_get_collection, patch("src.app.pipeline.mask_clouds") as mock_mask:
            result = run_multi_analysis(
                MagicMock(), "2024-01-01", "2024-01-31", ["NDVI", "NDMI"]
            )

        assert result["success"] is False
        assert "Nenhuma imagem encontrada" in result["error"]
        mock_get_collection.assert_called_once()
        mock_mask.assert_not_called()

    def test_run_multi_analysis_continues_when_climate_fetch_fails(self, caplog):
        collection = MagicMock()
        collection.size.return_value.getInfo.return_value = 1
        masked_collection = MagicMock()
        collection.map.return_value = masked_collection
        index_collection = MagicMock()
        masked_collection.map.return_value = index_collection
        index_map = MagicMock()
        index_collection.median.return_value = index_map
        index_map.select.return_value.reduceRegion.return_value.getInfo.return_value = {
            "NDVI": 0.3
        }
        geometry = geometry_with_centroid()
        geometry.area.return_value.divide.return_value.getInfo.return_value = 1.0

        with patch(
            "src.app.pipeline.get_image_collection", return_value=collection
        ), patch("src.app.pipeline.compute_time_series", return_value=[]), patch(
            "src.app.pipeline.fetch_climate_data", side_effect=RuntimeError("offline")
        ) as mock_fetch_climate, patch("src.app.pipeline.ee") as mock_ee:
            with caplog.at_level("WARNING", logger="src.app.pipeline"):
                result = run_multi_analysis(
                    geometry, "2024-01-01", "2024-01-31", ["NDVI"]
                )

        assert result["success"] is True
        assert result["climate_data"] is None
        assert result["climate_plot"] is None
        assert result["map_center"] == [-20.0, -45.0]
        mock_fetch_climate.assert_called_once()
        mock_ee.Reducer.mean.assert_called_once_with()
        assert any(
            record.getMessage() == "Climate data unavailable during multi-index analysis"
            and record.exc_info is not None
            for record in caplog.records
        )

    def test_run_multi_analysis_returns_error_when_pipeline_fails(self, caplog):
        with patch(
            "src.app.pipeline.get_image_collection",
            side_effect=RuntimeError("Earth Engine unavailable"),
        ):
            with caplog.at_level("ERROR", logger="src.app.pipeline"):
                result = run_multi_analysis(
                    MagicMock(), "2024-01-01", "2024-01-31", ["NDVI"]
                )

        assert result == {
            "success": False,
            "error": "Earth Engine unavailable",
        }
        record = next(
            record for record in caplog.records
            if record.name == "src.app.pipeline"
        )
        assert record.getMessage() == "Multi-index analysis failed"
        assert record.index_names == ("NDVI",)
        assert record.exc_info is not None
