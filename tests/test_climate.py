import pytest
from unittest.mock import MagicMock, patch
import pandas as pd

from src.app.climate import (
    fetch_climate_data,
    plot_climate_data,
    DEFAULT_PARAMETERS,
)


class MockGeometry:
    def __init__(self, coords=None):
        self._coords = coords

    def centroid(self):
        return MockCentroid(self._coords)

    def coordinates(self):
        return MockCoordinates(self._coords)


class MockCentroid:
    def __init__(self, coords):
        self._coords = coords

    def coordinates(self):
        return MockCoordinates(self._coords)

    def getInfo(self):
        return self._coords


class MockCoordinates:
    def __init__(self, coords):
        self._coords = coords

    def getInfo(self):
        return self._coords


def make_mock_response(data):
    mock_response = MagicMock()
    mock_response.json.return_value = data
    mock_response.raise_for_status.return_value = None
    return mock_response


class TestFetchClimateData:
    def test_fetch_climate_data_success(self):
        geometry = MockGeometry(coords=[-45.0, -20.0])

        api_response = {
            "properties": {
                "parameter": {
                    "PRECTOTCORR": {
                        "2024-01-01": 5.0,
                        "2024-01-02": -999,
                        "2024-01-03": 3.5,
                    },
                    "T2M": {
                        "2024-01-01": 25.0,
                        "2024-01-02": 26.5,
                        "2024-01-03": -999,
                    },
                    "ALLSKY_SFC_SW_DWN": {
                        "2024-01-01": 6.0,
                        "2024-01-02": 5.5,
                        "2024-01-03": 7.0,
                    },
                }
            }
        }

        with patch("src.app.climate.requests.get") as mock_get:
            mock_get.return_value = make_mock_response(api_response)

            result = fetch_climate_data(geometry, "2024-01-01", "2024-01-03")

        assert isinstance(result, pd.DataFrame)
        assert "date" in result.columns
        assert "precipitation" in result.columns
        assert "temperature" in result.columns
        assert "solar_radiation" in result.columns
        assert len(result) == 3
        assert result.iloc[0]["precipitation"] == 5.0
        assert pd.isna(result.iloc[1]["precipitation"])
        assert result.iloc[2]["precipitation"] == 3.5
        assert pd.isna(result.iloc[2]["temperature"])

    def test_fetch_climate_data_custom_parameters(self):
        geometry = MockGeometry(coords=[-45.0, -20.0])

        api_response = {
            "properties": {
                "parameter": {
                    "T2M_MAX": {
                        "2024-01-01": 30.0,
                        "2024-01-02": 31.0,
                    },
                    "T2M_MIN": {
                        "2024-01-01": 20.0,
                        "2024-01-02": 21.0,
                    },
                }
            }
        }

        with patch("src.app.climate.requests.get") as mock_get:
            mock_get.return_value = make_mock_response(api_response)

            result = fetch_climate_data(
                geometry,
                "2024-01-01",
                "2024-01-02",
                parameters=["T2M_MAX", "T2M_MIN"],
            )

        assert isinstance(result, pd.DataFrame)
        assert "temperature_max" in result.columns
        assert "temperature_min" in result.columns
        assert result.iloc[0]["temperature_max"] == 30.0
        assert result.iloc[0]["temperature_min"] == 20.0

        mock_get.assert_called_once_with(
            "https://power.larc.nasa.gov/api/temporal/daily/point",
            params={
                "community": "ag",
                "parameters": "T2M_MAX,T2M_MIN",
                "start": "20240101",
                "end": "20240102",
                "latitude": -20.0,
                "longitude": -45.0,
                "format": "JSON",
            },
            timeout=30,
        )

    def test_fetch_climate_data_with_empty_parameter_data(self):
        geometry = MockGeometry(coords=[-45.0, -20.0])

        with patch("src.app.climate.requests.get") as mock_get:
            mock_get.return_value = make_mock_response({"properties": {}})

            result = fetch_climate_data(
                geometry,
                "2024-01-01",
                "2024-01-03",
                parameters=["UNKNOWN_PARAMETER"],
            )

        assert isinstance(result, pd.DataFrame)
        assert result.empty
        assert list(result.columns) == []

    def test_fetch_climate_data_propagates_http_error(self):
        geometry = MockGeometry(coords=[-45.0, -20.0])
        response = make_mock_response({})
        response.raise_for_status.side_effect = RuntimeError("HTTP Error")

        with patch("src.app.climate.requests.get", return_value=response):
            with pytest.raises(RuntimeError, match="HTTP Error"):
                fetch_climate_data(geometry, "2024-01-01", "2024-01-03")

    def test_fetch_climate_data_invalid_geometry(self):
        geometry = MockGeometry(coords=None)

        with pytest.raises(ValueError, match="Geometry does not have valid coordinates"):
            fetch_climate_data(geometry, "2024-01-01", "2024-01-03")

    def test_fetch_climate_data_api_error(self):
        geometry = MockGeometry(coords=[-45.0, -20.0])

        with patch("src.app.climate.requests.get") as mock_get:
            mock_get.side_effect = Exception("API Error")

            with pytest.raises(Exception, match="API Error"):
                fetch_climate_data(geometry, "2024-01-01", "2024-01-03")


class TestPlotClimateData:
    def test_plot_with_valid_data(self):
        climate_df = pd.DataFrame({
            "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
            "precipitation": [5.0, 3.5, 2.0],
            "temperature": [25.0, 26.5, 27.0],
        })

        fig = plot_climate_data(climate_df)

        assert fig is not None
        assert len(fig.data) == 2
        assert fig.data[0].type == "bar"
        assert fig.data[1].type == "scatter"

    def test_plot_with_empty_dataframe(self):
        climate_df = pd.DataFrame()

        fig = plot_climate_data(climate_df)

        assert fig is not None
        assert len(fig.data) == 0

    def test_plot_with_missing_precipitation(self):
        climate_df = pd.DataFrame({
            "date": ["2024-01-01", "2024-01-02"],
            "temperature": [25.0, 26.5],
        })

        fig = plot_climate_data(climate_df)

        assert fig is not None
        assert len(fig.data) == 1
        assert fig.data[0].type == "scatter"

    def test_plot_with_missing_temperature(self):
        climate_df = pd.DataFrame({
            "date": ["2024-01-01", "2024-01-02"],
            "precipitation": [5.0, 3.5],
        })

        fig = plot_climate_data(climate_df)

        assert fig is not None
        assert len(fig.data) == 1
        assert fig.data[0].type == "bar"
