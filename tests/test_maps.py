import pytest
import requests
import folium
import base64
import zlib
from unittest.mock import MagicMock, patch

from src.app.maps import (
    create_base_map,
    add_index_layer,
    add_colorbar,
    create_thematic_map,
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
    create_selection_map,
    get_index_map_tile_url,
    preload_index_values,
)


class TestCreateBaseMap:
    @patch("src.app.maps.geemap")
    def test_create_base_map_with_custom_center_and_zoom(self, mock_geemap):
        mock_map = MagicMock()
        mock_geemap.Map.return_value = mock_map

        result = create_base_map(center=[-20.0, -45.0], zoom=12)

        mock_geemap.Map.assert_called_once_with(
            center=[-20.0, -45.0], zoom=12, basemap="Esri.WorldImagery"
        )
        mock_map.add_layer_control.assert_called_once()
        assert result == mock_map
        assert result == mock_map

    @patch("src.app.maps.geemap")
    def test_create_base_map_with_default_center(self, mock_geemap):
        mock_map = MagicMock()
        mock_geemap.Map.return_value = mock_map

        result = create_base_map()

        mock_geemap.Map.assert_called_once_with(
            center=DEFAULT_CENTER, zoom=DEFAULT_ZOOM, basemap="Esri.WorldImagery"
        )
        assert result == mock_map

    @patch("src.app.maps.geemap")
    def test_create_base_map_with_none_center_uses_default(self, mock_geemap):
        mock_map = MagicMock()
        mock_geemap.Map.return_value = mock_map

        result = create_base_map(center=None, zoom=DEFAULT_ZOOM)

        mock_geemap.Map.assert_called_once_with(
            center=DEFAULT_CENTER, zoom=DEFAULT_ZOOM, basemap="Esri.WorldImagery"
        )
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
    def test_search_location_handles_request_errors(self, mock_get, error, caplog):
        mock_get.side_effect = error

        with caplog.at_level("WARNING", logger="src.app.maps"):
            assert search_location("Passo Fundo, RS") is None

        record = next(record for record in caplog.records if record.name == "src.app.maps")
        assert record.getMessage() == "Location geocoding request failed or returned invalid data"
        assert record.exc_info is not None
        assert "Passo Fundo, RS" not in record.getMessage()


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

    @pytest.mark.parametrize("boundingbox", [
        ["nan", "-27", "-52", "-51"],
        ["-28", "inf", "-52", "-51"],
    ])
    def test_rejects_non_finite_boundingbox(self, boundingbox):
        with pytest.raises(ValueError, match="valores finitos"):
            calculate_map_zoom(boundingbox)

    def test_returns_maximum_zoom_for_zero_extent(self):
        assert calculate_map_zoom(["-28", "-28", "-52", "-52"]) == 20


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

    @pytest.mark.parametrize(
        "index_name, palette",
        [("NDWI", ["purple", "white", "cyan"]),
         ("NDMI", ["black", "gray", "white"])],
    )
    @patch("src.app.maps.ee")
    @patch("src.app.maps.geemap")
    def test_add_index_layer_uses_custom_palette_for_other_indices(
        self, mock_geemap, mock_ee, index_name, palette
    ):
        mock_map = MagicMock()
        mock_image = MagicMock()
        mock_contains = MagicMock()
        mock_contains.getInfo.return_value = True
        mock_image.bandNames.return_value.contains.return_value = mock_contains

        add_index_layer(mock_map, mock_image, index_name, palette=palette)

        assert mock_map.addLayer.call_args[0][1]["palette"] == palette

    @pytest.mark.parametrize("index_name", ["NDWI", "NDMI"])
    @patch("src.app.maps.ee")
    def test_add_index_layer_rejects_missing_band_for_other_indices(
        self, mock_ee, index_name
    ):
        mock_map = MagicMock()
        mock_image = MagicMock()
        mock_contains = MagicMock()
        mock_contains.getInfo.return_value = False
        mock_image.bandNames.return_value.contains.return_value = mock_contains

        with pytest.raises(ValueError, match=f"Imagem não contém banda {index_name}"):
            add_index_layer(mock_map, mock_image, index_name)


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


