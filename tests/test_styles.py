from pathlib import Path
from unittest.mock import patch

from src.app.styles import CSS_PATH, REQUIRED_TOKENS, load_styles


def test_stylesheet_exists_with_required_tokens():
    css = CSS_PATH.read_text(encoding="utf-8")

    assert CSS_PATH.is_file()
    assert all(token in css for token in REQUIRED_TOKENS)


def test_stylesheet_defines_component_and_responsive_rules():
    css = CSS_PATH.read_text(encoding="utf-8")

    assert "[data-testid=\"stTextInput\"]" in css
    assert "[data-testid=\"stButton\"]" in css
    assert ".ui-card" in css
    assert "@media (max-width: 768px)" in css


def test_load_styles_injects_css_from_any_working_directory():
    with patch("src.app.styles.st.markdown") as markdown:
        load_styles()

    markdown.assert_called_once()
    css, kwargs = markdown.call_args.args[0], markdown.call_args.kwargs
    assert "--color-background" in css
    assert kwargs == {"unsafe_allow_html": True}
