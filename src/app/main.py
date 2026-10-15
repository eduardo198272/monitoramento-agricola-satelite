import math
import logging

import streamlit as st
from datetime import date, timedelta
from streamlit_folium import st_folium

from src.app.config import APP_NAME, VERSION
from src.app.ee_auth import initialize_earth_engine
from src.app.maps import (
    enable_area_draw,
    create_selection_map,
    geojson_to_ee_geometry,
    search_location,
    calculate_map_zoom,
    calculate_area_context,
    DEFAULT_CENTER,
    DEFAULT_ZOOM,
    INDEX_PALETTES,
    get_index_map_tile_url,
    preload_index_values,
)
from src.app.map_interaction import render_index_hover_map
from src.app.anomalies import compute_trend
from src.app.styles import load_styles
from src.app.pipeline import run_analysis, run_multi_analysis

logger = logging.getLogger(__name__)

MAP_HEIGHT = 520
RESULTS_MAP_HEIGHT = 320

DEFAULT_START = date.today() - timedelta(days=365)
DEFAULT_END = date.today()
SUPPORTED_INDICES = ["NDVI", "NDWI", "NDMI"]
INDEX_SELECTION_OPTIONS = ["Todos", *SUPPORTED_INDICES]

UI_STATE_DEFAULTS = {
    "location_center": DEFAULT_CENTER,
    "location_zoom": DEFAULT_ZOOM,
    "location_result": None,
    "aoi_geojson": None,
    "aoi_geometry": None,
    "aoi_area_ha": None,
    "aoi_perimeter_km": None,
    "aoi_centroid": None,
    "analysis_mode": "single",
    "selected_indices": ["NDVI"],
    "visible_index": "NDVI",
    "analysis_results": {},
    "analysis_metadata": {},
    "analysis_status": "idle",
    "analysis_error": None,
    "analysis_map": None,
    "analysis_map_center": None,
    "index_value_grid": None,
    "index_preload_error": None,
    "index_tile_urls": {},
}


def initialize_ui_state() -> None:
    """Initialize the UI state without overwriting values during reruns."""
    for key, default in UI_STATE_DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = (
                default.copy() if isinstance(default, (list, dict)) else default
            )


def clear_analysis_state() -> None:
    """Clear results that no longer match the current area or request."""
    st.session_state.analysis_results = {}
    st.session_state.analysis_metadata = {}
    st.session_state.analysis_map = None
    st.session_state.analysis_map_center = None
    st.session_state.index_value_grid = None
    st.session_state.index_preload_error = None
    st.session_state.index_tile_urls = {}
    st.session_state.analysis_status = "idle"
    st.session_state.analysis_error = None


def clear_area_selection_state() -> None:
    """Clear the selected area and every value derived from it."""
    st.session_state.aoi_geojson = None
    st.session_state.aoi_geometry = None
    st.session_state.aoi_area_ha = None
    st.session_state.aoi_perimeter_km = None
    st.session_state.aoi_centroid = None
    clear_analysis_state()


def is_no_images_error(error: str) -> bool:
    """Recognize the pipeline's no-imagery response without matching case."""
    normalized_error = str(error or "").casefold()
    return "nenhuma imagem" in normalized_error or "no image" in normalized_error


def public_analysis_error(error: str) -> tuple[str, str]:
    """Return a stable UI status and a user-friendly message for a pipeline error."""
    if is_no_images_error(error):
        return (
            "no_data",
            "Nenhuma imagem Sentinel-2 disponível para o período e a área "
            "selecionados. Amplie o período ou revise a área e tente novamente.",
        )
    return (
        "error",
        "Não foi possível concluir a análise no Google Earth Engine. "
        "Verifique a conexão e a configuração do serviço e tente novamente.",
    )


@st.cache_resource
def init_earth_engine():
    try:
        initialize_earth_engine()
        return True, None
    except Exception as e:
        logger.exception("Earth Engine initialization failed")
        return False, str(e)


def display_map(map_obj) -> None:
    map_obj.to_streamlit(height=RESULTS_MAP_HEIGHT)


