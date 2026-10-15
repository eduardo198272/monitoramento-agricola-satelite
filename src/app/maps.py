import math
import logging
import base64
import uuid
import zlib

import geemap
import ee
import folium
import numpy as np
import requests
from folium.plugins import Draw

logger = logging.getLogger(__name__)


DEFAULT_CENTER = [-28.0, -52.0]
DEFAULT_ZOOM = 10
ESRI_WORLD_IMAGERY_URL = (
    "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/"
    "MapServer/tile/{z}/{y}/{x}"
)
ESRI_WORLD_IMAGERY_ATTRIBUTION = (
    "Tiles © Esri — Source: Esri, Maxar, Earthstar Geographics, "
    "and the GIS User Community"
)
NOMINATIM_SEARCH_URL = "https://nominatim.openstreetmap.org/search"
NOMINATIM_TIMEOUT = 10
NOMINATIM_USER_AGENT = "monitoramento-agricola-satelite/1.0"

NDVI_PALETTE = ["#f7fcf5", "#74c476", "#00441b"]
NDWI_PALETTE = ["#f7fbff", "#6baed6", "#08306b"]
NDMI_PALETTE = ["#fff5eb", "#fd8d3c", "#7f2704"]
INDEX_PALETTES = {
    "NDVI": NDVI_PALETTE,
    "NDWI": NDWI_PALETTE,
    "NDMI": NDMI_PALETTE,
}
INDEX_PRELOAD_SCALE_METERS = 10
MAX_PRELOADED_VALUES = 2_000_000
INDEX_NODATA = -9999.0


def search_location(query: str) -> dict | None:
    """Search for a location using the Nominatim geocoding service."""
    normalized_query = " ".join(query.split())
    if not normalized_query:
        return None

    try:
        response = requests.get(
            NOMINATIM_SEARCH_URL,
            params={"q": normalized_query, "format": "jsonv2", "limit": 1},
            headers={"User-Agent": NOMINATIM_USER_AGENT},
            timeout=NOMINATIM_TIMEOUT,
        )
        response.raise_for_status()
        results = response.json()

        if not results:
            return None

        location = results[0]
        return {
            "display_name": location["display_name"],
            "latitude": float(location["lat"]),
            "longitude": float(location["lon"]),
            "boundingbox": location["boundingbox"],
        }
    except (
        requests.exceptions.RequestException,
        ValueError,
        TypeError,
        KeyError,
        IndexError,
    ):
        logger.warning(
            "Location geocoding request failed or returned invalid data",
            exc_info=True,
        )
        return None


def calculate_map_zoom(boundingbox: list[str]) -> int:
    """Calculate a map zoom level from a Nominatim bounding box."""
    if not isinstance(boundingbox, (list, tuple)) or len(boundingbox) != 4:
        raise ValueError("boundingbox deve conter quatro limites")

    try:
        south, north, west, east = (float(value) for value in boundingbox)
    except (TypeError, ValueError):
        raise ValueError("boundingbox deve conter valores numéricos") from None

    if not all(math.isfinite(value) for value in (south, north, west, east)):
        raise ValueError("boundingbox deve conter valores finitos")
    if south > north or west > east:
        raise ValueError("boundingbox possui limites inválidos")

    extent = max(north - south, east - west)
    if extent == 0:
        return 20

    zoom = round(math.log2(360 / extent))
    return max(1, min(20, zoom))


def create_base_map(center: list = None, zoom: int = DEFAULT_ZOOM) -> geemap.Map:
    if center is None:
        center = DEFAULT_CENTER
    if not isinstance(zoom, int) or zoom < 1 or zoom > 20:
        raise ValueError("zoom deve ser inteiro entre 1 e 20")

    m = geemap.Map(center=center, zoom=zoom, basemap="Esri.WorldImagery")
    m.add_layer_control()
    return m


def add_index_layer(
    map_obj: geemap.Map,
    index_image: ee.Image,
    index_name: str,
    palette: list = None,
    opacity: float = 0.7,
    validate_band: bool = True,
) -> geemap.Map:
    if index_name.upper() == "NDVI":
        if palette is None:
            palette = NDVI_PALETTE
        if validate_band and not index_image.bandNames().contains("NDVI").getInfo():
            raise ValueError("Imagem não contém banda NDVI")
    elif index_name.upper() == "NDWI":
        if palette is None:
            palette = NDWI_PALETTE
        if validate_band and not index_image.bandNames().contains("NDWI").getInfo():
            raise ValueError("Imagem não contém banda NDWI")
    elif index_name.upper() == "NDMI":
        if palette is None:
            palette = NDMI_PALETTE
        if validate_band and not index_image.bandNames().contains("NDMI").getInfo():
            raise ValueError("Imagem não contém banda NDMI")
    else:
        raise ValueError(f"Índice desconhecido: {index_name}")

    vis_params = {
        "min": -1,
        "max": 1,
        "palette": palette,
        "opacity": opacity
    }
    map_obj.addLayer(index_image, vis_params, index_name)
    return map_obj


