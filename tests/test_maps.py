import pytest
from unittest.mock import MagicMock, patch

from src.app.maps import (
    create_base_map,
    add_index_layer,
    add_colorbar,
    enable_area_draw,
    get_drawn_geometry,
    geojson_to_ee_geometry,
    DEFAULT_CENTER,
    DEFAULT_ZOOM,
    NDVI_PALETTE,
    NDWI_PALETTE,
    NDMI_PALETTE,
)


class TestCreateBaseMap:
    @patch("src.app.maps.geemap")
    def test_create_base_map_with_custom_center_and_zoom(self, mock_geemap):
        mock_map = MagicMock()
        mock_geemap.Map.return_value = mock_map

        result = create_base_map(center=[-20.0, -45.0], zoom=12)

        mock_geemap.Map.assert_called_once_with(center=[-20.0, -45.0], zoom=12)
        mock_map.add_layer_control.assert_called_once()
        assert result == mock_map
        assert result == mock_map

    @patch("src.app.maps.geemap")
    def test_create_base_map_with_default_center(self, mock_geemap):
        mock_map = MagicMock()
        mock_geemap.Map.return_value = mock_map

        result = create_base_map()

        mock_geemap.Map.assert_called_once_with(center=DEFAULT_CENTER, zoom=DEFAULT_ZOOM)
        assert result == mock_map

    @patch("src.app.maps.geemap")
    def test_create_base_map_with_none_center_uses_default(self, mock_geemap):
        mock_map = MagicMock()
        mock_geemap.Map.return_value = mock_map

        result = create_base_map(center=None, zoom=DEFAULT_ZOOM)

        mock_geemap.Map.assert_called_once_with(center=DEFAULT_CENTER, zoom=DEFAULT_ZOOM)
        assert result == mock_map

    def test_create_base_map_invalid_zoom_too_low(self):
        with pytest.raises(ValueError, match="zoom deve ser inteiro entre 1 e 20"):
            create_base_map(center=[0, 0], zoom=0)

    def test_create_base_map_invalid_zoom_too_high(self):
        with pytest.raises(ValueError, match="zoom deve ser inteiro entre 1 e 20"):
            create_base_map(center=[0, 0], zoom=21)

    def test_create_base_map_invalid_zoom_float(self):
        with pytest.raises(ValueError, match="zoom deve ser inteiro entre 1 e 20"):
            create_base_map(center=[0, 0], zoom=10.5)


class TestAddIndexLayer:
    @patch("src.app.maps.ee")
    @patch("src.app.maps.geemap")
    def test_add_index_layer_ndvi_default_palette(self, mock_geemap, mock_ee):
        mock_map = MagicMock()
        mock_image = MagicMock()
        mock_band_names = MagicMock()
        mock_contains = MagicMock()
        mock_contains.getInfo.return_value = True
        mock_band_names.contains.return_value = mock_contains
        mock_image.bandNames.return_value = mock_band_names

        result = add_index_layer(mock_map, mock_image, "NDVI")

        mock_map.addLayer.assert_called_once()
        call_args = mock_map.addLayer.call_args
        vis_params = call_args[0][1]
        assert vis_params["min"] == -1
        assert vis_params["max"] == 1
        assert vis_params["palette"] == NDVI_PALETTE
        assert vis_params["opacity"] == 0.7
        assert call_args[0][2] == "NDVI"
        assert result == mock_map

    @patch("src.app.maps.ee")
    @patch("src.app.maps.geemap")
    def test_add_index_layer_ndwi_default_palette(self, mock_geemap, mock_ee):
        mock_map = MagicMock()
        mock_image = MagicMock()
        mock_band_names = MagicMock()
        mock_contains = MagicMock()
        mock_contains.getInfo.return_value = True
        mock_band_names.contains.return_value = mock_contains
        mock_image.bandNames.return_value = mock_band_names

        result = add_index_layer(mock_map, mock_image, "NDWI")

        mock_map.addLayer.assert_called_once()
        call_args = mock_map.addLayer.call_args
        vis_params = call_args[0][1]
        assert vis_params["palette"] == NDWI_PALETTE
        assert call_args[0][2] == "NDWI"

    @patch("src.app.maps.ee")
    @patch("src.app.maps.geemap")
    def test_add_index_layer_ndmi_default_palette(self, mock_geemap, mock_ee):
        mock_map = MagicMock()
        mock_image = MagicMock()
        mock_band_names = MagicMock()
        mock_contains = MagicMock()
        mock_contains.getInfo.return_value = True
        mock_band_names.contains.return_value = mock_contains
        mock_image.bandNames.return_value = mock_band_names

        result = add_index_layer(mock_map, mock_image, "NDMI")

        mock_map.addLayer.assert_called_once()
        call_args = mock_map.addLayer.call_args
        vis_params = call_args[0][1]
        assert vis_params["palette"] == NDMI_PALETTE
        assert call_args[0][2] == "NDMI"

    @patch("src.app.maps.ee")
    @patch("src.app.maps.geemap")
    def test_add_index_layer_custom_palette(self, mock_geemap, mock_ee):
        mock_map = MagicMock()
        mock_image = MagicMock()
        mock_band_names = MagicMock()
        mock_contains = MagicMock()
        mock_contains.getInfo.return_value = True
        mock_band_names.contains.return_value = mock_contains
        mock_image.bandNames.return_value = mock_band_names
        custom_palette = ["red", "yellow", "green"]

        result = add_index_layer(mock_map, mock_image, "NDVI", palette=custom_palette)

        call_args = mock_map.addLayer.call_args
        vis_params = call_args[0][1]
        assert vis_params["palette"] == custom_palette

    @patch("src.app.maps.ee")
    @patch("src.app.maps.geemap")
    def test_add_index_layer_custom_opacity(self, mock_geemap, mock_ee):
        mock_map = MagicMock()
        mock_image = MagicMock()
        mock_band_names = MagicMock()
        mock_contains = MagicMock()
        mock_contains.getInfo.return_value = True
        mock_band_names.contains.return_value = mock_contains
        mock_image.bandNames.return_value = mock_band_names

        add_index_layer(mock_map, mock_image, "NDVI", opacity=0.5)

        call_args = mock_map.addLayer.call_args
        vis_params = call_args[0][1]
        assert vis_params["opacity"] == 0.5

    @patch("src.app.maps.ee")
    def test_add_index_layer_missing_band_raises_error(self, mock_ee):
        mock_map = MagicMock()
        mock_image = MagicMock()
        mock_band_names = MagicMock()
        mock_contains = MagicMock()
        mock_contains.getInfo.return_value = False
        mock_band_names.contains.return_value = mock_contains
        mock_image.bandNames.return_value = mock_band_names

        with pytest.raises(ValueError, match="Imagem não contém banda NDVI"):
            add_index_layer(mock_map, mock_image, "NDVI")

    @patch("src.app.maps.ee")
    def test_add_index_layer_unknown_index_raises_error(self, mock_ee):
        mock_map = MagicMock()
        mock_image = MagicMock()

        with pytest.raises(ValueError, match="Índice desconhecido: INVALID"):
            add_index_layer(mock_map, mock_image, "INVALID")


