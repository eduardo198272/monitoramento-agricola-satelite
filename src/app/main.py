import ee
import streamlit as st
from datetime import date, timedelta
from streamlit_folium import st_folium

from src.app.config import APP_NAME, VERSION
from src.app.ee_auth import initialize_earth_engine
from src.app.earth_engine import (
    get_image_collection,
    calculate_ndvi,
    calculate_ndwi,
    calculate_ndmi,
    mask_clouds,
)
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
from src.app.time_series import compute_time_series, plot_time_series
from src.app.anomalies import detect_anomalies, generate_alert, compute_trend
from src.app.climate import fetch_climate_data, plot_climate_data
from src.app.styles import load_styles

DEFAULT_START = date.today() - timedelta(days=365)
DEFAULT_END = date.today()

UI_STATE_DEFAULTS = {
    "location_center": DEFAULT_CENTER,
    "location_zoom": DEFAULT_ZOOM,
    "location_result": None,
    "aoi_geojson": None,
    "aoi_geometry": None,
    "aoi_area_ha": None,
    "analysis_mode": "single",
    "visible_index": "NDVI",
    "analysis_results": {},
    "analysis_status": "idle",
    "analysis_error": None,
    "analysis_map": None,
}


def initialize_ui_state() -> None:
    """Initialize the UI state without overwriting values during reruns."""
    for key, default in UI_STATE_DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = default.copy() if isinstance(default, list) else default


def clear_analysis_state() -> None:
    """Clear results that no longer match the current area or request."""
    st.session_state.analysis_results = {}
    st.session_state.analysis_map = None
    st.session_state.analysis_status = "idle"
    st.session_state.analysis_error = None
    st.session_state.aoi_area_ha = None


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


def run_analysis(geometry, start_date, end_date, index_name):
    try:
        collection = get_image_collection(geometry, str(start_date), str(end_date))

        if collection.size().getInfo() == 0:
            return {
                "success": False,
                "error": "Nenhuma imagem encontrada para o período e área selecionados"
            }

        collection = collection.map(mask_clouds)

        if index_name == "NDVI":
            index_collection = collection.map(calculate_ndvi)
        elif index_name == "NDWI":
            index_collection = collection.map(calculate_ndwi)
        elif index_name == "NDMI":
            index_collection = collection.map(calculate_ndmi)
        else:
            return {
                "success": False,
                "error": f"Índice não suportado: {index_name}"
            }

        index_map = index_collection.median()

        band_name = index_name
        stats = index_map.select(band_name).reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=geometry,
            scale=10,
            maxPixels=1e9
        ).getInfo()

        mean_value = stats.get(band_name)

        area_ha = geometry.area().divide(10000).getInfo()

        time_series = compute_time_series(
            index_collection, geometry, index_name, scale=10
        )

        time_series_plot = plot_time_series(time_series, index_name) if time_series else None

        anomalies = detect_anomalies(time_series, window_size=3, std_threshold=1.0)
        alert = generate_alert(anomalies, index_name)

        try:
            climate_df = fetch_climate_data(geometry, start_date, end_date)
        except Exception:
            climate_df = None

        climate_plot = plot_climate_data(climate_df) if climate_df is not None and not climate_df.empty else None

        return {
            "success": True,
            "index_name": index_name,
            "index_map": index_map,
            "time_series": time_series,
            "time_series_plot": time_series_plot,
            "anomalies": anomalies,
            "alert": alert,
            "climate_data": climate_df,
            "climate_plot": climate_plot,
            "mean_value": mean_value,
            "area_ha": area_ha,
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


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
            location = search_location(location_query)
            if location is None:
                st.warning("Localidade não encontrada ou serviço indisponível.")
                st.session_state.location_result = None
            else:
                st.session_state.location_center = [
                    location["latitude"],
                    location["longitude"],
                ]
                st.session_state.location_zoom = calculate_map_zoom(
                    location["boundingbox"]
                )
                st.session_state.location_result = location

    if st.session_state.location_result:
        st.success(
            f"Localidade encontrada: "
            f"{st.session_state.location_result['display_name']}"
        )

    st.subheader("Área de interesse")
    st.info("Desenhe um polígono no mapa para definir a área de interesse")
    selection_map = create_selection_map(
        center=st.session_state.location_center,
        zoom=st.session_state.location_zoom,
        geojson=st.session_state.aoi_geojson,
    )
    map_data = st_folium(
        selection_map,
        key="area_selection_map",
        height=600,
        returned_objects=["last_active_drawing"],
        use_container_width=True,
    )

    drawn_geojson = map_data.get("last_active_drawing") if map_data else None
    if drawn_geojson:
        try:
            if drawn_geojson != st.session_state.aoi_geojson:
                st.session_state.aoi_geometry = geojson_to_ee_geometry(drawn_geojson)
                st.session_state.aoi_geojson = drawn_geojson
                clear_analysis_state()
            st.success("Área desenhada capturada! Clique em Analisar.")
        except ValueError as error:
            st.session_state.aoi_geometry = None
            st.session_state.aoi_geojson = None
            clear_analysis_state()
            st.error(str(error))
    elif st.session_state.aoi_geometry is None:
        st.info("Desenhe um polígono no mapa para definir a área.")

    st.subheader("Configurar análise")
    date_start_col, date_end_col, index_col = st.columns(3)
    with date_start_col:
        start_date = st.date_input("Data inicial", value=DEFAULT_START)
    with date_end_col:
        end_date = st.date_input("Data final", value=DEFAULT_END)
    with index_col:
        index_name = st.selectbox("Índice", options=["NDVI", "NDWI", "NDMI"])

    if end_date < start_date:
        st.error("Data final não pode ser anterior à data inicial")

    analyze = st.button("Analisar", disabled=(end_date < start_date))

    if analyze and end_date >= start_date:
        geometry = st.session_state.aoi_geometry

        if geometry is None:
            st.error("Desenhe uma área no mapa antes de analisar")
        else:
            st.session_state.analysis_status = "processing"
            st.session_state.analysis_error = None
            with st.spinner("Processando..."):
                result = run_analysis(geometry, start_date, end_date, index_name)
                if result["success"]:
                    st.session_state.analysis_results = {index_name: result}
                    st.session_state.visible_index = index_name
                    st.session_state.aoi_area_ha = result.get("area_ha")
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

                    m = add_index_layer(m, result["index_map"], index_name, palette=palette)
                    add_colorbar(m, palette, index_name)
                    st.session_state.analysis_map = m
                    st.session_state.analysis_status = "success"
                    st.session_state.analysis_error = None
                else:
                    st.session_state.analysis_error = result["error"]
                    st.session_state.analysis_map = None
                    st.session_state.analysis_results = {}
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