class TestCreateThematicMap:
    @pytest.mark.parametrize(
        "index_name, expected_palette",
        [
            ("NDVI", NDVI_PALETTE),
            ("NDWI", NDWI_PALETTE),
            ("NDMI", NDMI_PALETTE),
        ],
    )
    def test_creates_thematic_layer_legend_and_area_outline(
        self, monkeypatch, index_name, expected_palette
    ):
        index_image = MagicMock(name="cached_index_image")
        geometry = {"type": "Feature", "geometry": {"type": "Polygon"}}
        map_obj = MagicMock()
        add_index = MagicMock()
        add_legend = MagicMock()
        monkeypatch.setattr("src.app.maps.create_base_map", MagicMock(return_value=map_obj))
        monkeypatch.setattr("src.app.maps.add_index_layer", add_index)
        monkeypatch.setattr("src.app.maps.add_colorbar", add_legend)

        result = create_thematic_map(
            index_image,
            index_name,
            center=[-28.0, -52.0],
            zoom=12,
            geojson=geometry,
        )

        assert result is map_obj
        add_index.assert_called_once_with(
            map_obj,
            index_image,
            index_name,
            palette=expected_palette,
            validate_band=False,
        )
        add_legend.assert_called_once_with(map_obj, expected_palette, index_name)
        map_obj.add_geojson.assert_called_once_with(
            geometry,
            layer_name="Área selecionada",
            style={"color": "#ff7800", "weight": 3, "fillOpacity": 0},
        )

    def test_creates_map_without_area_overlay_when_geojson_is_absent(self, monkeypatch):
        map_obj = MagicMock()
        monkeypatch.setattr("src.app.maps.create_base_map", MagicMock(return_value=map_obj))
        monkeypatch.setattr("src.app.maps.add_index_layer", MagicMock())
        monkeypatch.setattr("src.app.maps.add_colorbar", MagicMock())

        create_thematic_map(MagicMock(), "NDVI")

        map_obj.add_geojson.assert_not_called()

    def test_rejects_unknown_index(self):
        with pytest.raises(ValueError, match="Índice desconhecido: INVALID"):
            create_thematic_map(MagicMock(), "INVALID")


