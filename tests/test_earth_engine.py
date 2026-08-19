import pytest
from unittest.mock import MagicMock, patch
from src.app.earth_engine import (
    filter_by_date,
    filter_by_area,
    get_image_collection,
    mask_clouds,
    calculate_ndvi,
    calculate_ndwi,
    calculate_ndmi,
)


class TestFilterByDate:
    @patch("src.app.earth_engine.ee")
    def test_filter_by_date_valid(self, mock_ee):
        mock_collection = MagicMock()
        mock_filtered = MagicMock()
        mock_collection.filter.return_value = mock_filtered
        mock_ee.Filter.date.return_value = "date_filter"

        result = filter_by_date(mock_collection, "2026-01-01", "2026-01-31")

        mock_ee.Filter.date.assert_called_once_with("2026-01-01", "2026-01-31")
        mock_collection.filter.assert_called_once_with("date_filter")
        assert result == mock_filtered

    def test_filter_by_date_invalid_format_start(self):
        mock_collection = MagicMock()
        with pytest.raises(ValueError, match="Data inválida: 2026/01/01"):
            filter_by_date(mock_collection, "2026/01/01", "2026-01-31")

    def test_filter_by_date_invalid_format_end(self):
        mock_collection = MagicMock()
        with pytest.raises(ValueError, match="Data inválida: 31-01-2026"):
            filter_by_date(mock_collection, "2026-01-01", "31-01-2026")

    def test_filter_by_date_start_after_end(self):
        mock_collection = MagicMock()
        with pytest.raises(ValueError, match="start_date deve ser menor ou igual a end_date"):
            filter_by_date(mock_collection, "2026-01-31", "2026-01-01")

    @patch("src.app.earth_engine.ee")
    def test_filter_by_date_equal_dates(self, mock_ee):
        mock_collection = MagicMock()
        mock_filtered = MagicMock()
        mock_collection.filter.return_value = mock_filtered
        mock_ee.Filter.date.return_value = "date_filter"
        result = filter_by_date(mock_collection, "2026-01-15", "2026-01-15")
        assert result == mock_filtered


class TestFilterByArea:
    @patch("src.app.earth_engine.ee")
    def test_filter_by_area_valid(self, mock_ee):
        mock_collection = MagicMock()
        mock_filtered = MagicMock()
        mock_collection.filter.return_value = mock_filtered
        mock_geometry = MagicMock()
        mock_ee.Filter.bounds.return_value = "bounds_filter"

        result = filter_by_area(mock_collection, mock_geometry)

        mock_ee.Filter.bounds.assert_called_once_with(mock_geometry)
        mock_collection.filter.assert_called_once_with("bounds_filter")
        assert result == mock_filtered

    def test_filter_by_area_none_geometry(self):
        mock_collection = MagicMock()
        with pytest.raises(ValueError, match="geometry não pode ser None"):
            filter_by_area(mock_collection, None)


