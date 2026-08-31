import pytest
import requests
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
    search_location,
    calculate_map_zoom,
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


class TestSearchLocation:
    @pytest.mark.parametrize("query", ["", "   ", "\t\n"])
    @patch("src.app.maps.requests.get")
    def test_search_location_ignores_empty_query(self, mock_get, query):
        assert search_location(query) is None
        mock_get.assert_not_called()

    @patch("src.app.maps.requests.get")
    def test_search_location_returns_first_result(self, mock_get):
        response = MagicMock()
        response.json.return_value = [{
            "display_name": "Passo Fundo, Rio Grande do Sul, Brasil",
            "lat": "-28.2628",
            "lon": "-52.4068",
            "boundingbox": ["-28.4", "-28.1", "-52.6", "-52.2"],
        }]
        mock_get.return_value = response

        result = search_location("Passo Fundo, RS")

        mock_get.assert_called_once()
        request = mock_get.call_args
        assert request.args[0] == "https://nominatim.openstreetmap.org/search"
        assert request.kwargs["params"] == {
            "q": "Passo Fundo, RS",
            "format": "jsonv2",
            "limit": 1,
        }
        assert "User-Agent" in request.kwargs["headers"]
        assert request.kwargs["timeout"] > 0
        assert result == {
            "display_name": "Passo Fundo, Rio Grande do Sul, Brasil",
            "latitude": -28.2628,
            "longitude": -52.4068,
            "boundingbox": ["-28.4", "-28.1", "-52.6", "-52.2"],
        }

    @patch("src.app.maps.requests.get")
    def test_search_location_normalizes_query(self, mock_get):
        response = MagicMock()
        response.json.return_value = []
        mock_get.return_value = response

        assert search_location("  Passo   Fundo,   RS  ") is None

        request = mock_get.call_args
        assert request.kwargs["params"]["q"] == "Passo Fundo, RS"

    @pytest.mark.parametrize(
        "error",
        [
            requests.exceptions.Timeout(),
            requests.exceptions.ConnectionError(),
            requests.exceptions.HTTPError(),
        ],
    )
    @patch("src.app.maps.requests.get")
    def test_search_location_handles_request_errors(self, mock_get, error):
        mock_get.side_effect = error

        assert search_location("Passo Fundo, RS") is None


    @patch("src.app.maps.requests.get")
    def test_search_location_handles_http_error(self, mock_get):
        response = MagicMock()
        response.raise_for_status.side_effect = requests.exceptions.HTTPError()
        mock_get.return_value = response

        assert search_location("Passo Fundo, RS") is None

    @patch("src.app.maps.requests.get")
    def test_search_location_handles_invalid_json(self, mock_get):
        response = MagicMock()
        response.json.side_effect = ValueError("invalid JSON")
        mock_get.return_value = response

        assert search_location("Passo Fundo, RS") is None

    @pytest.mark.parametrize(
        "payload",
        [{"display_name": "Passo Fundo"}, [{"lat": "invalid"}]],
    )
    @patch("src.app.maps.requests.get")
    def test_search_location_handles_malformed_result(self, mock_get, payload):
        response = MagicMock()
        response.json.return_value = payload
        mock_get.return_value = response

        assert search_location("Passo Fundo, RS") is None


class TestCalculateMapZoom:
    def test_returns_higher_zoom_for_smaller_area(self):
        small_area = ["-28.01", "-28.00", "-52.01", "-52.00"]
        large_area = ["-30.0", "-20.0", "-60.0", "-50.0"]

        assert calculate_map_zoom(small_area) > calculate_map_zoom(large_area)

    def test_clamps_zoom_to_minimum(self):
        assert calculate_map_zoom(["-90", "90", "-180", "180"]) == 1

    def test_clamps_zoom_to_maximum(self):
        assert calculate_map_zoom(["-28.000001", "-28", "-52.000001", "-52"]) == 20

    @pytest.mark.parametrize(
        "boundingbox",
        [
            None,
            [],
            ["-28", "-27", "-52"],
            ["south", "-27", "-52", "-51"],
            ["-28", "-27", "-52", "-51", "extra"],
            ["-27", "-28", "-52", "-51"],
        ],
    )
    def test_rejects_invalid_boundingbox(self, boundingbox):
        with pytest.raises(ValueError, match="boundingbox"):
            calculate_map_zoom(boundingbox)


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