class TestIndexPixelPreloading:
    def test_get_index_map_tile_url_clips_and_uses_data_range(self):
        image = MagicMock()
        geometry = MagicMock()
        fetcher = MagicMock()
        fetcher.url_format = "https://earthengine.example/{z}/{x}/{y}"
        image.select.return_value.clip.return_value.getMapId.return_value = {
            "tile_fetcher": fetcher,
        }

        result = get_index_map_tile_url(image, "NDVI", geometry, 0.2, 0.8)

        assert result == fetcher.url_format
        image.select.assert_called_once_with("NDVI")
        image.select.return_value.clip.assert_called_once_with(geometry)
        params = image.select.return_value.clip.return_value.getMapId.call_args.args[0]
        assert params["min"] == 0.2
        assert params["max"] == 0.8
        assert params["palette"] == NDVI_PALETTE

    @pytest.mark.parametrize("minimum, maximum", [(float("nan"), 0.5), (0.8, 0.2)])
    def test_tile_url_falls_back_to_full_index_range_for_invalid_data_range(
        self, minimum, maximum
    ):
        image = MagicMock()
        fetcher = MagicMock()
        fetcher.url_format = "https://earthengine.example/tiles"
        image.select.return_value.clip.return_value.getMapId.return_value = {
            "tile_fetcher": fetcher
        }

        result = get_index_map_tile_url(image, "NDVI", MagicMock(), minimum, maximum)

        assert result == fetcher.url_format
        params = image.select.return_value.clip.return_value.getMapId.call_args.args[0]
        assert (params["min"], params["max"]) == (-1, 1)

    def test_tile_url_rejects_unknown_index_and_missing_tile_url(self):
        with pytest.raises(ValueError, match="Índice desconhecido"):
            get_index_map_tile_url(MagicMock(), "EVI", MagicMock())

        image = MagicMock()
        image.select.return_value.clip.return_value.getMapId.return_value = {}
        with pytest.raises(ValueError, match="não retornou uma URL"):
            get_index_map_tile_url(image, "NDVI", MagicMock())

    @staticmethod
    def configure_preload(mock_ee, geometry, *, bounds=None, transform=None,
                          properties=None):
        region = MagicMock()
        geometry.bounds.return_value = region
        region.coordinates.return_value.getInfo.return_value = bounds or [[
            [0, 0], [20, 0], [20, 20], [0, 20], [0, 0]
        ]]
        projection = MagicMock()
        mock_ee.Projection.return_value.atScale.return_value = projection
        projection.getInfo.return_value = {
            "transform": transform if transform is not None else [10, 0, 0, 0, -10, 0]
        }
        stack = MagicMock()
        stack.addBands.return_value = stack
        stack.sampleRectangle.return_value.getInfo.return_value = {
            "properties": properties if properties is not None else {
                "NDVI": [[0.2, 0.4], [0.6, 0.8]],
                "grid_x": [[100, 101], [100, 101]],
                "grid_y": [[200, 200], [201, 201]],
            }
        }
        image = MagicMock()
        image.select.return_value.reproject.return_value.clip.return_value.rename.return_value.toFloat.return_value = stack
        mock_ee.Image.pixelCoordinates.return_value.rename.return_value = MagicMock()
        return image, stack

    @patch("src.app.maps.ee")
    def test_preloads_clipped_index_grid_for_local_hover(self, mock_ee):
        geometry = MagicMock()
        region = MagicMock()
        geometry.bounds.return_value = region
        region.coordinates.return_value.getInfo.return_value = [[
            [0, 0], [20, 0], [20, 20], [0, 20], [0, 0],
        ]]
        projection = MagicMock()
        mock_ee.Projection.return_value.atScale.return_value = projection
        projection.getInfo.return_value = {"transform": [10, 0, 0, 0, -10, 0]}
        image = MagicMock()
        projected_image = image.select.return_value.reproject.return_value.clip.return_value.rename.return_value.toFloat.return_value
        stack = MagicMock()
        projected_image.addBands.return_value = stack
        pixel_coordinates = MagicMock()
        mock_ee.Image.pixelCoordinates.return_value.rename.return_value = pixel_coordinates
        stack.sampleRectangle.return_value.getInfo.return_value = {
            "properties": {
                "NDVI": [[0.2, 0.4], [0.6, 0.8]],
                "grid_x": [[100, 101], [100, 101]],
                "grid_y": [[200, 200], [201, 201]],
            },
        }

        result = preload_index_values({"NDVI": image}, geometry, [-28, -52])

        pixels = result["indices"]["NDVI"]
        raw = zlib.decompress(base64.b64decode(pixels["values"]))
        assert pixels["rows"] == 2
        assert pixels["columns"] == 2
        assert pixels["minimum"] == pytest.approx(0.2)
        assert pixels["maximum"] == pytest.approx(0.8)
        assert result["first_column"] == 100
        assert result["first_row"] == 200
        assert len(raw) == 4 * 4
        image.select.assert_called_once_with("NDVI")
        assert projected_image.addBands.call_count == 1
        stack.sampleRectangle.assert_called_once_with(region=region, defaultValue=-9999.0)

    @patch("src.app.maps.ee")
    def test_preload_rejects_grid_exceeding_transfer_limit(self, mock_ee):
        region = MagicMock()
        geometry = MagicMock()
        geometry.bounds.return_value = region
        region.coordinates.return_value.getInfo.return_value = [[
            [0, 0], [10000, 0], [10000, 10000], [0, 10000], [0, 0],
        ]]
        projection = MagicMock()
        mock_ee.Projection.return_value.atScale.return_value = projection
        projection.getInfo.return_value = {"transform": [10, 0, 0, 0, -10, 0]}

        with pytest.raises(ValueError, match="grande demais para pré-carregar"):
            preload_index_values({"NDVI": MagicMock()}, geometry, [-28, -52])

    @pytest.mark.parametrize(
        "images, scale, error",
        [({}, 10, "Nenhum índice"), ({"NDVI": MagicMock()}, 0, "escala"),
         ({"NDVI": MagicMock()}, 1.5, "escala")],
    )
    @patch("src.app.maps.ee")
    def test_preload_rejects_empty_images_and_invalid_scales(
        self, mock_ee, images, scale, error
    ):
        with pytest.raises(ValueError, match=error):
            preload_index_values(images, MagicMock(), [-28, -52], scale=scale)
        mock_ee.Projection.assert_not_called()

    @patch("src.app.maps.ee")
    def test_preload_rejects_missing_projection_transform(self, mock_ee):
        mock_ee.Projection.return_value.atScale.return_value.getInfo.return_value = {}

        with pytest.raises(ValueError, match="grade espacial"):
            preload_index_values({"NDVI": MagicMock()}, MagicMock(), [-28, -52])

    @pytest.mark.parametrize(
        "bounds",
        [[["bad", "bounds"]], [[[["bad", 0], [1, 1]]]]],
    )
    @patch("src.app.maps.ee")
    def test_preload_rejects_invalid_bounds(self, mock_ee, bounds):
        geometry = MagicMock()
        self.configure_preload(mock_ee, geometry, bounds=bounds)
        with pytest.raises(ValueError, match="extensão válida"):
            preload_index_values({"NDVI": MagicMock()}, geometry, [-28, -52])

    @pytest.mark.parametrize(
        "properties",
        [
            {"NDVI": [[0.2]], "grid_x": [], "grid_y": []},
            {"NDVI": [[0.2]], "grid_x": [[1]], "grid_y": [[1, 2]]},
            {"NDVI": [[0.2]], "grid_x": [[1]], "grid_y": [[1]]},
        ],
    )
    @patch("src.app.maps.ee")
    def test_preload_rejects_empty_or_inconsistent_grid_coordinates(
        self, mock_ee, properties
    ):
        geometry = MagicMock()
        self.configure_preload(mock_ee, geometry, properties=properties)
        with pytest.raises(ValueError, match="não retornou pixels"):
            preload_index_values({"NDVI": MagicMock()}, geometry, [-28, -52])

    @patch("src.app.maps.ee")
    def test_preload_rejects_invalid_index_pixel_shape(self, mock_ee):
        geometry = MagicMock()
        image, _ = self.configure_preload(
            mock_ee,
            geometry,
            properties={
                "NDVI": [0.2, 0.4],
                "grid_x": [[1, 2]],
                "grid_y": [[1, 1]],
            },
        )
        with pytest.raises(ValueError, match="pixels de NDVI"):
            preload_index_values({"NDVI": image}, geometry, [-28, -52])

    @patch("src.app.maps.ee")
    def test_preload_handles_empty_values_and_constant_edge_ranges(self, mock_ee):
        geometry = MagicMock()
        image, _ = self.configure_preload(
            mock_ee,
            geometry,
            properties={
                "NDVI": [[-9999.0, float("nan")]],
                "NDWI": [[-1.0, -1.0]],
                "NDMI": [[1.0, 1.0]],
                "grid_x": [[1, 2]],
                "grid_y": [[1, 1]],
            },
        )
        results = preload_index_values(
            {"NDVI": image, "NDWI": image, "NDMI": image}, geometry, [-28, -52]
        )

        assert results["indices"]["NDVI"]["minimum"] == -1.0
        assert results["indices"]["NDVI"]["maximum"] == 1.0
        assert results["indices"]["NDWI"]["minimum"] == -1.0
        assert results["indices"]["NDWI"]["maximum"] == pytest.approx(-0.99)
        assert results["indices"]["NDMI"]["minimum"] == pytest.approx(0.99)
        assert results["indices"]["NDMI"]["maximum"] == 1.0

    @patch("src.app.maps.ee")
    def test_preload_rejects_actual_sample_size_over_transfer_limit(
        self, mock_ee, monkeypatch
    ):
        import src.app.maps as maps_module

        monkeypatch.setattr(maps_module, "MAX_PRELOADED_VALUES", 50)
        geometry = MagicMock()
        image, stack = self.configure_preload(mock_ee, geometry)
        values = [[0.2] * 8 for _ in range(8)]
        coordinates = [list(range(8)) for _ in range(8)]
        stack.sampleRectangle.return_value.getInfo.return_value["properties"].update(
            {"NDVI": values, "grid_x": coordinates, "grid_y": coordinates}
        )

        with pytest.raises(ValueError, match="grande demais para pré-carregar"):
            preload_index_values({"NDVI": image}, geometry, [-28, -52])