class TestGetImageCollection:
    @patch("src.app.earth_engine.ee")
    def test_get_image_collection_valid_inputs(self, mock_ee):
        mock_geometry = MagicMock()
        mock_collection = MagicMock()
        mock_filtered = MagicMock()
        mock_selected = MagicMock()

        mock_ee.ImageCollection.return_value = mock_collection
        mock_collection.filter.return_value = mock_filtered
        mock_filtered.filter.return_value = mock_filtered
        mock_filtered.select.return_value = mock_selected

        result = get_image_collection(mock_geometry, "2026-01-01", "2026-01-31", 20)

        mock_ee.ImageCollection.assert_called_once_with("COPERNICUS/S2_SR_HARMONIZED")
        mock_filtered.select.assert_called_once_with(["B2", "B3", "B4", "B8", "QA60"])
        assert result == mock_selected

    @patch("src.app.earth_engine.ee")
    def test_get_image_collection_default_cloud_cover(self, mock_ee):
        mock_geometry = MagicMock()
        mock_collection = MagicMock()
        mock_filtered = MagicMock()
        mock_collection.filter.return_value = mock_filtered
        mock_filtered.select.return_value = MagicMock()

        mock_ee.ImageCollection.return_value = mock_collection

        get_image_collection(mock_geometry, "2026-01-01", "2026-01-31")

        mock_ee.Filter.lt.assert_called_with("CLOUD_COVERAGE_ASSESSMENT", 20)

    @patch("src.app.earth_engine.ee")
    def test_get_image_collection_cloud_cover_zero(self, mock_ee):
        mock_geometry = MagicMock()
        mock_collection = MagicMock()
        mock_filtered = MagicMock()
        mock_collection.filter.return_value = mock_filtered
        mock_filtered.select.return_value = MagicMock()

        mock_ee.ImageCollection.return_value = mock_collection

        get_image_collection(mock_geometry, "2026-01-01", "2026-01-31", 0)

        mock_ee.Filter.lt.assert_called_with("CLOUD_COVERAGE_ASSESSMENT", 0)

    @patch("src.app.earth_engine.ee")
    def test_get_image_collection_cloud_cover_max(self, mock_ee):
        mock_geometry = MagicMock()
        mock_collection = MagicMock()
        mock_filtered = MagicMock()
        mock_collection.filter.return_value = mock_filtered
        mock_filtered.select.return_value = MagicMock()

        mock_ee.ImageCollection.return_value = mock_collection

        get_image_collection(mock_geometry, "2026-01-01", "2026-01-31", 100)

        mock_ee.Filter.lt.assert_called_with("CLOUD_COVERAGE_ASSESSMENT", 100)

    def test_get_image_collection_invalid_date_format(self):
        mock_geometry = MagicMock()
        with pytest.raises(ValueError, match="Data inválida"):
            get_image_collection(mock_geometry, "2026/01/01", "2026-01-31")

    def test_get_image_collection_start_after_end(self):
        mock_geometry = MagicMock()
        with pytest.raises(ValueError, match="start_date deve ser menor ou igual a end_date"):
            get_image_collection(mock_geometry, "2026-01-31", "2026-01-01")

    def test_get_image_collection_none_geometry(self):
        with pytest.raises(ValueError, match="geometry não pode ser None"):
            get_image_collection(None, "2026-01-01", "2026-01-31")

    def test_get_image_collection_invalid_cloud_cover_negative(self):
        mock_geometry = MagicMock()
        with pytest.raises(ValueError, match="cloud_cover_max deve ser inteiro entre 0 e 100"):
            get_image_collection(mock_geometry, "2026-01-01", "2026-01-31", -1)

    def test_get_image_collection_invalid_cloud_cover_over_100(self):
        mock_geometry = MagicMock()
        with pytest.raises(ValueError, match="cloud_cover_max deve ser inteiro entre 0 e 100"):
            get_image_collection(mock_geometry, "2026-01-01", "2026-01-31", 101)

    def test_get_image_collection_invalid_cloud_cover_float(self):
        mock_geometry = MagicMock()
        with pytest.raises(ValueError, match="cloud_cover_max deve ser inteiro entre 0 e 100"):
            get_image_collection(mock_geometry, "2026-01-01", "2026-01-31", 20.5)


class TestMaskClouds:
    @patch("src.app.earth_engine.ee")
    def test_mask_clouds_applies_mask(self, mock_ee):
        mock_image = MagicMock()
        mock_qa60 = MagicMock()
        mock_cloud_mask = MagicMock()
        mock_cirrus_mask = MagicMock()
        mock_combined_mask = MagicMock()
        mock_masked_image = MagicMock()

        mock_image.select.return_value = mock_qa60
        mock_qa60.bitwiseAnd.side_effect = [mock_cloud_mask, mock_cirrus_mask]
        mock_cloud_mask.eq.return_value = mock_cloud_mask
        mock_cirrus_mask.eq.return_value = mock_cirrus_mask
        mock_cloud_mask.And.return_value = mock_combined_mask
        mock_image.updateMask.return_value = mock_masked_image

        result = mask_clouds(mock_image)

        mock_image.select.assert_called_once_with("QA60")
        assert mock_qa60.bitwiseAnd.call_count == 2
        mock_qa60.bitwiseAnd.assert_any_call(1 << 10)
        mock_qa60.bitwiseAnd.assert_any_call(1 << 11)
        mock_cloud_mask.eq.assert_called_once_with(0)
        mock_cirrus_mask.eq.assert_called_once_with(0)
        mock_cloud_mask.And.assert_called_once_with(mock_cirrus_mask)
        mock_image.updateMask.assert_called_once_with(mock_combined_mask)
        assert result == mock_masked_image


