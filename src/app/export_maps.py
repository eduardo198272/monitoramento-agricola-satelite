"""Offline-testable raster map rendering for export artifacts."""

from dataclasses import dataclass
from io import BytesIO
import logging
import math
import textwrap

import ee
from PIL import Image, ImageDraw, ImageFont
import requests

from src.app.maps import (
    ESRI_WORLD_IMAGERY_ATTRIBUTION,
    ESRI_WORLD_IMAGERY_URL,
    INDEX_PALETTES,
)

logger = logging.getLogger(__name__)

TILE_SIZE = 256
MAX_ZOOM = 18
MAP_MARGIN = 28
MAP_OVERLAY_OPACITY = 0.7
REQUEST_TIMEOUT = 30
LEGEND_COLORS = {
    "NDVI": "NDVI: -1.0 a +1.0",
    "NDWI": "NDWI: -1.0 a +1.0",
    "NDMI": "NDMI: -1.0 a +1.0",
}


@dataclass(frozen=True)
class StaticMapResult:
    """A rendered map or an explicit per-index unavailable state."""

    status: str
    image_bytes: bytes | None
    attribution: str
    error: str | None = None


def _geometry_bounds(geometry_geojson: dict) -> tuple[float, float, float, float]:
    if (
        not isinstance(geometry_geojson, dict)
        or geometry_geojson.get("type") != "Polygon"
        or not isinstance(geometry_geojson.get("coordinates"), list)
        or not geometry_geojson["coordinates"]
    ):
        raise ValueError("A renderização exige uma geometria GeoJSON Polygon válida")

    rings = geometry_geojson["coordinates"]
    if any(
        not isinstance(ring, (list, tuple))
        or len(ring) < 4
        or ring[0] != ring[-1]
        for ring in rings
    ):
        raise ValueError("A geometria GeoJSON contém um anel inválido")
    points = [point for ring in rings for point in ring]
    if not points or any(
        not isinstance(point, (list, tuple))
        or len(point) < 2
        or any(
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(value)
            for value in point[:2]
        )
        or not -180 <= point[0] <= 180
        or not -90 <= point[1] <= 90
        for point in points
    ):
        raise ValueError("A geometria GeoJSON contém coordenadas inválidas")

    longitudes = [point[0] for point in points]
    latitudes = [point[1] for point in points]
    return min(longitudes), min(latitudes), max(longitudes), max(latitudes)


def _world_pixel(longitude: float, latitude: float, zoom: int) -> tuple[float, float]:
    scale = TILE_SIZE * (2**zoom)
    latitude = max(-85.05112878, min(85.05112878, latitude))
    x = (longitude + 180.0) / 360.0 * scale
    sin_latitude = math.sin(math.radians(latitude))
    y = (0.5 - math.log((1 + sin_latitude) / (1 - sin_latitude)) / (4 * math.pi)) * scale
    return x, y


def _world_lonlat(x: float, y: float, zoom: int) -> tuple[float, float]:
    scale = TILE_SIZE * (2**zoom)
    longitude = x / scale * 360.0 - 180.0
    mercator_y = math.pi * (1 - 2 * y / scale)
    latitude = math.degrees(math.atan(math.sinh(mercator_y)))
    return longitude, latitude


def _map_viewport(bounds, width, height):
    west, south, east, north = bounds
    usable_width = width - 2 * MAP_MARGIN
    usable_height = height - 2 * MAP_MARGIN
    selected_zoom = 0
    selected_extent = None
    for zoom in range(MAX_ZOOM + 1):
        top_left = _world_pixel(west, north, zoom)
        bottom_right = _world_pixel(east, south, zoom)
        extent_width = max(1.0, bottom_right[0] - top_left[0])
        extent_height = max(1.0, bottom_right[1] - top_left[1])
        if extent_width <= usable_width and extent_height <= usable_height:
            selected_zoom = zoom
            selected_extent = (top_left, bottom_right)
        else:
            break

    if selected_extent is None:
        raise ValueError("Geometria grande demais para o enquadramento solicitado")
    top_left, bottom_right = selected_extent
    center_x = (top_left[0] + bottom_right[0]) / 2
    center_y = (top_left[1] + bottom_right[1]) / 2
    view_left = center_x - width / 2
    view_top = center_y - height / 2
    return selected_zoom, view_left, view_top