def create_thematic_map(
    index_image: ee.Image,
    index_name: str,
    center: list = None,
    zoom: int = DEFAULT_ZOOM,
    geojson: dict = None,
) -> geemap.Map:
    """Create a thematic map from an already-computed index image."""
    normalized_index = index_name.upper()
    if normalized_index not in INDEX_PALETTES:
        raise ValueError(f"Índice desconhecido: {index_name}")

    thematic_map = create_base_map(center=center, zoom=zoom)
    palette = INDEX_PALETTES[normalized_index]
    add_index_layer(
        thematic_map,
        index_image,
        normalized_index,
        palette=palette,
        validate_band=False,
    )
    add_colorbar(thematic_map, palette, normalized_index)

    if geojson:
        thematic_map.add_geojson(
            geojson,
            layer_name="Área selecionada",
            style={"color": "#ff7800", "weight": 3, "fillOpacity": 0},
        )

    return thematic_map


def get_index_map_tile_url(
    index_image: ee.Image,
    index_name: str,
    geometry: ee.Geometry,
    min_value: float = -1,
    max_value: float = 1,
) -> str:
    """Create authenticated, AOI-clipped map tiles with a data-driven range."""
    normalized_index = index_name.upper()
    if normalized_index not in INDEX_PALETTES:
        raise ValueError(f"Índice desconhecido: {index_name}")

    if not math.isfinite(min_value) or not math.isfinite(max_value) or min_value >= max_value:
        min_value, max_value = -1, 1
    clipped_image = index_image.select(normalized_index).clip(geometry)
    map_id = clipped_image.getMapId(
        {
            "min": min_value,
            "max": max_value,
            "palette": INDEX_PALETTES[normalized_index],
        }
    )
    tile_fetcher = map_id.get("tile_fetcher")
    tile_url = getattr(tile_fetcher, "url_format", None)
    if not tile_url:
        raise ValueError("Earth Engine não retornou uma URL para os tiles do índice")
    return tile_url