class TestEnableAreaDraw:
    @patch("src.app.maps.geemap")
    def test_enable_area_draw_polygon(self, mock_geemap):
        mock_map = MagicMock()
        mock_draw_control = MagicMock()
        mock_map.draw_control = mock_draw_control

        enable_area_draw(mock_map)

        mock_map.add_draw_control_lite.assert_called_once()


class TestCreateSelectionMap:
    def test_uses_esri_world_imagery_as_base_layer_with_attribution(self):
        result = create_selection_map()

        tile_layers = [
            child
            for child in result._children.values()
            if isinstance(child, folium.TileLayer)
        ]

        assert len(tile_layers) == 1
        tile_layer = tile_layers[0]
        assert tile_layer.tiles == (
            "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/"
            "MapServer/tile/{z}/{y}/{x}"
        )
        assert tile_layer.options["attribution"] == (
            "Tiles © Esri — Source: Esri, Maxar, Earthstar Geographics, "
            "and the GIS User Community"
        )
        assert tile_layer.layer_name == "Satélite (Esri)"
        assert tile_layer.overlay is False
        assert tile_layer.control is True

    def test_keeps_scale_control(self):
        result = create_selection_map()

        assert result.control_scale is True

    def test_exposes_base_layer_in_layer_control(self):
        result = create_selection_map()

        assert any(
            type(child).__name__ == "LayerControl"
            for child in result._children.values()
        )

    def test_creates_map_with_default_center_and_zoom(self):
        result = create_selection_map()

        assert result.location == DEFAULT_CENTER
        assert result.options["zoom"] == DEFAULT_ZOOM

    def test_creates_map_with_custom_center_and_zoom(self):
        result = create_selection_map(center=[-20.0, -45.0], zoom=12)

        assert result.location == [-20.0, -45.0]
        assert result.options["zoom"] == 12

    @patch("src.app.maps.Draw")
    def test_keeps_native_polygon_draw_control_without_other_draw_tools(
        self, draw_control
    ):
        create_selection_map()

        draw_control.assert_called_once_with(
            export=False,
            feature_group=draw_control.call_args.kwargs["feature_group"],
            draw_options={
                "polyline": False,
                "rectangle": False,
                "circle": False,
                "marker": False,
                "circlemarker": False,
                "polygon": True,
            },
            edit_options={"edit": True, "remove": True},
        )
        assert isinstance(
            draw_control.call_args.kwargs["feature_group"], folium.FeatureGroup
        )
        draw_control.return_value.add_to.assert_called_once()

    @pytest.mark.parametrize("zoom", [0, 21, 10.5])
    def test_rejects_invalid_zoom(self, zoom):
        with pytest.raises(ValueError, match="zoom deve ser inteiro entre 1 e 20"):
            create_selection_map(zoom=zoom)

    def test_adds_selected_geojson(self):
        geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[-52.1, -28.0], [-52.0, -28.0],
                                  [-52.0, -28.1], [-52.1, -28.0]]],
            },
        }

        result = create_selection_map(geojson=geojson)

        drawn_items = next(
            child
            for child in result._children.values()
            if isinstance(child, folium.FeatureGroup)
        )
        assert any(
            type(child).__name__ == "GeoJson"
            for child in drawn_items._children.values()
        )
        draw_control = next(
            child
            for child in result._children.values()
            if getattr(child, "feature_group", None) is drawn_items
        )
        assert draw_control.feature_group is drawn_items

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

    @patch("src.app.maps.ee")
    def test_converts_valid_concave_polygon(self, mock_ee):
        coordinates = [[
            [0, 0], [3, 0], [3, 3], [2, 1], [0, 3], [0, 0],
        ]]

        geojson_to_ee_geometry({"type": "Polygon", "coordinates": coordinates})

        mock_ee.Geometry.Polygon.assert_called_once_with(coordinates)

    def test_rejects_non_polygon(self):
        with pytest.raises(ValueError, match="usando um polígono"):
            geojson_to_ee_geometry({"type": "Point", "coordinates": [-52, -28]})

    @pytest.mark.parametrize(
        "geojson, message",
        [
            (None, "formato GeoJSON válido"),
            ({}, "usando um polígono"),
            ({"type": "Polygon", "coordinates": []}, "usando um polígono"),
            ({"type": "Polygon", "coordinates": [[[0, 0], [1, 1], [0, 0]]]},
             "três vértices distintos"),
            ({"type": "Polygon", "coordinates": [[[0, 0], [1, 0], [1, 1], [0, 1]]]},
             "anel fechado"),
            ({"type": "Polygon", "coordinates": [[[0, 0], [1, 0], [2, 0], [0, 0]]]},
             "área zero"),
            ({"type": "Polygon", "coordinates": [[[0, 0], [4, 3], [0, 4], [3, 0], [0, 0]]]},
             "lados não podem se cruzar"),
            ({"type": "Polygon", "coordinates": {"ring": []}}, "anel válido"),
            ({"type": "Polygon", "coordinates": [1]}, "anel do polígono está malformado"),
            ({"type": "Polygon", "coordinates": [[0, [1, 2], [2, 2], [0, 0]]]},
             "coordenadas do polígono estão malformadas"),
            ({"type": "Polygon", "coordinates": [[[0, 0], [1, 0], [0, 0], [0, 0]]]},
             "três vértices distintos"),
            ({"type": "Polygon", "coordinates": [[[0, 0], [float("nan"), 1], [1, 1], [0, 0]]]},
             "finitas"),
            ({"type": "Polygon", "coordinates": [[[0, 0], [181, 0], [1, 1], [0, 0]]]},
             "limites geográficos"),
            ({"type": "Feature", "geometry": None}, "geometria GeoJSON está malformada"),
        ],
    )
    def test_rejects_invalid_polygon_payload(self, geojson, message):
        with pytest.raises(ValueError, match=message):
            geojson_to_ee_geometry(geojson)


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


