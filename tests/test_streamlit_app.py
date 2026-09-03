import pytest
from unittest.mock import MagicMock, patch
from streamlit.testing.v1 import AppTest
import plotly.graph_objects as go

import src.app.main as main_module
from src.app.main import display_map, display_summary


def app_script():
    """Keep AppTest execution in the same module namespace as the app."""
    import src.app.main as app_main

    app_main.main()


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


@pytest.fixture
def function_app(monkeypatch):
    """Run the app with its external and map integrations isolated."""
    monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
    monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
    monkeypatch.setattr(main_module, "st_folium", lambda *args, **kwargs: {})

    app = AppTest.from_function(app_script)
    app.run()
    return app


class TestApplicationFlow:
    def test_earth_engine_initialization_failure_returns_error(self, monkeypatch):
        monkeypatch.setattr(
            main_module,
            "initialize_earth_engine",
            MagicMock(side_effect=RuntimeError("credenciais ausentes")),
        )
        main_module.init_earth_engine.clear()

        assert main_module.init_earth_engine() == (False, "credenciais ausentes")

        main_module.init_earth_engine.clear()

    def test_app_shows_earth_engine_initialization_error(self, monkeypatch):
        monkeypatch.setattr(
            main_module,
            "init_earth_engine",
            lambda: (False, "credenciais ausentes"),
        )

        app = AppTest.from_function(app_script)
        app.run()

        assert any("Erro ao inicializar Earth Engine" in error.value for error in app.error)
        assert any("EE_PROJECT_ID" in info.value for info in app.info)

    def test_valid_location_search_updates_state_and_message(
        self, function_app, monkeypatch
    ):
        location = {
            "display_name": "Passo Fundo, RS",
            "latitude": -28.26,
            "longitude": -52.41,
            "boundingbox": ["-28.3", "-28.2", "-52.5", "-52.3"],
        }
        search = MagicMock(return_value=location)
        monkeypatch.setattr(main_module, "search_location", search)
        monkeypatch.setattr(main_module, "calculate_map_zoom", lambda _: 11)

        function_app.text_input[0].set_value("Passo Fundo").run()
        next(button for button in function_app.button if button.label == "Pesquisar").click().run()

        search.assert_called_once_with("Passo Fundo")
        assert function_app.session_state["location_center"] == [-28.26, -52.41]
        assert function_app.session_state["location_zoom"] == 11
        assert any(
            "Localidade encontrada: Passo Fundo, RS" in success.value
            for success in function_app.success
        )

    def test_location_search_without_result_shows_warning(
        self, function_app, monkeypatch
    ):
        search = MagicMock(return_value=None)
        monkeypatch.setattr(main_module, "search_location", search)

        function_app.text_input[0].set_value("Localidade inexistente").run()
        next(button for button in function_app.button if button.label == "Pesquisar").click().run()

        search.assert_called_once_with("Localidade inexistente")
        assert any("Localidade não encontrada" in warning.value for warning in function_app.warning)
        assert function_app.session_state["location_result"] is None

    def test_empty_location_search_does_not_call_service(
        self, function_app, monkeypatch
    ):
        search = MagicMock()
        monkeypatch.setattr(main_module, "search_location", search)

        function_app.text_input[0].set_value("   ").run()
        next(button for button in function_app.button if button.label == "Pesquisar").click().run()

        search.assert_not_called()
        assert any("Informe uma localidade" in warning.value for warning in function_app.warning)

    def test_invalid_dates_block_analysis(self, function_app):
        start = next(item for item in function_app.date_input if item.label == "Data inicial")
        end = next(item for item in function_app.date_input if item.label == "Data final")

        start.set_value("2026-12-31").run()
        end.set_value("2026-01-01").run()

        analyze = next(button for button in function_app.button if button.label == "Analisar")
        assert analyze.disabled is True
        assert any("Data final não pode ser anterior" in error.value for error in function_app.error)

    def test_analysis_without_area_shows_error(self, function_app, monkeypatch):
        run_analysis = MagicMock()
        monkeypatch.setattr(main_module, "run_analysis", run_analysis)

        next(button for button in function_app.button if button.label == "Analisar").click().run()

        run_analysis.assert_not_called()
        assert any("Desenhe uma área no mapa" in error.value for error in function_app.error)

    def test_invalid_drawn_area_shows_error_and_is_not_analyzed(self, monkeypatch):
        geojson = {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}}
        run_analysis = MagicMock()

        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": geojson},
        )
        monkeypatch.setattr(
            main_module,
            "geojson_to_ee_geometry",
            MagicMock(side_effect=ValueError("Polígono inválido")),
        )
        monkeypatch.setattr(main_module, "run_analysis", run_analysis)

        app = AppTest.from_function(app_script)
        app.run()

        assert any("Polígono inválido" in error.value for error in app.error)
        assert app.session_state["drawn_geometry"] is None
        run_analysis.assert_not_called()

    def test_failed_analysis_shows_pipeline_error(self, monkeypatch):
        geometry = MagicMock()
        geojson = {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}}
        failure = {"success": False, "error": "Nenhuma imagem encontrada"}

        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": geojson},
        )
        monkeypatch.setattr(main_module, "geojson_to_ee_geometry", lambda _: geometry)
        run_analysis = MagicMock(return_value=failure)
        monkeypatch.setattr(main_module, "run_analysis", run_analysis)

        app = AppTest.from_function(app_script)
        app.run()
        next(button for button in app.button if button.label == "Analisar").click().run()

        run_analysis.assert_called_once()
        assert app.session_state["analysis_result"] is None
        assert app.session_state["map_obj"] is None
        assert any("Nenhuma imagem encontrada" in error.value for error in app.error)

    def test_successful_analysis_renders_outputs(self, monkeypatch):
        geometry = MagicMock()
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [
            -52.41,
            -28.26,
        ]
        geojson = {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}}
        result = {
            "success": True,
            "index_name": "NDVI",
            "index_map": MagicMock(),
            "time_series": [],
            "time_series_plot": None,
            "climate_plot": None,
            "alert": None,
            "mean_value": 0.65,
            "area_ha": 12.5,
        }

        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": geojson},
        )
        monkeypatch.setattr(main_module, "geojson_to_ee_geometry", lambda _: geometry)
        run_analysis = MagicMock(return_value=result)
        monkeypatch.setattr(main_module, "run_analysis", run_analysis)
        monkeypatch.setattr(main_module, "create_base_map", MagicMock())
        monkeypatch.setattr(main_module, "add_index_layer", MagicMock())
        monkeypatch.setattr(main_module, "add_colorbar", MagicMock())

        app = AppTest.from_function(app_script)
        app.run()
        next(button for button in app.button if button.label == "Analisar").click().run()

        run_analysis.assert_called_once()
        assert app.session_state["analysis_result"] == result
        assert len(app.metric) == 3

    @pytest.mark.parametrize(
        "index_name, expected_palette",
        [
            ("NDWI", ["brown", "white", "blue"]),
            ("NDMI", ["red", "yellow", "blue"]),
        ],
    )
    def test_successful_analysis_uses_index_palette(
        self, monkeypatch, index_name, expected_palette
    ):
        geometry = MagicMock()
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [
            -52.41,
            -28.26,
        ]
        geojson = {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}}
        result = {
            "success": True,
            "index_name": index_name,
            "index_map": MagicMock(),
            "time_series": [],
            "time_series_plot": None,
            "climate_plot": None,
            "alert": None,
            "mean_value": 0.2,
            "area_ha": 12.5,
        }
        add_index_layer = MagicMock()

        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": geojson},
        )
        monkeypatch.setattr(main_module, "geojson_to_ee_geometry", lambda _: geometry)
        monkeypatch.setattr(main_module, "run_analysis", MagicMock(return_value=result))
        monkeypatch.setattr(main_module, "create_base_map", MagicMock())
        monkeypatch.setattr(main_module, "add_index_layer", add_index_layer)
        monkeypatch.setattr(main_module, "add_colorbar", MagicMock())

        app = AppTest.from_function(app_script)
        app.run()
        next(selectbox for selectbox in app.selectbox if selectbox.label == "Índice").set_value(index_name).run()
        next(button for button in app.button if button.label == "Analisar").click().run()

        assert add_index_layer.call_args.kwargs["palette"] == expected_palette

    def test_existing_geometry_skips_empty_selection_message(self, function_app):
        function_app.session_state["drawn_geometry"] = MagicMock()
        function_app.session_state["drawn_geojson"] = None
        function_app.run()

        assert not any(
            message.value.endswith("Desenhe um polígono no mapa para definir a área.")
            for message in function_app.info
        )

    def test_successful_analysis_renders_time_series_climate_and_alert(self, monkeypatch):
        geometry = MagicMock()
        geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [
            -52.41,
            -28.26,
        ]
        geojson = {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}}
        result = {
            "success": True,
            "index_name": "NDVI",
            "index_map": MagicMock(),
            "time_series": [{"date": "2026-01-01", "value": 0.5}],
            "time_series_plot": go.Figure(),
            "climate_plot": go.Figure(),
            "alert": "ALERTA: queda detectada",
            "mean_value": 0.5,
            "area_ha": 12.5,
        }

        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": geojson},
        )
        monkeypatch.setattr(main_module, "geojson_to_ee_geometry", lambda _: geometry)
        monkeypatch.setattr(main_module, "run_analysis", MagicMock(return_value=result))
        monkeypatch.setattr(main_module, "create_base_map", MagicMock())
        monkeypatch.setattr(main_module, "add_index_layer", MagicMock())
        monkeypatch.setattr(main_module, "add_colorbar", MagicMock())
        monkeypatch.setattr(main_module.st, "plotly_chart", MagicMock())

        app = AppTest.from_function(app_script)
        app.run()
        next(button for button in app.button if button.label == "Analisar").click().run()

        assert any("Série Temporal de NDVI" in item.value for item in app.subheader)
        assert any("Dados Climáticos" in item.value for item in app.subheader)
        assert any("ALERTA: queda detectada" in item.value for item in app.warning)

    def test_successful_search_survives_rerun(self, function_app, monkeypatch):
        location = {
            "display_name": "Passo Fundo, RS",
            "latitude": -28.26,
            "longitude": -52.41,
            "boundingbox": ["-28.3", "-28.2", "-52.5", "-52.3"],
        }
        monkeypatch.setattr(main_module, "search_location", lambda _: location)
        monkeypatch.setattr(main_module, "calculate_map_zoom", lambda _: 11)

        function_app.text_input[0].set_value("Passo Fundo").run()
        next(button for button in function_app.button if button.label == "Pesquisar").click().run()
        function_app.run()

        assert function_app.session_state["location_result"] == location
        assert any("Localidade encontrada" in success.value for success in function_app.success)


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
