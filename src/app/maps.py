import math
import logging

import geemap
import ee
import folium
import requests
from folium.plugins import Draw

logger = logging.getLogger(__name__)


DEFAULT_CENTER = [-28.0, -52.0]
DEFAULT_ZOOM = 10
NOMINATIM_SEARCH_URL = "https://nominatim.openstreetmap.org/search"
NOMINATIM_TIMEOUT = 10
NOMINATIM_USER_AGENT = "monitoramento-agricola-satelite/1.0"

NDVI_PALETTE = ["blue", "white", "green"]
NDWI_PALETTE = ["brown", "white", "blue"]
NDMI_PALETTE = ["red", "yellow", "blue"]


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

    m = geemap.Map(center=center, zoom=zoom)
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
    palettes = {
        "NDVI": NDVI_PALETTE,
        "NDWI": NDWI_PALETTE,
        "NDMI": NDMI_PALETTE,
    }
    normalized_index = index_name.upper()
    if normalized_index not in palettes:
        raise ValueError(f"Índice desconhecido: {index_name}")

    thematic_map = create_base_map(center=center, zoom=zoom)
    palette = palettes[normalized_index]
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

    selection_map = folium.Map(location=center, zoom_start=zoom, control_scale=True)
    Draw(
        export=False,
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

    if geojson:
        folium.GeoJson(
            geojson,
            name="Área selecionada",
            style_function=lambda _: {
                "color": "#ff7800",
                "weight": 3,
                "fillColor": "#ff7800",
                "fillOpacity": 0.2,
            },
        ).add_to(selection_map)

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
