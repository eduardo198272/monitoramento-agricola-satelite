import sys
from unittest.mock import MagicMock

import pandas as pd
import pytest

mock_ee = MagicMock()
sys.modules['ee'] = mock_ee

mock_geemap = MagicMock()
sys.modules['geemap'] = mock_geemap


@pytest.fixture
def mock_http_response():
    """Create a deterministic HTTP response without making a network call."""
    def factory(payload=None, status_code=200):
        response = MagicMock()
        response.status_code = status_code
        response.json.return_value = payload if payload is not None else {}
        response.raise_for_status.return_value = None
        return response

    return factory


@pytest.fixture
def mock_ee_geometry():
    """Create an Earth Engine-like geometry with centroid and area methods."""
    def factory(coordinates=(-45.0, -20.0), area_m2=1000000.0):
        geometry = MagicMock()
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = list(coordinates)
        geometry.area.return_value.divide.return_value.getInfo.return_value = area_m2 / 10000
        return geometry

    return factory


@pytest.fixture
def mock_ee_collection():
    """Create a configurable Earth Engine-like image collection."""
    def factory(size=3):
        collection = MagicMock()
        collection.size.return_value.getInfo.return_value = size
        collection.map.return_value = collection
        collection.median.return_value = MagicMock(name='median_image')
        return collection

    return factory


@pytest.fixture
def sample_time_series():
    """Return deterministic index observations for time-series tests."""
    return [
        {'date': '2026-01-01', 'value': 0.5},
        {'date': '2026-02-01', 'value': 0.6},
        {'date': '2026-03-01', 'value': 0.7},
    ]


@pytest.fixture
def sample_dataframe():
    """Return a deterministic DataFrame for processing and presentation tests."""
    return pd.DataFrame({
        'date': ['2026-01-01', '2026-02-01', '2026-03-01'],
        'precipitation': [5.0, 3.5, 2.0],
        'temperature': [25.0, 26.5, 27.0],
    })
