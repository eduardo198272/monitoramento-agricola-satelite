from io import BytesIO
from unittest.mock import MagicMock

from PIL import Image
import pytest

from src.app.export_maps import (
    ESRI_WORLD_IMAGERY_ATTRIBUTION,
    StaticMapResult,
    render_static_index_map,
)


GEOMETRY = {
    "type": "Polygon",
    "coordinates": [[
        [-52.0, -28.0],
        [-51.99, -28.0],
        [-51.99, -27.99],
        [-52.0, -27.99],
        [-52.0, -28.0],
    ]],
}


def png_bytes(color, size=(256, 256), mode="RGB"):
    buffer = BytesIO()
    Image.new(mode, size, color).save(buffer, format="PNG")
    return buffer.getvalue()


class FakeResponse:
    def __init__(self, content):
        self.content = content

    def raise_for_status(self):
        return None


@pytest.mark.parametrize("index_name", ["NDVI", "NDWI", "NDMI"])
def test_render_static_index_map_composes_satellite_index_outline_and_legend(
    monkeypatch, index_name
):
    import src.app.export_maps as export_maps

    index_image = MagicMock()
    visualized = MagicMock()
    index_image.select.return_value.clip.return_value.visualize.return_value = visualized
    visualized.getThumbURL.return_value = "https://earthengine.test/thumbnail"
    requested_urls = []

    def fake_get(url, timeout):
        requested_urls.append(url)
        return FakeResponse(
            png_bytes((230, 230, 230) if "earthengine.test" in url else (30, 80, 120))
        )

    monkeypatch.setattr(export_maps.requests, "get", fake_get)
    result = render_static_index_map(
        index_image,
        index_name,
        GEOMETRY,
        width=512,
        height=384,
    )

    assert isinstance(result, StaticMapResult)
    assert result.status == "available"
    assert result.image_bytes.startswith(b"\x89PNG\r\n\x1a\n")
    assert result.attribution == ESRI_WORLD_IMAGERY_ATTRIBUTION
    assert result.error is None
    output = Image.open(BytesIO(result.image_bytes))
    assert output.size == (512, 384)
    assert output.mode == "RGB"
    center_pixel = output.getpixel((256, 192))
    assert all(160 <= value <= 205 for value in center_pixel)
    colors = {color for _, color in output.getcolors(maxcolors=512 * 384)}
    assert (255, 120, 0) in colors  # GeoJSON outline
    assert any(
        red > 220 and green > 220 and blue > 220 for red, green, blue in colors
    )  # legend panel
    index_image.select.assert_called_once_with(index_name)
    index_image.select.return_value.clip.assert_called_once()
    visual_params = index_image.select.return_value.clip.return_value.visualize.call_args.kwargs
    assert visual_params["min"] == -1
    assert visual_params["max"] == 1
    assert visual_params["opacity"] == 0.7
    assert len(visual_params["palette"]) == 3
    thumbnail_params = visualized.getThumbURL.call_args.args[0]
    assert thumbnail_params["dimensions"] == "512x384"
    assert thumbnail_params["crs"] == "EPSG:3857"
    assert thumbnail_params["format"] == "png"
    assert len(requested_urls) >= 2
    assert any("/tile/" in url for url in requested_urls)


def test_render_static_index_map_returns_explicit_unavailable_result_on_remote_failure(
    monkeypatch,
):
    import src.app.export_maps as export_maps

    index_image = MagicMock()
    index_image.select.return_value.clip.return_value.visualize.return_value.getThumbURL.side_effect = (
        RuntimeError("Earth Engine indisponível")
    )
    monkeypatch.setattr(export_maps.requests, "get", MagicMock())

    result = render_static_index_map(index_image, "NDVI", GEOMETRY)

    assert result.status == "unavailable"
    assert result.image_bytes is None
    assert result.error
    export_maps.requests.get.assert_not_called()


def test_render_static_index_map_reports_tile_download_failure(monkeypatch):
    import src.app.export_maps as export_maps

    index_image = MagicMock()
    visualized = index_image.select.return_value.clip.return_value.visualize.return_value
    visualized.getThumbURL.return_value = "https://earthengine.test/thumbnail"

    def fail_tile(url, timeout):
        if "/tile/" in url:
            raise RuntimeError("tiles indisponíveis")
        return FakeResponse(png_bytes((200, 200, 200)))

    monkeypatch.setattr(export_maps.requests, "get", fail_tile)
    result = render_static_index_map(index_image, "NDVI", GEOMETRY, width=256, height=256)

    assert result.status == "unavailable"
    assert result.image_bytes is None
    assert "tiles indisponíveis" in result.error


