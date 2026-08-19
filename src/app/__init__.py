"""Application package for agricultural monitoring."""

from src.app.earth_engine import (
    filter_by_date,
    filter_by_area,
    get_image_collection,
    mask_clouds,
    calculate_ndvi,
    calculate_ndwi,
    calculate_ndmi,
)

from src.app.maps import (
    create_base_map,
    add_index_layer,
    add_colorbar,
    enable_area_draw,
    get_drawn_geometry,
    get_predefined_areas,
    load_predefined_area,
)

from src.app.time_series import (
    compute_time_series,
    plot_time_series,
)

from src.app.anomalies import (
    detect_anomalies,
    generate_alert,
    compute_trend,
)

__all__ = [
    "filter_by_date",
    "filter_by_area",
    "get_image_collection",
    "mask_clouds",
    "calculate_ndvi",
    "calculate_ndwi",
    "calculate_ndmi",
    "create_base_map",
    "add_index_layer",
    "add_colorbar",
    "enable_area_draw",
    "get_drawn_geometry",
    "get_predefined_areas",
    "load_predefined_area",
    "compute_time_series",
    "plot_time_series",
    "detect_anomalies",
    "generate_alert",
    "compute_trend",
]