def render_analysis_map(index_image, index_name: str, geojson: dict | None):
    """Render the selected index using cached tile and pixel-grid data."""
    preloaded = st.session_state.index_value_grid
    index_grid = (preloaded or {}).get("indices", {}).get(index_name)
    if index_grid is None:
        st.error(
            st.session_state.index_preload_error
            or "Os valores do índice ainda não estão disponíveis no mapa."
        )
        return

    tile_urls = st.session_state.index_tile_urls
    if index_name not in tile_urls:
        tile_urls[index_name] = get_index_map_tile_url(
            index_image,
            index_name,
            st.session_state.aoi_geometry,
            index_grid["minimum"],
            index_grid["maximum"],
        )
    tile_url = tile_urls[index_name]
    return render_index_hover_map(
        tile_url=tile_url,
        center=st.session_state.analysis_map_center or DEFAULT_CENTER,
        zoom=12,
        geojson=geojson,
        index_name=index_name,
        palette=INDEX_PALETTES[index_name],
        value_grid=preloaded,
        key="thematic-index-map",
    )


def display_summary(
    index_name: str,
    mean_value: float,
    area_value: float,
    area_unit: str,
    trend: str,
) -> None:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Índice", value=index_name)
    with col2:
        st.metric(label="Valor Médio", value=f"{mean_value:.4f}")
    with col3:
        st.metric(label=f"Área ({area_unit})", value=f"{area_value:.2f}")

    trend_colors = {"crescente": "green", "estável": "blue", "decrescente": "red"}
    trend_color = trend_colors.get(trend.lower(), "gray")

    with col4:
        st.markdown(f"**Tendência:** :{trend_color}[{trend}]")


def display_anomaly_alert(alert: str | None) -> None:
    if alert:
        st.warning(alert)


def display_multi_index_overview(
    index_results: dict, image_count: int | None
) -> None:
    """Render real per-index metrics from a completed multi-index analysis."""
    st.subheader("Visão geral multiíndice")
    st.metric(
        label="Imagens analisadas",
        value=image_count if image_count is not None else "Indisponível",
    )

    columns = st.columns(len(index_results))
    for column, (index_name, result) in zip(columns, index_results.items()):
        mean_value = result.get("mean_value")
        mean_label = (
            f"{mean_value:.4f}"
            if isinstance(mean_value, (int, float)) and math.isfinite(mean_value)
            else "Indisponível"
        )
        time_series = result.get("time_series") or []
        trend = (
            result.get("trend") or compute_trend(time_series)
            if len(time_series) >= 2
            else "Indisponível"
        )

        with column:
            with st.container(border=True):
                st.markdown(f"**{index_name}**")
                st.metric(label="Valor médio", value=mean_label)
                st.metric(label="Tendência", value=trend)


def display_analysis_details(
    index_name: str, result: dict, climate_plot
) -> None:
    """Render time-series, anomaly, and shared climate details below the map."""
    st.subheader(f"Série Temporal de {index_name}")
    time_series_plot = result.get("time_series_plot")
    if time_series_plot is not None:
        st.plotly_chart(time_series_plot, use_container_width=True)
    else:
        st.info(f"Série temporal de {index_name} indisponível para este período.")

    st.subheader(f"Anomalias de {index_name}")
    anomalies = [
        point
        for point in result.get("anomalies", [])
        if point.get("anomaly", False)
    ]
    if anomalies:
        st.markdown("Possíveis variações observadas:")
        for point in anomalies:
            st.markdown(f"- {point['date']}: valor {point['value']:.4f}")
    else:
        st.info(f"Nenhuma anomalia detectada no {index_name} para este período.")

    st.subheader("Dados Climáticos (NASA POWER)")
    if climate_plot is not None:
        st.plotly_chart(climate_plot, use_container_width=True)
    else:
        st.info("Dados climáticos indisponíveis para este período.")

    climate_summary = result.get("climate_summary")
    if climate_summary is not None:
        has_summary = any(v is not None for v in climate_summary.values())
        if has_summary:
            st.markdown("**Resumo Climático**")
            col1, col2, col3 = st.columns(3)
            with col1:
                precip = climate_summary.get("total_precipitation_mm")
                if precip is not None:
                    st.metric("Precipitação total", f"{precip:.1f} mm")
                else:
                    st.metric("Precipitação total", "Indisponível")
            with col2:
                temp = climate_summary.get("mean_temperature_c")
                if temp is not None:
                    st.metric("Temperatura média", f"{temp:.1f} °C")
                else:
                    st.metric("Temperatura média", "Indisponível")
            with col3:
                rad = climate_summary.get("mean_solar_radiation_mj_m2_day")
                if rad is not None:
                    st.metric("Radiação solar média", f"{rad:.1f} MJ/m²/dia")
                else:
                    st.metric("Radiação solar média", "Indisponível")