class TestCalculateNDVI:
    @patch("src.app.earth_engine.ee")
    def test_calculate_ndvi_returns_band_ndvi(self, mock_ee):
        mock_image = MagicMock()
        mock_ndvi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndvi
        mock_ndvi.rename.return_value = mock_ndvi

        result = calculate_ndvi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8", "B4"])
        mock_ndvi.rename.assert_called_once_with("NDVI")
        assert result == mock_ndvi

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndvi_nir_greater_red(self, mock_ee):
        mock_image = MagicMock()
        mock_ndvi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndvi
        mock_ndvi.rename.return_value = mock_ndvi

        calculate_ndvi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8", "B4"])

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndvi_nir_equal_red(self, mock_ee):
        mock_image = MagicMock()
        mock_ndvi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndvi
        mock_ndvi.rename.return_value = mock_ndvi

        calculate_ndvi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8", "B4"])

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndvi_nir_less_red(self, mock_ee):
        mock_image = MagicMock()
        mock_ndvi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndvi
        mock_ndvi.rename.return_value = mock_ndvi

        calculate_ndvi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8", "B4"])

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndvi_map_on_collection(self, mock_ee):
        mock_collection = MagicMock()
        mock_mapped = MagicMock()
        mock_collection.map.return_value = mock_mapped

        result = mock_collection.map(calculate_ndvi)

        mock_collection.map.assert_called_once_with(calculate_ndvi)
        assert result == mock_mapped

    def test_calculate_ndvi_missing_bands_raises_error(self):
        mock_image = MagicMock()
        mock_image.normalizedDifference.side_effect = Exception("Band not found")

        with pytest.raises(Exception):
            calculate_ndvi(mock_image)


class TestCalculateNDWI:
    @patch("src.app.earth_engine.ee")
    def test_calculate_ndwi_returns_band_ndwi(self, mock_ee):
        mock_image = MagicMock()
        mock_ndwi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndwi
        mock_ndwi.rename.return_value = mock_ndwi

        result = calculate_ndwi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8", "B11"])
        mock_ndwi.rename.assert_called_once_with("NDWI")
        assert result == mock_ndwi

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndwi_nir_greater_swir(self, mock_ee):
        mock_image = MagicMock()
        mock_ndwi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndwi
        mock_ndwi.rename.return_value = mock_ndwi

        calculate_ndwi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8", "B11"])

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndwi_nir_equal_swir(self, mock_ee):
        mock_image = MagicMock()
        mock_ndwi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndwi
        mock_ndwi.rename.return_value = mock_ndwi

        calculate_ndwi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8", "B11"])

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndwi_nir_less_swir(self, mock_ee):
        mock_image = MagicMock()
        mock_ndwi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndwi
        mock_ndwi.rename.return_value = mock_ndwi

        calculate_ndwi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8", "B11"])

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndwi_map_on_collection(self, mock_ee):
        mock_collection = MagicMock()
        mock_mapped = MagicMock()
        mock_collection.map.return_value = mock_mapped

        result = mock_collection.map(calculate_ndwi)

        mock_collection.map.assert_called_once_with(calculate_ndwi)
        assert result == mock_mapped

    def test_calculate_ndwi_missing_bands_raises_error(self):
        mock_image = MagicMock()
        mock_image.normalizedDifference.side_effect = Exception("Band not found")

        with pytest.raises(Exception):
            calculate_ndwi(mock_image)


class TestCalculateNDMI:
    @patch("src.app.earth_engine.ee")
    def test_calculate_ndmi_returns_band_ndmi(self, mock_ee):
        mock_image = MagicMock()
        mock_ndmi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndmi
        mock_ndmi.rename.return_value = mock_ndmi

        result = calculate_ndmi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8A", "B11"])
        mock_ndmi.rename.assert_called_once_with("NDMI")
        assert result == mock_ndmi

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndmi_nir_greater_swir(self, mock_ee):
        mock_image = MagicMock()
        mock_ndmi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndmi
        mock_ndmi.rename.return_value = mock_ndmi

        calculate_ndmi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8A", "B11"])

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndmi_nir_equal_swir(self, mock_ee):
        mock_image = MagicMock()
        mock_ndmi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndmi
        mock_ndmi.rename.return_value = mock_ndmi

        calculate_ndmi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8A", "B11"])

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndmi_nir_less_swir(self, mock_ee):
        mock_image = MagicMock()
        mock_ndmi = MagicMock()
        mock_image.normalizedDifference.return_value = mock_ndmi
        mock_ndmi.rename.return_value = mock_ndmi

        calculate_ndmi(mock_image)

        mock_image.normalizedDifference.assert_called_once_with(["B8A", "B11"])

    @patch("src.app.earth_engine.ee")
    def test_calculate_ndmi_map_on_collection(self, mock_ee):
        mock_collection = MagicMock()
        mock_mapped = MagicMock()
        mock_collection.map.return_value = mock_mapped

        result = mock_collection.map(calculate_ndmi)

        mock_collection.map.assert_called_once_with(calculate_ndmi)
        assert result == mock_mapped

    def test_calculate_ndmi_missing_bands_raises_error(self):
        mock_image = MagicMock()
        mock_image.normalizedDifference.side_effect = Exception("Band not found")

        with pytest.raises(Exception):
            calculate_ndmi(mock_image)