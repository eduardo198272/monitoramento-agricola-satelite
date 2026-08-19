import streamlit as st
from datetime import date, timedelta

from src.app.config import APP_NAME, VERSION
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
    get_predefined_areas,
    load_predefined_area,
)

DEFAULT_START = date.today() - timedelta(days=365)
DEFAULT_END = date.today()


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


def compute_index_image(collection, index_name: str):
    if index_name == "NDVI":
        return collection.map(calculate_ndvi)
    elif index_name == "NDWI":
        return collection.map(calculate_ndwi)
    elif index_name == "NDMI":
        return collection.map(calculate_ndmi)
    raise ValueError(f"Índice não suportado: {index_name}")


def compute_statistics(index_image, geometry, index_name: str):
    band_name = index_name
    stats = index_image.select(band_name).reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=geometry,
        scale=10,
        maxPixels=1e9
    ).getInfo()

    mean_value = stats.get(band_name, 0)

    area_ha = geometry.area().divide(10000).getInfo()

    trend = "estável"
    if mean_value > 0.5:
        trend = "crescente"
    elif mean_value < 0.2:
        trend = "decrescente"

    alert = "Normal"
    if mean_value < 0:
        alert = "Possível água/nuvem"

    return mean_value, area_ha, trend, alert


def run_analysis(geometry, start_date, end_date, index_name):
    collection = get_image_collection(geometry, str(start_date), str(end_date))

    if collection.size().getInfo() == 0:
        raise ValueError("Nenhuma imagem encontrada para o período e área selecionados")

    collection = collection.map(mask_clouds)

    index_collection = compute_index_image(collection, index_name)

    mean_index = index_collection.mean()

    mean_value, area_ha, trend, alert = compute_statistics(
        mean_index, geometry, index_name
    )

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

    m = add_index_layer(m, mean_index, index_name, palette=palette)
    add_colorbar(m, palette, index_name)

    return m, mean_value, area_ha, trend, alert


import ee


def main():
    st.set_page_config(
        page_title="Monitoramento Agrícola por Imagens de Satélite",
        layout="wide"
    )

    st.title("Monitoramento Agrícola por Imagens de Satélite")

    with st.sidebar:
        st.header("Parâmetros de Análise")

        start_date = st.date_input("Data inicial", value=DEFAULT_START)
        end_date = st.date_input("Data final", value=DEFAULT_END)

        if end_date < start_date:
            st.error("Data final não pode ser anterior à data inicial")

        index_name = st.selectbox("Índice", options=["NDVI", "NDWI", "NDMI"])

        st.subheader("Seleção de Área")
        area_option = st.radio("Tipo de seleção", ["Desenhar no mapa", "Área pré-definida"])

        drawn_geometry = None
        predefined_geometry = None

        if area_option == "Área pré-definida":
            areas = get_predefined_areas()
            area_names = [a["name"] for a in areas]
            selected_area = st.selectbox("Área pré-definida", options=area_names)
            if selected_area:
                predefined_geometry = load_predefined_area(selected_area)

        analyze = st.button("Analisar", disabled=(end_date < start_date))

    if "map_obj" not in st.session_state:
        st.session_state.map_obj = None
        st.session_state.analysis_result = None
        st.session_state.error = None

    if area_option == "Desenhar no mapa" and st.session_state.map_obj is not None:
        pass

    col_main = st.container()

    with col_main:
        if analyze and end_date >= start_date:
            geometry = predefined_geometry if area_option == "Área pré-definida" else None

            if geometry is None:
                st.error("Selecione ou desenhe uma área antes de analisar")
            else:
                with st.spinner("Processando..."):
                    try:
                        m, mean_value, area_ha, trend, alert = run_analysis(
                            geometry, start_date, end_date, index_name
                        )
                        st.session_state.map_obj = m
                        st.session_state.analysis_result = {
                            "index_name": index_name,
                            "mean_value": mean_value,
                            "area_ha": area_ha,
                            "trend": trend,
                            "alert": alert
                        }
                        st.session_state.error = None
                    except Exception as e:
                        st.session_state.error = str(e)
                        st.session_state.map_obj = None
                        st.session_state.analysis_result = None

        if st.session_state.error:
            st.error(st.session_state.error)
        elif st.session_state.map_obj and st.session_state.analysis_result:
            display_map(st.session_state.map_obj)
            res = st.session_state.analysis_result
            display_summary(
                res["index_name"],
                res["mean_value"],
                res["area_ha"],
                res["trend"],
                res["alert"]
            )
        else:
            st.info("Selecione uma área e clique em Analisar")


if __name__ == "__main__":
    main()