def render_header_bar() -> None:
    with st.container(key="app-header"):
        _render_header_content()


def _render_header_content() -> None:
    """Render product identity and report Earth Engine errors only when needed."""
    st.title("Monitoramento Agrícola")
    st.caption(
        "Analise a condição da vegetação usando imagens de satélite e dados climáticos."
    )

    ee_ok, _ = init_earth_engine()
    if not ee_ok:
        st.error("Earth Engine indisponível", icon="❌")
        st.info(
            "Verifique as credenciais e a configuração da variável EE_PROJECT_ID. "
            "Tente novamente quando o serviço estiver disponível."
        )
        st.stop()


def render_controls_bar() -> tuple[bool, bool]:
    with st.container(key="controls-bar"):
        return _render_controls_content()


def _render_controls_content() -> tuple[bool, bool]:
    """Render compact controls bar: search | period | index | analyze.
    Returns (analyze_clicked, analysis_disabled).
    """
    col_search, col_period_start, col_period_end, col_index, col_analyze = st.columns(
        [2.6, 1.15, 1.15, 2.8, 1.3], vertical_alignment="center"
    )

    with col_search:
        with st.container(key="search-control"):
            search_col, btn_col = st.columns(
                [1, 0.16], vertical_alignment="center", gap="small"
            )
            with search_col:
                location_query = st.text_input(
                    "Localidade",
                    placeholder="Cidade, município...",
                    label_visibility="collapsed",
                    key="location_query",
                )
            with btn_col:
                search = st.button(
                    "🔍",
                    help="Pesquisar localidade",
                    key="search_location_button",
                    use_container_width=True,
                )

    with col_period_start:
        start_date = st.date_input(
            "Data inicial",
            value=DEFAULT_START,
            key="analysis_start_date",
            format="DD/MM/YYYY",
            label_visibility="collapsed",
        )

    with col_period_end:
        end_date = st.date_input(
            "Data final",
            value=DEFAULT_END,
            key="analysis_end_date",
            format="DD/MM/YYYY",
            label_visibility="collapsed",
        )

    with col_index:
        selected_index = st.radio(
            "Índice",
            options=INDEX_SELECTION_OPTIONS,
            index=1,
            horizontal=True,
            key="index_selection",
            label_visibility="collapsed",
        )
        st.session_state.analysis_mode = "multi" if selected_index == "Todos" else "single"
        st.session_state.selected_indices = (
            SUPPORTED_INDICES.copy()
            if selected_index == "Todos"
            else [selected_index]
        )

    with col_analyze:
        analysis_disabled = (
            st.session_state.aoi_geometry is None or end_date < start_date
        )
        analyze = st.button(
            "Analisar área",
            type="primary",
            use_container_width=True,
            disabled=analysis_disabled,
        )

    if search:
        if not location_query.strip():
            st.warning("Informe uma localidade para pesquisar.")
        else:
            try:
                location = search_location(location_query)
                if location is not None:
                    center = [location["latitude"], location["longitude"]]
                    zoom = calculate_map_zoom(location["boundingbox"])
            except Exception:
                logger.exception("Location search or map centering failed")
                st.warning(
                    "Localidade não encontrada ou serviço de geocodificação "
                    "indisponível. Confira o nome e tente novamente."
                )
            else:
                if location is None:
                    st.warning(
                        "Localidade não encontrada ou serviço de geocodificação "
                        "indisponível. Confira o nome e tente novamente."
                    )
                else:
                    st.session_state.location_center = center
                    st.session_state.location_zoom = zoom
                    st.session_state.location_result = location

    if st.session_state.location_result:
        st.success(
            f"Localidade encontrada: "
            f"{st.session_state.location_result['display_name']}"
        )

    if end_date < start_date:
        st.error("Data final não pode ser anterior à data inicial")

    return analyze, analysis_disabled


