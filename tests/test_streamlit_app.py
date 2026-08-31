import pytest
from streamlit.testing.v1 import AppTest


@pytest.fixture
def app():
    app = AppTest.from_file("src/app/main.py")
    app.run()
    return app


class TestAppStructure:
    def test_app_loads_without_error(self, app):
        assert not app.exception

    def test_page_config_wide_layout(self, app):
        page_config = app.get("page_config")
        if page_config:
            assert page_config[0].layout == "wide"

    def test_title_displayed(self, app):
        assert len(app.title) > 0
        assert "Monitoramento Agrícola" in app.title[0].value


class TestSidebarControls:
    def test_sidebar_has_location_search_input(self, app):
        search_input = next(
            (text_input for text_input in app.text_input
             if text_input.label == "Pesquisar localidade"),
            None,
        )
        assert search_input is not None

    def test_sidebar_has_location_search_button(self, app):
        buttons = app.button
        search_button = next((b for b in buttons if b.label == "Pesquisar"), None)
        assert search_button is not None

    def test_sidebar_has_date_inputs(self, app):
        date_inputs = app.date_input
        assert len(date_inputs) >= 2

    def test_sidebar_date_input_labels(self, app):
        date_inputs = app.date_input
        labels = [di.label for di in date_inputs]
        assert "Data inicial" in labels
        assert "Data final" in labels

    def test_sidebar_default_start_date(self, app):
        start_input = next(di for di in app.date_input if di.label == "Data inicial")
        assert start_input.value is not None

    def test_sidebar_default_end_date(self, app):
        end_input = next(di for di in app.date_input if di.label == "Data final")
        assert end_input.value is not None

    def test_sidebar_has_index_selectbox(self, app):
        selectboxes = app.selectbox
        index_select = next(sb for sb in selectboxes if sb.label == "Índice")
        assert index_select is not None
        assert set(index_select.options) == {"NDVI", "NDWI", "NDMI"}

    def test_sidebar_has_analyze_button(self, app):
        buttons = app.button
        analyze_btn = next((b for b in buttons if b.label == "Analisar"), None)
        assert analyze_btn is not None



class TestValidation:
    def test_end_date_before_start_shows_error(self, app):
        start_input = next(di for di in app.date_input if di.label == "Data inicial")
        end_input = next(di for di in app.date_input if di.label == "Data final")

        start_input.set_value("2026-12-31").run()
        end_input.set_value("2026-01-01").run()

        errors = [el.value for el in app.error]
        assert any("Data final não pode ser anterior" in e for e in errors)

    def test_analyze_button_disabled_when_dates_invalid(self, app):
        start_input = next(di for di in app.date_input if di.label == "Data inicial")
        end_input = next(di for di in app.date_input if di.label == "Data final")

        start_input.set_value("2026-12-31").run()
        end_input.set_value("2026-01-01").run()

        analyze_btn = next((b for b in app.button if b.label == "Analisar"), None)
        assert analyze_btn is not None
        assert analyze_btn.disabled is True


class TestInitialState:
    def test_initial_message_displayed(self, app):
        info_messages = [el.value for el in app.info]
        assert any("Desenhe um polígono" in msg for msg in info_messages)
