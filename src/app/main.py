import math

import streamlit as st
from datetime import date, timedelta
from streamlit_folium import st_folium

from src.app.config import APP_NAME, VERSION
from src.app.ee_auth import initialize_earth_engine
from src.app.maps import (
    create_base_map,
    add_index_layer,
    add_colorbar,
    enable_area_draw,
    create_selection_map,
    geojson_to_ee_geometry,
    search_location,
    calculate_map_zoom,
    DEFAULT_CENTER,
    DEFAULT_ZOOM,
)
from src.app.anomalies import compute_trend
from src.app.styles import load_styles
from src.app.pipeline import run_analysis, run_multi_analysis

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
    "analysis_mode": "single",
    "selected_indices": ["NDVI"],
    "visible_index": "NDVI",
    "analysis_results": {},
    "analysis_metadata": {},
    "analysis_status": "idle",
    "analysis_error": None,
    "analysis_map": None,
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
    st.session_state.analysis_status = "idle"
    st.session_state.analysis_error = None


def clear_area_selection_state() -> None:
    """Clear the selected area and every value derived from it."""
    st.session_state.aoi_geojson = None
    st.session_state.aoi_geometry = None
    st.session_state.aoi_area_ha = None
    clear_analysis_state()


@st.cache_resource
def init_earth_engine():
    try:
        initialize_earth_engine()
        return True, None
    except Exception as e:
        return False, str(e)


def display_map(map_obj) -> None:
    map_obj.to_streamlit(height=600)


def display_summary(
    index_name: str,
    mean_value: float,
    area_ha: float,
    trend: str,
    alert: str = None
) -> None:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Índice", value=index_name)
    with col2:
        st.metric(label="Valor Médio", value=f"{mean_value:.4f}")
    with col3:
        st.metric(label="Área (ha)", value=f"{area_ha:.2f}")

    trend_colors = {"crescente": "green", "estável": "blue", "decrescente": "red"}
    trend_color = trend_colors.get(trend.lower(), "gray")

    with col4:
        st.markdown(f"**Tendência:** :{trend_color}[{trend}]")

    if alert:
        alert_color = "red" if alert.lower() != "normal" else "green"
        st.markdown(f"**Alerta:** :{alert_color}[{alert}]")