def render_selection_map_area() -> None:
    """Render the selection map and handle area drawing/editing."""
    st.subheader("Área de interesse")
    st.info("Use a ferramenta de polígono no mapa para desenhar a área de interesse.")
    selection_map = create_selection_map(
        center=st.session_state.location_center,
        zoom=st.session_state.location_zoom,
        geojson=st.session_state.aoi_geojson,
    )
    map_data = st_folium(
        selection_map,
        key="area_selection_map",
        height=MAP_HEIGHT,
        returned_objects=["last_active_drawing", "all_drawings"],
        use_container_width=True,
    )

    map_data = map_data or {}
    drawn_geojson = map_data.get("last_active_drawing")
    drawings_removed = (
        "all_drawings" in map_data
        and isinstance(map_data["all_drawings"], list)
        and not map_data["all_drawings"]
        and st.session_state.aoi_geojson is not None
    )
    if drawings_removed:
        clear_area_selection_state()
    elif drawn_geojson:
        try:
            if drawn_geojson != st.session_state.aoi_geojson:
                geometry = geojson_to_ee_geometry(drawn_geojson)
                context = calculate_area_context(geometry)
                st.session_state.aoi_geometry = geometry
                st.session_state.aoi_geojson = drawn_geojson
                st.session_state.aoi_area_ha = context["area_ha"]
                st.session_state.aoi_perimeter_km = context["perimeter_km"]
                st.session_state.aoi_centroid = context["centroid"]
                clear_analysis_state()
                # Re-evaluate the Analyze button against the freshly stored AOI.
                st.rerun()
            lat, lon = st.session_state.aoi_centroid
            st.success(
                f"Área selecionada: {st.session_state.aoi_area_ha:.2f} ha  |  "
                f"Perímetro: {st.session_state.aoi_perimeter_km:.2f} km  |  "
                f"Centroide: {lat:.4f}, {lon:.4f}"
            )
        except Exception as error:
            logger.exception("Failed to validate or calculate selected area")
            st.error(str(error))
    elif st.session_state.aoi_geometry is not None:
        area_ha = st.session_state.aoi_area_ha
        perimeter_km = st.session_state.aoi_perimeter_km
        centroid = st.session_state.aoi_centroid
        if area_ha is not None and perimeter_km is not None and centroid is not None:
            lat, lon = centroid
            st.success(
                f"Área selecionada: {area_ha:.2f} ha  |  "
                f"Perímetro: {perimeter_km:.2f} km  |  "
                f"Centroide: {lat:.4f}, {lon:.4f}"
            )
        else:
            st.success(
                f"Área selecionada: {area_ha:.2f} ha"
                if area_ha is not None
                else "Área selecionada."
            )


def render_results_panels() -> None:
    """Render results panels after successful analysis."""
    available_indices = list(st.session_state.analysis_results)
    if st.session_state.visible_index not in available_indices:
        st.session_state.visible_index = available_indices[0]
    if st.session_state.get("visible_index_control") not in available_indices:
        st.session_state.visible_index_control = st.session_state.visible_index

    st.radio(
        "Índice no mapa",
        options=available_indices,
        horizontal=True,
        key="visible_index_control",
    )
    st.session_state.visible_index = st.session_state.visible_index_control
    visible_index = st.session_state.visible_index
    res = st.session_state.analysis_results[visible_index]

    display_summary(
        visible_index,
        res["mean_value"],
        res.get("area_ha", st.session_state.analysis_metadata.get("area_ha")),
        "ha",
        compute_trend(res["time_series"]) if res["time_series"] else "estável",
    )

    display_anomaly_alert(res.get("alert"))

    if len(available_indices) > 1:
        display_multi_index_overview(
            st.session_state.analysis_results,
            st.session_state.analysis_metadata.get("image_count"),
        )

    climate_plot = res.get("climate_plot")
    if climate_plot is None:
        climate_plot = st.session_state.analysis_metadata.get("climate_plot")
    display_analysis_details(visible_index, res, climate_plot)