def test_render_static_index_map_resizes_nonstandard_satellite_tiles(monkeypatch):
    import src.app.export_maps as export_maps

    index_image = MagicMock()
    visualized = index_image.select.return_value.clip.return_value.visualize.return_value
    visualized.getThumbURL.return_value = "https://earthengine.test/thumbnail"

    def fake_get(url, timeout):
        color = (30, 80, 120) if "/tile/" in url else (230, 230, 230)
        size = (128, 128) if "/tile/" in url else (512, 384)
        return FakeResponse(png_bytes(color, size))

    monkeypatch.setattr(export_maps.requests, "get", fake_get)
    result = render_static_index_map(
        index_image, "NDVI", GEOMETRY, width=512, height=384
    )

    assert result.status == "available"
    assert Image.open(BytesIO(result.image_bytes)).size == (512, 384)


def test_render_static_index_map_preserves_thumbnail_alpha(monkeypatch):
    import src.app.export_maps as export_maps

    index_image = MagicMock()
    visualized = index_image.select.return_value.clip.return_value.visualize.return_value
    visualized.getThumbURL.return_value = "https://earthengine.test/thumbnail"

    def fake_get(url, timeout):
        if "/tile/" in url:
            return FakeResponse(png_bytes((30, 80, 120)))
        return FakeResponse(
            png_bytes((230, 230, 230, 128), (512, 384), mode="RGBA")
        )

    monkeypatch.setattr(export_maps.requests, "get", fake_get)
    result = render_static_index_map(
        index_image, "NDVI", GEOMETRY, width=512, height=384
    )

    assert result.status == "available"
    pixel = Image.open(BytesIO(result.image_bytes)).getpixel((256, 192))
    assert all(100 <= value <= 180 for value in pixel)


def test_render_static_index_map_rejects_unknown_index_before_network(monkeypatch):
    import src.app.export_maps as export_maps

    get = MagicMock()
    monkeypatch.setattr(export_maps.requests, "get", get)

    with pytest.raises(ValueError, match="Índice desconhecido"):
        render_static_index_map(MagicMock(), "EVI", GEOMETRY)

    get.assert_not_called()


@pytest.mark.parametrize(
    "geometry",
    [
        None,
        {"type": "Point", "coordinates": [-52.0, -28.0]},
        {"type": "Polygon", "coordinates": [None]},
        {"type": "Polygon", "coordinates": [[[-52.0, -28.0], [-52.0, -28.0]]]},
        {"type": "Polygon", "coordinates": [[[-52.0, -28.0], [181, 0], [-52.0, -28.0], [-52.0, -28.0]]]},
        {"type": "Polygon", "coordinates": [[[-52.0, -28.0], [True, 0], [-52.0, -28.0], [-52.0, -28.0]]]},
        {
            "type": "Polygon",
            "coordinates": [[[-52.0, -28.0], [float("nan"), 0], [-52.0, -28.0]]],
        },
    ],
)
def test_render_static_index_map_rejects_invalid_geometry_before_network(
    monkeypatch, geometry
):
    import src.app.export_maps as export_maps

    get = MagicMock()
    monkeypatch.setattr(export_maps.requests, "get", get)

    with pytest.raises(ValueError, match="geometria GeoJSON"):
        render_static_index_map(MagicMock(), "NDVI", geometry)

    get.assert_not_called()


def test_render_static_index_map_rejects_geometry_that_cannot_fit_minimum_canvas(
    monkeypatch,
):
    import src.app.export_maps as export_maps

    get = MagicMock()
    monkeypatch.setattr(export_maps.requests, "get", get)
    world_geometry = {
        "type": "Polygon",
        "coordinates": [[
            [-180, -80], [180, -80], [180, 80], [-180, 80], [-180, -80]
        ]],
    }

    with pytest.raises(ValueError, match="Geometria grande demais"):
        render_static_index_map(
            MagicMock(), "NDVI", world_geometry, width=256, height=256
        )

    get.assert_not_called()


def test_viewport_uses_maximum_zoom_when_geometry_fits_all_levels():
    import src.app.export_maps as export_maps

    tiny_bounds = (-52.000001, -28.000001, -52.0, -28.0)

    zoom, _, _ = export_maps._map_viewport(tiny_bounds, 512, 384)

    assert zoom == export_maps.MAX_ZOOM


@pytest.mark.parametrize("width,height", [(255, 400), (400, 255), (256.0, 400)])
def test_render_static_index_map_rejects_invalid_dimensions_before_network(
    monkeypatch, width, height
):
    import src.app.export_maps as export_maps

    get = MagicMock()
    monkeypatch.setattr(export_maps.requests, "get", get)

    with pytest.raises(ValueError, match="Dimensões do mapa"):
        render_static_index_map(
            MagicMock(), "NDVI", GEOMETRY, width=width, height=height
        )

    get.assert_not_called()
