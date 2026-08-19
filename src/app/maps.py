import geemap
import ee


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
    m.add_scale_bar()
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


PREDEFINED_AREAS = {
    "Talhão A": ee.Geometry.Polygon([[
        [-52.1, -28.0],
        [-52.05, -28.0],
        [-52.05, -28.05],
        [-52.1, -28.05],
        [-52.1, -28.0]
    ]]),
    "Talhão B": ee.Geometry.Polygon([[
        [-52.2, -28.1],
        [-52.15, -28.1],
        [-52.15, -28.15],
        [-52.2, -28.15],
        [-52.2, -28.1]
    ]]),
    "Talhão C": ee.Geometry.Polygon([[
        [-52.3, -27.9],
        [-52.25, -27.9],
        [-52.25, -27.95],
        [-52.3, -27.95],
        [-52.3, -27.9]
    ]]),
}


def get_predefined_areas() -> list[dict]:
    return [
        {"name": name, "geometry": geom}
        for name, geom in PREDEFINED_AREAS.items()
    ]


def load_predefined_area(area_name: str) -> ee.Geometry | None:
    import unicodedata
    
    def normalize(s: str) -> str:
        return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()
    
    normalized_input = normalize(area_name)
    for name, geom in PREDEFINED_AREAS.items():
        if normalize(name) == normalized_input:
            return geom
    return None


def enable_area_draw(map_obj: geemap.Map, draw_type: str = "polygon") -> None:
    if draw_type not in ("polygon", "rectangle"):
        raise ValueError("draw_type deve ser 'polygon' ou 'rectangle'")

    map_obj.add_draw_control()
    if draw_type == "rectangle":
        map_obj.draw_control.rectangle = True
        map_obj.draw_control.polygon = False
    else:
        map_obj.draw_control.rectangle = False
        map_obj.draw_control.polygon = True


def get_drawn_geometry(map_obj: geemap.Map) -> ee.Geometry | None:
    if not hasattr(map_obj, "draw_last_feature") or map_obj.draw_last_feature is None:
        return None

    try:
        geom = map_obj.draw_last_feature.geometry()
        return ee.Geometry(geom)
    except Exception:
        return None