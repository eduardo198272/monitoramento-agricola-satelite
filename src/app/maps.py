import geemap
import ee
import folium
from folium.plugins import Draw


DEFAULT_CENTER = [-28.0, -52.0]
DEFAULT_ZOOM = 10

NDVI_PALETTE = ["blue", "white", "green"]
NDWI_PALETTE = ["brown", "white", "blue"]
NDMI_PALETTE = ["red", "yellow", "blue"]


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
    opacity: float = 0.7
) -> geemap.Map:
    if index_name.upper() == "NDVI":
        if palette is None:
            palette = NDVI_PALETTE
        if not index_image.bandNames().contains("NDVI").getInfo():
            raise ValueError("Imagem não contém banda NDVI")
    elif index_name.upper() == "NDWI":
        if palette is None:
            palette = NDWI_PALETTE
        if not index_image.bandNames().contains("NDWI").getInfo():
            raise ValueError("Imagem não contém banda NDWI")
    elif index_name.upper() == "NDMI":
        if palette is None:
            palette = NDMI_PALETTE
        if not index_image.bandNames().contains("NDMI").getInfo():
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
    geometry_type = geometry.get("type")
    coordinates = geometry.get("coordinates")

    if geometry_type != "Polygon" or not coordinates:
        raise ValueError("Desenhe uma área usando um polígono")

    if len(coordinates[0]) < 4:
        raise ValueError("O polígono precisa ter pelo menos três vértices")

    return ee.Geometry.Polygon(coordinates)


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
