"""Interactive Leaflet map component for sampling Earth Engine index pixels."""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


_COMPONENT_DIR = Path(__file__).with_name("assets") / "index_hover"
_index_hover_component = components.declare_component(
    "index_pixel_hover", path=str(_COMPONENT_DIR)
)


def render_index_hover_map(
    *,
    tile_url: str,
    center: list[float],
    zoom: int,
    geojson: dict | None,
    index_name: str,
    palette: list[str],
    value_grid: dict,
    key: str,
    height: int = 320,
) -> dict | None:
    """Render the map; all cursor reads happen from the preloaded browser grid."""
    return _index_hover_component(
        tile_url=tile_url,
        center=center,
        zoom=zoom,
        geojson=geojson,
        index_name=index_name,
        palette=palette,
        value_grid=value_grid,
        key=key,
        default=None,
        width="stretch",
        height=height,
    )