class TestCalculateAreaContext:
    @pytest.fixture
    def mock_ee_geometry(self):
        """Create an Earth Engine-like geometry with area, perimeter and centroid methods."""
        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = 2500000.0  # 250 ha in m²
        geometry.perimeter.return_value.getInfo.return_value = 20000.0  # 20 km in m
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-52.4, -28.3]
        return geometry

    @patch("src.app.maps.ee")
    def test_calculate_area_context_returns_all_metrics(self, mock_ee, mock_ee_geometry):
        from src.app.maps import calculate_area_context

        result = calculate_area_context(mock_ee_geometry)

        assert result["area_ha"] == 250.0
        assert result["perimeter_km"] == 20.0
        assert result["centroid"] == (-28.3, -52.4)

    @patch("src.app.maps.ee")
    def test_calculate_area_context_area_conversion_m2_to_ha(self, mock_ee):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = 1000000.0  # 100 ha in m²
        geometry.perimeter.return_value.getInfo.return_value = 10000.0  # 10 km in m
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-50.0, -20.0]

        result = calculate_area_context(geometry)

        assert result["area_ha"] == 100.0

    @patch("src.app.maps.ee")
    def test_calculate_area_context_perimeter_conversion_m_to_km(self, mock_ee):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = 2500000.0
        geometry.perimeter.return_value.getInfo.return_value = 15000.0  # 15 km in m
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-50.0, -20.0]

        result = calculate_area_context(geometry)

        assert result["perimeter_km"] == 15.0

    @patch("src.app.maps.ee")
    def test_calculate_area_context_centroid_order_lat_lon(self, mock_ee):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = 125000.0  # 12.5 ha in m²
        geometry.perimeter.return_value.getInfo.return_value = 5000.0  # 5 km in m
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-52.41, -28.26]

        result = calculate_area_context(geometry)

        assert result["centroid"] == (-28.26, -52.41)

    def test_calculate_area_context_raises_for_invalid_area(self):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = float("nan")
        geometry.perimeter.return_value.getInfo.return_value = 5000.0
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-52.4, -28.3]

        with pytest.raises(ValueError, match="valores finitos"):
            calculate_area_context(geometry)

    def test_calculate_area_context_raises_for_zero_area(self):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = 0.0
        geometry.perimeter.return_value.getInfo.return_value = 5000.0
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-52.4, -28.3]

        with pytest.raises(ValueError, match="área <= 0"):
            calculate_area_context(geometry)

    def test_calculate_area_context_raises_for_negative_area(self):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = -10000.0
        geometry.perimeter.return_value.getInfo.return_value = 5000.0
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-52.4, -28.3]

        with pytest.raises(ValueError, match="área <= 0"):
            calculate_area_context(geometry)

    def test_calculate_area_context_raises_for_invalid_perimeter(self):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = 125000.0
        geometry.perimeter.return_value.getInfo.return_value = float("inf")
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-52.4, -28.3]

        with pytest.raises(ValueError, match="valores finitos"):
            calculate_area_context(geometry)

    def test_calculate_area_context_raises_for_zero_perimeter(self):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = 125000.0
        geometry.perimeter.return_value.getInfo.return_value = 0.0
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-52.4, -28.3]

        with pytest.raises(ValueError, match="perímetro.*<= 0"):
            calculate_area_context(geometry)

    def test_calculate_area_context_raises_for_malformed_centroid(self):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = 125000.0
        geometry.perimeter.return_value.getInfo.return_value = 5000.0
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-52.4]

        with pytest.raises(ValueError, match="Centroide inválido"):
            calculate_area_context(geometry)

    def test_calculate_area_context_wraps_non_value_errors(self):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.side_effect = RuntimeError("offline")

        with pytest.raises(ValueError, match="Falha ao calcular contexto geográfico: offline"):
            calculate_area_context(geometry)

    def test_calculate_area_context_raises_for_invalid_centroid(self):
        from src.app.maps import calculate_area_context

        geometry = MagicMock()
        geometry.area.return_value.getInfo.return_value = 125000.0
        geometry.perimeter.return_value.getInfo.return_value = 5000.0
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [float("nan"), -28.3]

        with pytest.raises(ValueError, match="Centroide contém valores não finitos"):
            calculate_area_context(geometry)

    def test_calculate_area_context_raises_for_none_geometry(self):
        from src.app.maps import calculate_area_context

        with pytest.raises(ValueError, match="Geometria inválida"):
            calculate_area_context(None)