def _fetch_satellite(width, height, zoom, view_left, view_top, http_get):
    view_right = view_left + width
    view_bottom = view_top + height
    first_tile_x = math.floor(view_left / TILE_SIZE)
    last_tile_x = math.floor((view_right - 1) / TILE_SIZE)
    first_tile_y = max(0, math.floor(view_top / TILE_SIZE))
    last_tile_y = min(2**zoom - 1, math.floor((view_bottom - 1) / TILE_SIZE))
    tile_world_size = 2**zoom
    mosaic = Image.new(
        "RGB",
        ((last_tile_x - first_tile_x + 1) * TILE_SIZE,
         (last_tile_y - first_tile_y + 1) * TILE_SIZE),
    )

    for tile_y in range(first_tile_y, last_tile_y + 1):
        for tile_x in range(first_tile_x, last_tile_x + 1):
            wrapped_x = tile_x % tile_world_size
            url = ESRI_WORLD_IMAGERY_URL.format(
                z=zoom, y=tile_y, x=wrapped_x
            )
            response = http_get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            tile = Image.open(BytesIO(response.content)).convert("RGB")
            if tile.size != (TILE_SIZE, TILE_SIZE):
                tile = tile.resize((TILE_SIZE, TILE_SIZE), Image.Resampling.LANCZOS)
            mosaic.paste(
                tile,
                ((tile_x - first_tile_x) * TILE_SIZE,
                 (tile_y - first_tile_y) * TILE_SIZE),
            )

    crop_box = (
        round(view_left - first_tile_x * TILE_SIZE),
        round(view_top - first_tile_y * TILE_SIZE),
        round(view_right - first_tile_x * TILE_SIZE),
        round(view_bottom - first_tile_y * TILE_SIZE),
    )
    return mosaic.crop(crop_box)


