import streamlit as st
from config import APP_NAME, VERSION

st.set_page_config(
    page_title=APP_NAME,
    layout="wide"
)

st.title(APP_NAME)
st.write(f"Versão: {VERSION}")

st.subheader("Interface inicial")

area = st.text_input("Nome da área de análise")
periodo = st.text_input("Período da análise")

if area:
    st.write(f"Área: {area}")

if periodo:
    st.write(f"Período: {periodo}")