def main():
    st.set_page_config(
        page_title="Monitoramento Agrícola por Imagens de Satélite",
        layout="wide"
    )
    load_styles()

    st.title("Monitoramento Agrícola")
    st.caption("Analise a condição da vegetação usando imagens de satélite e dados climáticos.")

    initialize_ui_state()

    ee_ok, ee_error = init_earth_engine()
    if not ee_ok:
        st.error("Status do serviço: Earth Engine indisponível")
        st.error(f"Erro ao inicializar Earth Engine: {ee_error}")
        st.info("Configure a variável EE_PROJECT_ID no arquivo .env")
        return

    st.success("Status do serviço: Earth Engine conectado")

    st.subheader("Localizar área")
    search_col, search_button_col = st.columns([4, 1])
    with search_col:
        location_query = st.text_input(
            "Pesquisar localidade",
            key="location_query",
            placeholder="Cidade, município ou endereço",
        )
    with search_button_col:
        st.write("")
        search = st.button("Pesquisar")

    if search:
        if not location_query.strip():
            st.warning("Informe uma localidade para pesquisar.")
        else:
            try:
                location = search_location(location_query)
                if location is None:
                    raise ValueError("Localidade não encontrada")
                center = [location["latitude"], location["longitude"]]
                zoom = calculate_map_zoom(location["boundingbox"])
            except Exception:
                st.warning("Localidade não encontrada ou serviço indisponível.")
            else:
                st.session_state.location_center = center
                st.session_state.location_zoom = zoom
                st.session_state.location_result = location

    if st.session_state.location_result:
        st.success(
            f"Localidade encontrada: "
            f"{st.session_state.location_result['display_name']}"
        )

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
        height=600,
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
                area_ha = geometry.area().divide(10000).getInfo()
                if (
                    not isinstance(area_ha, (int, float))
                    or not math.isfinite(area_ha)
                    or area_ha <= 0
                ):
                    raise ValueError("Não foi possível calcular uma área válida em hectares.")
                st.session_state.aoi_geometry = geometry
                st.session_state.aoi_geojson = drawn_geojson
                st.session_state.aoi_area_ha = area_ha
                clear_analysis_state()
            st.success(f"Área selecionada: {st.session_state.aoi_area_ha:.2f} ha")
        except Exception as error:
            st.error(str(error))
    elif st.session_state.aoi_geometry is not None:
        area_ha = st.session_state.aoi_area_ha
        st.success(
            f"Área selecionada: {area_ha:.2f} ha"
            if area_ha is not None
            else "Área selecionada."
        )

    with st.container(border=True):
        st.caption("Período da análise")
        date_start_col, date_end_col = st.columns(2)
        with date_start_col:
            start_date = st.date_input(
                "Data inicial",
                value=DEFAULT_START,
                key="analysis_start_date",
                format="DD/MM/YYYY",
            )
        with date_end_col:
            end_date = st.date_input(
                "Data final",
                value=DEFAULT_END,
                key="analysis_end_date",
                format="DD/MM/YYYY",
            )

    st.subheader("Configurar análise")
    selected_index = st.radio(
        "Índice",
        options=INDEX_SELECTION_OPTIONS,
        index=INDEX_SELECTION_OPTIONS.index("NDVI"),
        horizontal=True,
        key="index_selection",
    )
    st.session_state.analysis_mode = "multi" if selected_index == "Todos" else "single"
    st.session_state.selected_indices = (
        SUPPORTED_INDICES.copy()
        if selected_index == "Todos"
        else [selected_index]
    )
    index_name = (
        selected_index
        if selected_index in SUPPORTED_INDICES
        else st.session_state.visible_index
    )

    if end_date < start_date:
        st.error("Data final não pode ser anterior à data inicial")

    analysis_disabled = (
        st.session_state.aoi_geometry is None or end_date < start_date
    )
    analyze = st.button("Analisar área", disabled=analysis_disabled)

    if analyze and end_date >= start_date:
        geometry = st.session_state.aoi_geometry

        if geometry is None:
            st.error("Desenhe uma área no mapa antes de analisar")
        else:
            st.session_state.analysis_status = "processing"
            st.session_state.analysis_error = None
            st.session_state.analysis_results = {}
            st.session_state.analysis_metadata = {}
            st.session_state.analysis_map = None
            selected_indices = st.session_state.selected_indices
            with st.spinner("Processando..."):
                if st.session_state.analysis_mode == "multi":
                    result = run_multi_analysis(
                        geometry, start_date, end_date, selected_indices
                    )
                else:
                    result = run_analysis(
                        geometry, start_date, end_date, selected_indices[0]
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
                        st.session_state.analysis_results = {index_name: result}
                        st.session_state.visible_index = index_name
                        m = create_base_map(
                            center=[geometry.centroid().coordinates().getInfo()[1],
                                    geometry.centroid().coordinates().getInfo()[0]],
                            zoom=12
                        )
                        if index_name == "NDVI":
                            palette = ["blue", "white", "green"]
                        elif index_name == "NDWI":
                            palette = ["brown", "white", "blue"]
                        else:
                            palette = ["red", "yellow", "blue"]

                        m = add_index_layer(
                            m, result["index_map"], index_name, palette=palette
                        )
                        add_colorbar(m, palette, index_name)
                        st.session_state.analysis_map = m
                    st.session_state.analysis_status = "success"
                    st.session_state.analysis_error = None
                else:
                    st.session_state.analysis_error = result["error"]
                    st.session_state.analysis_map = None
                    st.session_state.analysis_results = {}
                    st.session_state.analysis_metadata = {}
                    st.session_state.analysis_status = (
                        "no_data"
                        if "Nenhuma imagem" in result["error"]
                        else "error"
                    )

    if st.session_state.analysis_error:
        st.error(st.session_state.analysis_error)
    elif st.session_state.analysis_map and st.session_state.analysis_results:
        res = st.session_state.analysis_results[st.session_state.visible_index]

        display_map(st.session_state.analysis_map)
        display_summary(
            res.get("index_name", index_name),
            res["mean_value"],
            res["area_ha"],
            compute_trend(res["time_series"]) if res["time_series"] else "estável",
            res["alert"]
        )

        if res["time_series_plot"]:
            st.subheader(f"Série Temporal de {index_name}")
            st.plotly_chart(res["time_series_plot"], use_container_width=True)

        if res["climate_plot"]:
            st.subheader("Dados Climáticos (NASA POWER)")
            st.plotly_chart(res["climate_plot"], use_container_width=True)

            if res["alert"]:
                st.warning(res["alert"])


if __name__ == "__main__":
    main()