def render_results_map_area() -> bool:
    """Show the single dynamic map in place of the area-selection map."""
    available_indices = list(st.session_state.analysis_results)
    if not available_indices:
        return False
    if st.button("Alterar área", key="edit_analysis_area"):
        clear_analysis_state()
        return False
    selected = st.session_state.get("visible_index_control")
    visible_index = selected if selected in available_indices else available_indices[0]
    st.session_state.visible_index = visible_index
    st.subheader("Mapa do índice")
    try:
        render_analysis_map(
            st.session_state.analysis_results[visible_index]["index_map"],
            visible_index,
            st.session_state.aoi_geojson,
        )
    except Exception:
        logger.exception("Failed to render the interactive thematic map")
        st.error("Não foi possível carregar o mapa temático.")
    return True


def main():
    st.set_page_config(
        page_title="Monitoramento Agrícola por Imagens de Satélite",
        layout="wide",
    )
    load_styles()

    initialize_ui_state()

    render_header_bar()
    analyze, analysis_disabled = render_controls_bar()

    if analyze and not analysis_disabled:
        geometry = st.session_state.aoi_geometry
        start_date = st.session_state.analysis_start_date
        end_date = st.session_state.analysis_end_date

        if geometry is None:
            st.error("Desenhe uma área no mapa antes de analisar")
        else:
            st.session_state.analysis_status = "processing"
            st.session_state.analysis_error = None
            st.session_state.analysis_results = {}
            st.session_state.analysis_metadata = {}
            st.session_state.analysis_map = None
            st.session_state.index_tile_urls = {}
            st.session_state.index_value_grid = None
            st.session_state.index_preload_error = None
            selected_indices = st.session_state.selected_indices
            with st.spinner(
                "Buscando imagens Sentinel-2, aplicando máscara de nuvens "
                "e calculando os índices..."
            ):
                if st.session_state.analysis_mode == "multi":
                    result = run_multi_analysis(
                        geometry,
                        start_date,
                        end_date,
                        selected_indices,
                        area_ha=st.session_state.aoi_area_ha,
                    )
                else:
                    result = run_analysis(
                        geometry,
                        start_date,
                        end_date,
                        selected_indices[0],
                        area_ha=st.session_state.aoi_area_ha,
                    )

                if result["success"]:
                    st.session_state.aoi_area_ha = result.get("area_ha")
                    st.session_state.analysis_metadata = {
                        key: result[key]
                        for key in (
                            "area_ha",
                            "image_count",
                            "climate_data",
                            "climate_plot",
                        )
                        if key in result
                    }
                    if st.session_state.analysis_mode == "multi":
                        st.session_state.analysis_results = result["indices"]
                        st.session_state.visible_index = selected_indices[0]
                    else:
                        st.session_state.visible_index = selected_indices[0]
                        st.session_state.analysis_results = {st.session_state.visible_index: result}
                    st.session_state.analysis_map_center = (
                        result.get("map_center")
                        or st.session_state.aoi_centroid
                        or st.session_state.location_center
                    )
                    try:
                        st.session_state.index_value_grid = preload_index_values(
                            {
                                name: index_result["index_map"]
                                for name, index_result
                                in st.session_state.analysis_results.items()
                            },
                            geometry,
                            st.session_state.analysis_map_center,
                            scale=10,
                        )
                    except Exception as preload_error:
                        logger.exception("Failed to preload index pixel values")
                        st.session_state.index_preload_error = str(preload_error)
                    st.session_state.analysis_status = "success"
                    st.session_state.analysis_error = None
                else:
                    status, message = public_analysis_error(result.get("error"))
                    st.session_state.analysis_error = message
                    st.session_state.analysis_map = None
                    st.session_state.analysis_results = {}
                    st.session_state.analysis_metadata = {}
                    st.session_state.analysis_status = status

    has_result_maps = bool(st.session_state.analysis_results) and all(
        "index_map" in value for value in st.session_state.analysis_results.values()
    )
    if st.session_state.analysis_status == "success" and has_result_maps:
        if render_results_map_area():
            render_results_panels()
        else:
            render_selection_map_area()
    else:
        render_selection_map_area()

    if st.session_state.analysis_status == "no_data":
        st.warning(st.session_state.analysis_error)
    elif st.session_state.analysis_status == "error":
        st.error(st.session_state.analysis_error)


if __name__ == "__main__":
    main()
