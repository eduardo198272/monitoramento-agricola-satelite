import pytest
from unittest.mock import MagicMock, patch
from streamlit.testing.v1 import AppTest

from src.app.main import display_map, display_summary


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


class TestPresentation:
    def test_display_map_uses_expected_height(self):
        map_obj = MagicMock()

        display_map(map_obj)

        map_obj.to_streamlit.assert_called_once_with(height=600)

    @pytest.mark.parametrize(
        "trend, expected_color",
        [
            ("crescente", "green"),
            ("estável", "blue"),
            ("decrescente", "red"),
            ("sem dados", "gray"),
        ],
    )
    def test_display_summary_renders_metrics_and_trend(self, trend, expected_color):
        columns = [MagicMock() for _ in range(4)]

        with patch("src.app.main.st") as mock_st:
            mock_st.columns.return_value = columns

            display_summary("NDVI", 0.62543, 12.5, trend)

        mock_st.columns.assert_called_once_with(4)
        assert [call.kwargs for call in mock_st.metric.call_args_list] == [
            {"label": "Índice", "value": "NDVI"},
            {"label": "Valor Médio", "value": "0.6254"},
            {"label": "Área (ha)", "value": "12.50"},
        ]
        mock_st.markdown.assert_called_once_with(
            f"**Tendência:** :{expected_color}[{trend}]"
        )

    @pytest.mark.parametrize(
        "alert, expected_color",
        [("normal", "green"), ("ALERTA: queda", "red")],
    )
    def test_display_summary_renders_alert_with_semantic_color(
        self, alert, expected_color
    ):
        columns = [MagicMock() for _ in range(4)]

        with patch("src.app.main.st") as mock_st:
            mock_st.columns.return_value = columns

            display_summary("NDVI", 0.5, 10.0, "estável", alert)

        assert mock_st.markdown.call_args_list == [
            (("**Tendência:** :blue[estável]",),),
            ((f"**Alerta:** :{expected_color}[{alert}]",),),
        ]

    def test_display_summary_does_not_render_alert_when_absent(self):
        columns = [MagicMock() for _ in range(4)]

        with patch("src.app.main.st") as mock_st:
            mock_st.columns.return_value = columns

            display_summary("NDVI", 0.5, 10.0, "estável", None)

        assert mock_st.markdown.call_count == 1
        mock_st.markdown.assert_called_once_with("**Tendência:** :blue[estável]")