def _palette_color(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return tuple(int(color[offset : offset + 2], 16) for offset in (0, 2, 4))


def _draw_legend(image: Image.Image, index_name: str) -> None:
    draw = ImageDraw.Draw(image, "RGBA")
    font = ImageFont.load_default()
    x, y = 14, image.height - 73
    draw.rounded_rectangle((x, y, x + 226, y + 58), radius=5, fill=(255, 255, 255, 225))
    draw.text((x + 9, y + 6), LEGEND_COLORS[index_name], fill=(20, 20, 20, 255), font=font)

    palette = [_palette_color(color) for color in INDEX_PALETTES[index_name]]
    ramp_left, ramp_top, ramp_width, ramp_height = x + 9, y + 24, 208, 12
    ramp = Image.new("RGB", (ramp_width, ramp_height))
    ramp_draw = ImageDraw.Draw(ramp)
    for pixel_x in range(ramp_width):
        position = pixel_x / max(1, ramp_width - 1) * (len(palette) - 1)
        start = min(int(position), len(palette) - 2)
        fraction = position - start
        color = tuple(
            round(palette[start][channel] * (1 - fraction)
                  + palette[start + 1][channel] * fraction)
            for channel in range(3)
        )
        ramp_draw.line((pixel_x, 0, pixel_x, ramp_height), fill=color)
    image.paste(ramp, (ramp_left, ramp_top))
    draw.text((ramp_left, ramp_top + 14), "-1.0", fill=(20, 20, 20, 255), font=font)
    draw.text((ramp_left + 96, ramp_top + 14), "0", fill=(20, 20, 20, 255), font=font)
    draw.text((ramp_left + 185, ramp_top + 14), "+1.0", fill=(20, 20, 20, 255), font=font)


def _draw_attribution(image: Image.Image) -> None:
    draw = ImageDraw.Draw(image, "RGBA")
    font = ImageFont.load_default()
    line_width = max(24, (image.width - 24) // 6)
    text = "\n".join(
        textwrap.wrap(ESRI_WORLD_IMAGERY_ATTRIBUTION, width=line_width)
    )
    left, top, right, bottom = draw.multiline_textbbox(
        (0, 0), text, font=font, spacing=2, align="right"
    )
    text_width, text_height = right - left, bottom - top
    box_left = image.width - text_width - 18
    draw.rounded_rectangle(
        (box_left, 8, image.width - 8, text_height + 18),
        radius=4,
        fill=(255, 255, 255, 220),
    )
    draw.multiline_text(
        (box_left + 5, 11), text, fill=(20, 20, 20, 255),
        font=font, spacing=2, align="right",
    )


def _draw_geometry(image, geometry_geojson, zoom, view_left, view_top):
    draw = ImageDraw.Draw(image)
    for ring in geometry_geojson["coordinates"]:
        points = []
        for longitude, latitude, *_ in ring:
            pixel_x, pixel_y = _world_pixel(longitude, latitude, zoom)
            points.append((round(pixel_x - view_left), round(pixel_y - view_top)))
        draw.line(points, fill="#ff7800", width=3, joint="curve")


def render_static_index_map(
    index_image,
    index_name: str,
    geometry_geojson: dict,
    *,
    width: int = 1200,
    height: int = 800,
    http_get=None,
) -> StaticMapResult:
    """Compose Esri imagery with an Earth Engine index overlay in memory.

    Network and Earth Engine failures are returned as an explicit unavailable
    result so callers can retain the other index maps and report the failure.
    """
    normalized_index = index_name.upper() if isinstance(index_name, str) else ""
    if normalized_index not in INDEX_PALETTES:
        raise ValueError(f"Índice desconhecido: {index_name}")
    if (
        not isinstance(width, int)
        or not isinstance(height, int)
        or width < 256
        or height < 256
    ):
        raise ValueError("Dimensões do mapa devem ser inteiros de pelo menos 256 px")
    bounds = _geometry_bounds(geometry_geojson)
    zoom, view_left, view_top = _map_viewport(bounds, width, height)
    get = http_get or requests.get

    try:
        top_left_lon, top_left_lat = _world_lonlat(view_left, view_top, zoom)
        bottom_right_lon, bottom_right_lat = _world_lonlat(
            view_left + width, view_top + height, zoom
        )
        thumbnail_region = {
            "type": "Polygon",
            "coordinates": [[
                [top_left_lon, top_left_lat],
                [bottom_right_lon, top_left_lat],
                [bottom_right_lon, bottom_right_lat],
                [top_left_lon, bottom_right_lat],
                [top_left_lon, top_left_lat],
            ]],
        }
        clipped_image = index_image.select(normalized_index).clip(
            ee.Geometry(geometry_geojson)
        )
        visualized = clipped_image.visualize(
            min=-1,
            max=1,
            palette=INDEX_PALETTES[normalized_index],
            opacity=MAP_OVERLAY_OPACITY,
        )
        thumbnail_url = visualized.getThumbURL(
            {
                "region": thumbnail_region,
                "dimensions": f"{width}x{height}",
                "crs": "EPSG:3857",
                "format": "png",
            }
        )
        response = get(thumbnail_url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        overlay = Image.open(BytesIO(response.content))
        if "A" not in overlay.getbands():
            overlay.putalpha(round(255 * MAP_OVERLAY_OPACITY))
        overlay = overlay.convert("RGBA")
        if overlay.size != (width, height):
            overlay = overlay.resize((width, height), Image.Resampling.LANCZOS)

        satellite = _fetch_satellite(
            width, height, zoom, view_left, view_top, get
        )
        output = satellite.convert("RGBA")
        output.alpha_composite(overlay)
        _draw_geometry(output, geometry_geojson, zoom, view_left, view_top)
        _draw_legend(output, normalized_index)
        _draw_attribution(output)

        buffer = BytesIO()
        output.convert("RGB").save(buffer, format="PNG", optimize=True)
        return StaticMapResult(
            status="available",
            image_bytes=buffer.getvalue(),
            attribution=ESRI_WORLD_IMAGERY_ATTRIBUTION,
        )
    except Exception as error:
        logger.warning(
            "Static export map rendering failed for %s", normalized_index,
            exc_info=True,
        )
        return StaticMapResult(
            status="unavailable",
            image_bytes=None,
            attribution=ESRI_WORLD_IMAGERY_ATTRIBUTION,
            error=f"Não foi possível gerar o mapa {normalized_index}: {error}",
        )
