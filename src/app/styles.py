from pathlib import Path

import streamlit as st


CSS_PATH = Path(__file__).with_name("assets") / "style.css"
REQUIRED_TOKENS = (
    "#0E1117",
    "#161B22",
    "#1C2128",
    "#30363D",
    "#F0F3F6",
    "#8B949E",
)


def load_styles() -> None:
    """Load the application stylesheet from its module-relative path."""
    css = CSS_PATH.read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