class TestAddColorbar:
    @patch("src.app.maps.geemap")
    def test_add_colorbar_calls_add_colorbar(self, mock_geemap):
        mock_map = MagicMock()
        palette = ["blue", "white", "green"]

        add_colorbar(mock_map, palette, "NDVI")

        mock_map.add_colorbar.assert_called_once()
        call_kwargs = mock_map.add_colorbar.call_args[1]
        assert call_kwargs["vis_params"]["min"] == -1
        assert call_kwargs["vis_params"]["max"] == 1
        assert call_kwargs["vis_params"]["palette"] == palette
        assert call_kwargs["label"] == "NDVI"
        assert call_kwargs["position"] == "bottomright"

    @patch("src.app.maps.geemap")
    def test_add_colorbar_custom_min_max(self, mock_geemap):
        mock_map = MagicMock()
        palette = ["blue", "white", "green"]

        add_colorbar(mock_map, palette, "NDVI", min_val=-0.5, max_val=0.5)

        call_kwargs = mock_map.add_colorbar.call_args[1]
        assert call_kwargs["vis_params"]["min"] == -0.5
        assert call_kwargs["vis_params"]["max"] == 0.5


class TestEnableAreaDraw:
    @patch("src.app.maps.geemap")
    def test_enable_area_draw_polygon(self, mock_geemap):
        mock_map = MagicMock()
        mock_draw_control = MagicMock()
        mock_map.draw_control = mock_draw_control

        enable_area_draw(mock_map)

        mock_map.add_draw_control_lite.assert_called_once()

class TestGeojsonToEeGeometry:
    @patch("src.app.maps.ee")
    def test_converts_polygon(self, mock_ee):
        geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[-52.1, -28.0], [-52.0, -28.0],
                                  [-52.0, -28.1], [-52.1, -28.0]]],
            },
        }

        geojson_to_ee_geometry(geojson)

        mock_ee.Geometry.Polygon.assert_called_once_with(
            geojson["geometry"]["coordinates"]
        )

    def test_rejects_non_polygon(self):
        with pytest.raises(ValueError, match="usando um polígono"):
            geojson_to_ee_geometry({"type": "Point", "coordinates": [-52, -28]})


class TestGetDrawnGeometry:
    @patch("src.app.maps.ee")
    def test_get_drawn_geometry_returns_geometry(self, mock_ee):
        mock_map = MagicMock()
        mock_feature = MagicMock()
        mock_geometry = MagicMock()
        mock_feature.geometry.return_value = mock_geometry
        mock_map.draw_last_feature = mock_feature
        mock_ee.Geometry.return_value = "ee_geometry"

        result = get_drawn_geometry(mock_map)

        mock_ee.Geometry.assert_called_once_with(mock_geometry)
        assert result == "ee_geometry"

    def test_get_drawn_geometry_no_draw_returns_none(self):
        mock_map = MagicMock()
        mock_map.draw_last_feature = None

        result = get_drawn_geometry(mock_map)

        assert result is None

    def test_get_drawn_geometry_missing_attribute_returns_none(self):
        mock_map = MagicMock()
        del mock_map.draw_last_feature

        result = get_drawn_geometry(mock_map)

        assert result is None

    @patch("src.app.maps.ee")
    def test_get_drawn_geometry_exception_returns_none(self, mock_ee):
        mock_map = MagicMock()
        mock_feature = MagicMock()
        mock_feature.geometry.side_effect = Exception("Error")
        mock_map.draw_last_feature = mock_feature

        result = get_drawn_geometry(mock_map)

        assert result is None