def _utm_epsg(center: list[float]) -> int:
    latitude, longitude = center
    zone = max(1, min(60, int((longitude + 180) // 6) + 1))
    return (32700 if latitude < 0 else 32600) + zone


def _pack_float_grid(values: list) -> str:
    array = np.asarray(values, dtype="<f4")
    return base64.b64encode(zlib.compress(array.tobytes())).decode("ascii")


def preload_index_values(
    index_images: dict[str, ee.Image],
    geometry: ee.Geometry,
    center: list[float],
    scale: int = INDEX_PRELOAD_SCALE_METERS,
) -> dict:
    """Fetch clipped index pixels once and pack them for browser-local lookup."""
    if not index_images:
        raise ValueError("Nenhum índice foi selecionado para pré-carregamento")
    if not isinstance(scale, int) or scale <= 0:
        raise ValueError("A escala de pré-carregamento deve ser um inteiro positivo")

    epsg = _utm_epsg(center)
    projection = ee.Projection(f"EPSG:{epsg}").atScale(scale)
    projection_info = projection.getInfo()
    transform = projection_info.get("transform")
    if not transform or len(transform) != 6:
        raise ValueError("Não foi possível determinar a grade espacial do raster")

    region = geometry.bounds(1, projection)
    bounds = region.coordinates().getInfo()
    ring = bounds
    while (
        isinstance(ring, (list, tuple))
        and ring
        and isinstance(ring[0], (list, tuple))
        and ring[0]
        and isinstance(ring[0][0], (list, tuple))
    ):
        ring = ring[0]
    if (
        not isinstance(ring, (list, tuple))
        or not ring
        or any(
            not isinstance(point, (list, tuple))
            or len(point) < 2
            or not all(isinstance(value, (int, float)) for value in point[:2])
            for point in ring
        )
    ):
        raise ValueError("A área selecionada não possui uma extensão válida")
    min_x = min(point[0] for point in ring)
    max_x = max(point[0] for point in ring)
    min_y = min(point[1] for point in ring)
    max_y = max(point[1] for point in ring)
    estimated_columns = math.ceil((max_x - min_x) / scale) + 2
    estimated_rows = math.ceil((max_y - min_y) / scale) + 2
    estimated_values = estimated_columns * estimated_rows * (len(index_images) + 2)
    if estimated_values > MAX_PRELOADED_VALUES:
        raise ValueError(
            "A área é grande demais para pré-carregar todos os pixels em 10 m. "
            "Reduza a área ou selecione menos índices."
        )

    names = list(index_images)
    projected = [
        index_images[name]
        .select(name)
        .reproject(projection)
        .clip(geometry)
        .rename(name)
        .toFloat()
        for name in names
    ]
    image_stack = projected[0]
    for band in projected[1:]:
        image_stack = image_stack.addBands(band)
    pixel_coordinates = ee.Image.pixelCoordinates(projection).rename(
        ["grid_x", "grid_y"]
    )
    image_stack = image_stack.addBands(pixel_coordinates)
    sampled = image_stack.sampleRectangle(
        region=region,
        defaultValue=INDEX_NODATA,
    ).getInfo()
    properties = sampled.get("properties", {})
    grid_x = np.asarray(properties.get("grid_x", []))
    grid_y = np.asarray(properties.get("grid_y", []))
    if (
        grid_x.ndim != 2
        or grid_y.ndim != 2
        or grid_x.size == 0
        or grid_y.size == 0
        or grid_x.shape != grid_y.shape
    ):
        raise ValueError("O pré-carregamento não retornou pixels para a área")

    values_by_index = {}
    total_values = 0
    for name in names:
        pixels = np.asarray(properties.get(name, []), dtype=np.float32)
        if pixels.ndim != 2 or pixels.size == 0 or pixels.shape != grid_x.shape:
            raise ValueError(f"Não foi possível carregar os pixels de {name}")
        total_values += pixels.size
        if total_values > MAX_PRELOADED_VALUES:
            raise ValueError(
                "A área é grande demais para pré-carregar todos os pixels em 10 m. "
                "Reduza a área ou selecione menos índices."
            )
        valid = pixels[np.isfinite(pixels) & (pixels != INDEX_NODATA)]
        if valid.size:
            minimum = float(valid.min())
            maximum = float(valid.max())
            if math.isclose(minimum, maximum):
                minimum = max(-1.0, minimum - 0.01)
                maximum = min(1.0, maximum + 0.01)
        else:
            minimum, maximum = -1.0, 1.0
        values_by_index[name] = {
            "values": _pack_float_grid(pixels),
            "rows": int(pixels.shape[0]),
            "columns": int(pixels.shape[1]),
            "minimum": minimum,
            "maximum": maximum,
        }

    return {
        "analysis_key": uuid.uuid4().hex,
        "crs": f"EPSG:{epsg}",
        "transform": transform,
        "first_column": int(grid_x.flat[0]),
        "first_row": int(grid_y.flat[0]),
        "scale": scale,
        "nodata": INDEX_NODATA,
        "indices": values_by_index,
    }


def add_colorbar(
    map_obj: geemap.Map,
    palette: list,
    index_name: str,
    min_val: float = -1,
    max_val: float = 1
) -> None:
    map_obj.add_colorbar(
        vis_params={"min": min_val, "max": max_val, "palette": palette},
        label=index_name,
        position="bottomright"
    )


def create_selection_map(
    center: list = None,
    zoom: int = DEFAULT_ZOOM,
    geojson: dict = None,
) -> folium.Map:
    """Create the interactive map used to select the area of interest."""
    if center is None:
        center = DEFAULT_CENTER
    if not isinstance(zoom, int) or zoom < 1 or zoom > 20:
        raise ValueError("zoom deve ser inteiro entre 1 e 20")

    selection_map = folium.Map(
        location=center,
        zoom_start=zoom,
        control_scale=True,
        tiles=None,
    )
    folium.TileLayer(
        tiles=ESRI_WORLD_IMAGERY_URL,
        attr=ESRI_WORLD_IMAGERY_ATTRIBUTION,
        name="Satélite (Esri)",
        overlay=False,
        control=True,
    ).add_to(selection_map)
    drawn_items = folium.FeatureGroup(name="Área selecionada", show=True)
    drawn_items.add_to(selection_map)

    if geojson:
        folium.GeoJson(
            geojson,
            name="Geometria da área",
            style_function=lambda _: {
                "color": "#ff7800",
                "weight": 3,
                "fillColor": "#ff7800",
                "fillOpacity": 0.2,
            },
        ).add_to(drawn_items)

    Draw(
        export=False,
        feature_group=drawn_items,
        draw_options={
            "polyline": False,
            "rectangle": False,
            "circle": False,
            "marker": False,
            "circlemarker": False,
            "polygon": True,
        },
        edit_options={"edit": True, "remove": True},
    ).add_to(selection_map)
    folium.LayerControl(collapsed=True).add_to(selection_map)

    return selection_map


def geojson_to_ee_geometry(geojson: dict) -> ee.Geometry:
    """Convert a drawn GeoJSON geometry into an Earth Engine geometry."""
    if not isinstance(geojson, dict):
        raise ValueError("A área desenhada não possui um formato GeoJSON válido")

    geometry = geojson.get("geometry", geojson)
    if not isinstance(geometry, dict):
        raise ValueError("A geometria GeoJSON está malformada")
    geometry_type = geometry.get("type")
    coordinates = geometry.get("coordinates")

    if geometry_type != "Polygon" or not coordinates:
        raise ValueError("Desenhe uma área usando um polígono")

    if not isinstance(coordinates, (list, tuple)) or not coordinates:
        raise ValueError("O polígono precisa conter pelo menos um anel válido")

    for ring in coordinates:
        _validate_polygon_ring(ring)

    return ee.Geometry.Polygon(coordinates)


def _validate_polygon_ring(ring: list) -> None:
    if not isinstance(ring, (list, tuple)):
        raise ValueError("O anel do polígono está malformado")

    try:
        points = [tuple(point) for point in ring]
    except (TypeError, ValueError):
        raise ValueError("As coordenadas do polígono estão malformadas") from None

    if any(
        len(point) < 2
        or not all(isinstance(value, (int, float)) and math.isfinite(value) for value in point[:2])
        or not -180 <= point[0] <= 180
        or not -90 <= point[1] <= 90
        for point in points
    ):
        raise ValueError("As coordenadas devem ser finitas e estar dentro dos limites geográficos")

    if len(points) < 4 or points[0] != points[-1]:
        raise ValueError("O polígono deve ter pelo menos três vértices distintos e um anel fechado")

    vertices = points[:-1]
    if len(set(vertices)) < 3:
        raise ValueError("O polígono deve ter pelo menos três vértices distintos")

    signed_area = sum(
        x1 * y2 - x2 * y1
        for (x1, y1), (x2, y2) in zip(points, points[1:])
    )
    if math.isclose(signed_area, 0.0, abs_tol=1e-12):
        raise ValueError("O polígono não pode ter área zero")

    if _ring_has_self_intersection(vertices):
        raise ValueError("O polígono é inválido: seus lados não podem se cruzar")


def _ring_has_self_intersection(vertices: list[tuple]) -> bool:
    def orientation(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    def intersects(a, b, c, d):
        return (
            orientation(a, b, c) * orientation(a, b, d) < 0
            and orientation(c, d, a) * orientation(c, d, b) < 0
        )

    count = len(vertices)
    for first in range(count):
        a, b = vertices[first], vertices[(first + 1) % count]
        for second in range(first + 1, count):
            if second == first or second == (first + 1) % count or (second + 1) % count == first:
                continue
            c, d = vertices[second], vertices[(second + 1) % count]
            if intersects(a, b, c, d):
                return True
    return False


def enable_area_draw(map_obj: geemap.Map) -> None:
    map_obj.add_draw_control_lite()


def get_drawn_geometry(map_obj: geemap.Map) -> ee.Geometry | None:
    if not hasattr(map_obj, "draw_last_feature") or map_obj.draw_last_feature is None:
        return None

    try:
        geom = map_obj.draw_last_feature.geometry()
        return ee.Geometry(geom)
    except Exception:
        return None


def calculate_area_context(geometry: ee.Geometry) -> dict:
    """
    Calculate area (ha), perimeter (km), and centroid (lat, lon) from an EE geometry.

    Args:
        geometry: Earth Engine geometry object.

    Returns:
        Dictionary with keys "area_ha", "perimeter_km", "centroid" (tuple of lat, lon).

    Raises:
        ValueError: If geometry is invalid or metrics are not finite/positive.
    """
    if geometry is None:
        raise ValueError("Geometria inválida: None")

    try:
        area_m2 = geometry.area().getInfo()
        perimeter_m = geometry.perimeter().getInfo()
        centroid_coords = geometry.centroid().coordinates().getInfo()

        if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in (area_m2, perimeter_m)):
            raise ValueError("Área ou perímetro não são valores finitos válidos")

        if area_m2 <= 0:
            raise ValueError("Não foi possível calcular uma área válida em hectares (área <= 0)")

        if perimeter_m <= 0:
            raise ValueError("Não foi possível calcular um perímetro válido em km (perímetro <= 0)")

        if not (isinstance(centroid_coords, (list, tuple)) and len(centroid_coords) == 2):
            raise ValueError("Centroide inválido: coordenadas ausentes ou malformadas")

        lon, lat = centroid_coords
        if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in (lon, lat)):
            raise ValueError("Centroide contém valores não finitos")

        return {
            "area_ha": area_m2 / 10000.0,
            "perimeter_km": perimeter_m / 1000.0,
            "centroid": (lat, lon),
        }

    except ValueError:
        raise
    except Exception as e:
        raise ValueError(f"Falha ao calcular contexto geográfico: {e}") from e
