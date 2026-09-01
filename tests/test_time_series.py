import pytest
from unittest.mock import MagicMock, patch

from src.app.time_series import compute_time_series, plot_time_series


class TestComputeTimeSeries:
    @patch("src.app.time_series.ee")
    def test_compute_time_series_reduces_images_with_expected_parameters(self, mock_ee):
        mock_collection = MagicMock()
        mock_geometry = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 2

        first_image = MagicMock(name="first_image")
        first_image.date.return_value.format.return_value = "2026-02-01"
        first_image.reduceRegion.return_value.get.return_value = 0.6
        second_image = MagicMock(name="second_image")
        second_image.date.return_value.format.return_value = "2026-01-01"
        second_image.reduceRegion.return_value.get.return_value = 0.5

        reduced_features = MagicMock()
        reduced_features.size.return_value.getInfo.return_value = 2
        first_feature = MagicMock()
        first_feature.toDictionary.return_value.getInfo.return_value = {
            "date": "2026-02-01",
            "value": 0.6,
        }
        second_feature = MagicMock()
        second_feature.toDictionary.return_value.getInfo.return_value = {
            "date": "2026-01-01",
            "value": 0.5,
        }
        feature_list = MagicMock()
        feature_list.size.return_value.getInfo.return_value = 2
        feature_list.get.side_effect = [first_feature, second_feature]
        reduced_features.toList.return_value = feature_list

        def map_and_execute(callback):
            callback(first_image)
            callback(second_image)
            return reduced_features

        mock_collection.map.side_effect = map_and_execute
        mock_ee.Image.side_effect = lambda image: image
        mock_ee.Feature.side_effect = lambda feature, *_args, **_kwargs: (
            MagicMock() if feature is None else feature
        )
        mock_ee.Reducer.mean.return_value = "mean_reducer"

        result = compute_time_series(mock_collection, mock_geometry, "NDVI", scale=20)

        assert result == [
            {"date": "2026-01-01", "value": 0.5},
            {"date": "2026-02-01", "value": 0.6},
        ]
        first_image.reduceRegion.assert_called_once_with(
            reducer="mean_reducer",
            geometry=mock_geometry,
            scale=20,
            maxPixels=1e9,
        )
        second_image.reduceRegion.assert_called_once_with(
            reducer="mean_reducer",
            geometry=mock_geometry,
            scale=20,
            maxPixels=1e9,
        )
        assert first_image.reduceRegion.return_value.get.call_args.args == ("NDVI",)
        assert second_image.reduceRegion.return_value.get.call_args.args == ("NDVI",)

    @patch("src.app.time_series.ee")
    def test_compute_time_series_with_data(self, mock_ee):
        mock_collection = MagicMock()
        mock_geometry = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 3

        mock_feat1 = MagicMock()
        mock_feat1.toDictionary.return_value.getInfo.return_value = {"date": "2026-01-01", "value": 0.5}
        mock_feat2 = MagicMock()
        mock_feat2.toDictionary.return_value.getInfo.return_value = {"date": "2026-02-01", "value": 0.6}
        mock_feat3 = MagicMock()
        mock_feat3.toDictionary.return_value.getInfo.return_value = {"date": "2026-03-01", "value": 0.7}

        mock_features_list = MagicMock()
        mock_features_list.size.return_value.getInfo.return_value = 3
        mock_features_list.get.side_effect = [mock_feat1, mock_feat2, mock_feat3]

        mock_features = MagicMock()
        mock_features.toList.return_value = mock_features_list
        mock_features.size.return_value.getInfo.return_value = 3
        mock_collection.map.return_value = mock_features

        mock_ee.Feature.side_effect = lambda *args, **kwargs: args[0] if args else MagicMock()
        mock_ee.Image.return_value = MagicMock()
        mock_ee.Reducer.mean.return_value = "mean_reducer"

        result = compute_time_series(mock_collection, mock_geometry, "NDVI")

        assert len(result) == 3
        assert result[0]["date"] == "2026-01-01"
        assert result[0]["value"] == 0.5
        assert result[1]["date"] == "2026-02-01"
        assert result[1]["value"] == 0.6
        assert result[2]["date"] == "2026-03-01"
        assert result[2]["value"] == 0.7

    @patch("src.app.time_series.ee")
    def test_compute_time_series_empty_collection(self, mock_ee):
        mock_collection = MagicMock()
        mock_geometry = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 0

        result = compute_time_series(mock_collection, mock_geometry, "NDVI")

        assert result == []

    @patch("src.app.time_series.ee")
    def test_compute_time_series_removes_none_values(self, mock_ee):
        mock_collection = MagicMock()
        mock_geometry = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 3

        mock_feat1 = MagicMock()
        mock_feat1.toDictionary.return_value.getInfo.return_value = {"date": "2026-01-01", "value": 0.5}
        mock_feat2 = MagicMock()
        mock_feat2.toDictionary.return_value.getInfo.return_value = {"date": "2026-02-01", "value": None}
        mock_feat3 = MagicMock()
        mock_feat3.toDictionary.return_value.getInfo.return_value = {"date": "2026-03-01", "value": 0.7}

        mock_features_list = MagicMock()
        mock_features_list.size.return_value.getInfo.return_value = 3
        mock_features_list.get.side_effect = [mock_feat1, mock_feat2, mock_feat3]

        mock_features = MagicMock()
        mock_features.toList.return_value = mock_features_list
        mock_features.size.return_value.getInfo.return_value = 3
        mock_collection.map.return_value = mock_features

        mock_ee.Feature.side_effect = lambda *args, **kwargs: args[0] if args else MagicMock()
        mock_ee.Image.return_value = MagicMock()
        mock_ee.Reducer.mean.return_value = "mean_reducer"

        result = compute_time_series(mock_collection, mock_geometry, "NDVI")

        assert len(result) == 2
        assert result[0]["date"] == "2026-01-01"
        assert result[1]["date"] == "2026-03-01"

    @patch("src.app.time_series.ee")
    def test_compute_time_series_sorts_by_date(self, mock_ee):
        mock_collection = MagicMock()
        mock_geometry = MagicMock()
        mock_collection.size.return_value.getInfo.return_value = 3

        mock_feat1 = MagicMock()
        mock_feat1.toDictionary.return_value.getInfo.return_value = {"date": "2026-03-01", "value": 0.7}
        mock_feat2 = MagicMock()
        mock_feat2.toDictionary.return_value.getInfo.return_value = {"date": "2026-01-01", "value": 0.5}
        mock_feat3 = MagicMock()
        mock_feat3.toDictionary.return_value.getInfo.return_value = {"date": "2026-02-01", "value": 0.6}

        mock_features_list = MagicMock()
        mock_features_list.size.return_value.getInfo.return_value = 3
        mock_features_list.get.side_effect = [mock_feat1, mock_feat2, mock_feat3]

        mock_features = MagicMock()
        mock_features.toList.return_value = mock_features_list
        mock_features.size.return_value.getInfo.return_value = 3
        mock_collection.map.return_value = mock_features

        mock_ee.Feature.side_effect = lambda *args, **kwargs: args[0] if args else MagicMock()
        mock_ee.Image.return_value = MagicMock()
        mock_ee.Reducer.mean.return_value = "mean_reducer"

        result = compute_time_series(mock_collection, mock_geometry, "NDVI")

        assert result[0]["date"] == "2026-01-01"
        assert result[1]["date"] == "2026-02-01"
        assert result[2]["date"] == "2026-03-01"


class TestPlotTimeSeries:
    def test_plot_time_series_with_data(self):
        data = [
            {"date": "2026-01-01", "value": 0.5},
            {"date": "2026-02-01", "value": 0.6},
            {"date": "2026-03-01", "value": 0.7},
        ]

        fig = plot_time_series(data, "NDVI")

        assert fig is not None
        assert hasattr(fig, 'data')
        assert fig.layout.title.text == "Evolução Temporal de NDVI"
        assert list(fig.layout.yaxis.range) == [-1, 1]

    def test_plot_time_series_empty_data_returns_none(self):
        fig = plot_time_series([], "NDVI")
        assert fig is None

    def test_plot_time_series_ndwi(self):
        data = [
            {"date": "2026-01-01", "value": -0.2},
            {"date": "2026-02-01", "value": 0.1},
        ]

        fig = plot_time_series(data, "NDWI")

        assert fig is not None
        assert fig.layout.title.text == "Evolução Temporal de NDWI"
