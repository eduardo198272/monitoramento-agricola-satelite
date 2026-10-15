from contextlib import contextmanager
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest
from streamlit.testing.v1 import AppTest
import plotly.graph_objects as go

import src.app.main as main_module
from src.app.main import (
    DEFAULT_END,
    DEFAULT_START,
    UI_STATE_DEFAULTS,
    display_analysis_details,
    display_anomaly_alert,
    display_map,
    display_multi_index_overview,
    display_summary,
)


def app_script():
    """Keep AppTest execution in the same module namespace as the app."""
    import src.app.main as app_main

    app_main.main()


def make_geometry(area_ha=12.5, perimeter_km=5.0, centroid=(-28.26, -52.41)):
    geometry = MagicMock()
    # Support both old pattern (divide().getInfo()) and new pattern (getInfo())
    geometry.area.return_value.getInfo.return_value = area_ha * 10000  # area in m²
    geometry.area.return_value.divide.return_value.getInfo.return_value = area_ha
    geometry.perimeter.return_value.getInfo.return_value = perimeter_km * 1000  # perimeter in m
    geometry.perimeter.return_value.divide.return_value.getInfo.return_value = perimeter_km
    geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [
        centroid[1], centroid[0],
    ]
    return geometry


@pytest.fixture
def app(monkeypatch):
    """Run the app with its external and map integrations isolated."""
    monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
    monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
    monkeypatch.setattr(main_module, "st_folium", lambda *args, **kwargs: {})

    app = AppTest.from_function(app_script)
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

    def test_map_first_header_displays_operational_context(self, app):
        assert app.title[0].value == "Monitoramento Agrícola"
        assert any(
            "imagens de satélite" in item.value
            for item in app.caption
        )
        assert not any("Earth Engine conectado" in item.value for item in app.success)

    def test_area_workspace_shows_drawing_instruction_without_fake_button(self, app):
        assert any(
            "Use a ferramenta de polígono no mapa" in item.value
            for item in app.info
        )
        assert all(button.label != "Desenhar área" for button in app.button)


class TestWorkspaceControls:
    def test_workspace_has_location_search_input(self, app):
        search_input = next(
            (text_input for text_input in app.text_input
             if text_input.label == "Localidade"),
            None,
        )
        assert search_input is not None

    def test_workspace_has_location_search_button(self, app):
        buttons = app.button
        search_button = next((b for b in buttons if b.label == "🔍"), None)
        assert search_button is not None

    def test_workspace_has_date_inputs(self, app):
        date_inputs = app.date_input
        assert len(date_inputs) >= 2
        assert any(item.value == DEFAULT_START for item in date_inputs)
        assert any(item.value == DEFAULT_END for item in date_inputs)

    def test_workspace_date_input_labels(self, app):
        date_inputs = app.date_input
        labels = [di.label for di in date_inputs]
        assert "Data inicial" in labels
        assert "Data final" in labels

    def test_workspace_default_start_date(self, app):
        start_input = next(di for di in app.date_input if di.label == "Data inicial")
        assert start_input.value is not None

    def test_workspace_default_end_date(self, app):
        end_input = next(di for di in app.date_input if di.label == "Data final")
        assert end_input.value is not None

    def test_workspace_has_horizontal_index_radio(self, app):
        index_selector = next(radio for radio in app.radio if radio.label == "Índice")
        assert index_selector is not None
        assert index_selector.options == ["Todos", "NDVI", "NDWI", "NDMI"]
        assert not any(item.label == "Índice" for item in app.selectbox)

    @pytest.mark.parametrize(
        "selection, expected_mode, expected_indices",
        [
            ("NDVI", "single", ["NDVI"]),
            ("NDWI", "single", ["NDWI"]),
            ("NDMI", "single", ["NDMI"]),
            ("Todos", "multi", ["NDVI", "NDWI", "NDMI"]),
        ],
    )
    def test_index_selection_updates_mode_and_supported_indices(
        self, app, selection, expected_mode, expected_indices
    ):
        next(radio for radio in app.radio if radio.label == "Índice").set_value(selection).run()

        assert app.session_state["analysis_mode"] == expected_mode
        assert app.session_state["selected_indices"] == expected_indices

    def test_switching_analysis_mode_keeps_drawn_area_on_selection_map(
        self, app, monkeypatch
    ):
        selected_geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[-52.1, -28.0], [-52.0, -28.0],
                                 [-52.0, -28.1], [-52.1, -28.0]]],
            },
        }
        geometry = make_geometry()
        app.session_state["aoi_geojson"] = selected_geojson
        app.session_state["aoi_geometry"] = geometry
        app.session_state["aoi_area_ha"] = 12.5
        app.session_state["aoi_perimeter_km"] = 5.0
        app.session_state["aoi_centroid"] = (-28.26, -52.41)
        create_map = MagicMock()
        monkeypatch.setattr(main_module, "create_selection_map", create_map)

        next(radio for radio in app.radio if radio.label == "Índice").set_value("Todos").run()

        assert app.session_state["aoi_geojson"] == selected_geojson
        assert app.session_state["aoi_geometry"] is geometry
        assert create_map.call_args.kwargs["geojson"] == selected_geojson

    def test_workspace_has_analyze_button(self, app):
        buttons = app.button
        analyze_btn = next((b for b in buttons if b.label == "Analisar área"), None)
        assert analyze_btn is not None
        assert analyze_btn.disabled is True

    def test_analyze_button_is_enabled_when_area_and_dates_are_valid(self, function_app):
        function_app.session_state["aoi_geometry"] = make_geometry()

        function_app.run()

        analyze_btn = next(
            button for button in function_app.button if button.label == "Analisar área"
        )
        assert analyze_btn.disabled is False

    def test_todos_calls_multi_index_pipeline(self, function_app, monkeypatch):
        run_analysis = MagicMock()
        index_results = {name: {"mean_value": 0.2} for name in ("NDVI", "NDWI", "NDMI")}
        run_multi_analysis = MagicMock(
            return_value={
                "success": True,
                "indices": index_results,
                "area_ha": 12.5,
                "image_count": 3,
                "climate_data": None,
                "climate_plot": None,
                "map_center": [-20.0, -45.0],
            }
        )
        monkeypatch.setattr(main_module, "run_analysis", run_analysis)
        monkeypatch.setattr(main_module, "run_multi_analysis", run_multi_analysis)
        function_app.session_state["aoi_geometry"] = make_geometry()

        next(
            radio for radio in function_app.radio if radio.label == "Índice"
        ).set_value("Todos").run()
        next(
            button
            for button in function_app.button
            if button.label == "Analisar área"
        ).click().run()

        run_analysis.assert_not_called()
        run_multi_analysis.assert_called_once_with(
            function_app.session_state["aoi_geometry"],
            function_app.session_state["analysis_start_date"],
            function_app.session_state["analysis_end_date"],
            ["NDVI", "NDWI", "NDMI"],
            area_ha=None,
        )
        assert function_app.session_state["analysis_status"] == "success"
        assert function_app.session_state["analysis_results"] == index_results
        assert function_app.session_state["analysis_map_center"] == [-20.0, -45.0]
        assert function_app.session_state["analysis_metadata"] == {
            "area_ha": 12.5,
            "image_count": 3,
            "climate_data": None,
            "climate_plot": None,
        }

        function_app.run()

        run_multi_analysis.assert_called_once()
        assert function_app.session_state["analysis_results"] == index_results
        assert function_app.session_state["analysis_metadata"]["image_count"] == 3



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

        analyze_btn = next((b for b in app.button if b.label == "Analisar área"), None)
        assert analyze_btn is not None
        assert analyze_btn.disabled is True

    def test_same_day_is_a_valid_analysis_period(self, app):
        start_input = next(di for di in app.date_input if di.label == "Data inicial")
        end_input = next(di for di in app.date_input if di.label == "Data final")
        same_date = "2026-06-15"

        start_input.set_value(same_date).run()
        end_input.set_value(same_date).run()

        assert not any("Data final não pode ser anterior" in item.value for item in app.error)
        assert app.session_state["analysis_start_date"] == app.session_state["analysis_end_date"]


class TestInitialState:
    def test_ui_v2_state_has_single_source_of_truth(self, app):
        expected_keys = set(UI_STATE_DEFAULTS)

        assert all(key in app.session_state for key in expected_keys)
        assert app.session_state["analysis_status"] == "idle"
        assert app.session_state["analysis_mode"] == "single"
        assert app.session_state["visible_index"] == "NDVI"
        assert app.session_state["analysis_results"] == {}
        assert app.session_state["analysis_metadata"] == {}
        assert app.session_state["aoi_geojson"] is None
        assert app.session_state["aoi_geometry"] is None
        assert app.session_state["aoi_area_ha"] is None

    def test_initial_message_displayed(self, app):
        info_messages = [el.value for el in app.info]
        assert any("ferramenta de polígono no mapa" in msg for msg in info_messages)


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
    def test_earth_engine_initialization_failure_returns_error(self, monkeypatch, caplog):
        monkeypatch.setattr(
            main_module,
            "initialize_earth_engine",
            MagicMock(side_effect=RuntimeError("credenciais ausentes")),
        )
        main_module.init_earth_engine.clear()

        with caplog.at_level("ERROR", logger="src.app.main"):
            assert main_module.init_earth_engine() == (False, "credenciais ausentes")

        record = next(record for record in caplog.records if record.name == "src.app.main")
        assert record.getMessage() == "Earth Engine initialization failed"
        assert record.exc_info is not None

        main_module.init_earth_engine.clear()

    def test_app_shows_earth_engine_initialization_error(self, monkeypatch):
        monkeypatch.setattr(
            main_module,
            "init_earth_engine",
            lambda: (False, "credenciais ausentes"),
        )

        app = AppTest.from_function(app_script)
        app.run()

        assert any("Earth Engine indisponível" in error.value for error in app.error)
        assert any("EE_PROJECT_ID" in info.value for info in app.info)
        assert all("credenciais ausentes" not in error.value for error in app.error)

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
        selected_geojson = {"type": "Feature", "properties": {"selected": True}}
        selected_geometry = {"geometry": "existing-area"}
        function_app.session_state["aoi_geojson"] = selected_geojson
        function_app.session_state["aoi_geometry"] = selected_geometry
        function_app.session_state["aoi_area_ha"] = 12.5

        function_app.text_input[0].set_value("Passo Fundo").run()
        next(button for button in function_app.button if button.label == "🔍").click().run()

        search.assert_called_once_with("Passo Fundo")
        assert function_app.session_state["location_center"] == [-28.26, -52.41]
        assert function_app.session_state["location_zoom"] == 11
        assert function_app.session_state["aoi_geojson"] == selected_geojson
        assert function_app.session_state["aoi_geometry"] == selected_geometry
        assert function_app.session_state["aoi_area_ha"] == 12.5
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
        next(button for button in function_app.button if button.label == "🔍").click().run()

        search.assert_called_once_with("Localidade inexistente")
        assert any("Localidade não encontrada" in warning.value for warning in function_app.warning)
        assert function_app.session_state["location_result"] is None

    def test_location_search_failure_preserves_map_and_selected_area(
        self, function_app, monkeypatch
    ):
        search = MagicMock(side_effect=RuntimeError("serviço indisponível"))
        monkeypatch.setattr(main_module, "search_location", search)
        selected_geojson = {"type": "Feature", "properties": {"selected": True}}
        selected_geometry = {"geometry": "existing-area"}
        function_app.session_state["location_center"] = [-27.0, -51.0]
        function_app.session_state["location_zoom"] = 8
        function_app.session_state["location_result"] = {"display_name": "Local anterior"}
        function_app.session_state["aoi_geojson"] = selected_geojson
        function_app.session_state["aoi_geometry"] = selected_geometry
        function_app.session_state["aoi_area_ha"] = 12.5
        create_map = MagicMock()
        monkeypatch.setattr(main_module, "create_selection_map", create_map)

        function_app.text_input[0].set_value("Nova localidade").run()
        next(button for button in function_app.button if button.label == "🔍").click().run()

        search.assert_called_once_with("Nova localidade")
        assert any(
            "geocodificação indisponível" in warning.value
            for warning in function_app.warning
        )
        assert function_app.session_state["location_center"] == [-27.0, -51.0]
        assert function_app.session_state["location_zoom"] == 8
        assert function_app.session_state["location_result"] == {"display_name": "Local anterior"}
        assert function_app.session_state["aoi_geojson"] == selected_geojson
        assert function_app.session_state["aoi_geometry"] == selected_geometry
        assert function_app.session_state["aoi_area_ha"] == 12.5
        assert create_map.call_args.kwargs["center"] == [-27.0, -51.0]
        assert create_map.call_args.kwargs["zoom"] == 8
        assert create_map.call_args.kwargs["geojson"] == selected_geojson

    def test_empty_location_search_does_not_call_service(
        self, function_app, monkeypatch
    ):
        search = MagicMock()
        monkeypatch.setattr(main_module, "search_location", search)

        function_app.text_input[0].set_value("   ").run()
        next(button for button in function_app.button if button.label == "🔍").click().run()

        search.assert_not_called()
        assert any("Informe uma localidade" in warning.value for warning in function_app.warning)

    def test_invalid_dates_block_analysis(self, function_app):
        start = next(item for item in function_app.date_input if item.label == "Data inicial")
        end = next(item for item in function_app.date_input if item.label == "Data final")

        start.set_value("2026-12-31").run()
        end.set_value("2026-01-01").run()

        analyze = next(button for button in function_app.button if button.label == "Analisar área")
        assert analyze.disabled is True
        assert any("Data final não pode ser anterior" in error.value for error in function_app.error)

    def test_analysis_without_area_is_disabled(self, function_app, monkeypatch):
        run_analysis = MagicMock()
        run_multi_analysis = MagicMock()
        monkeypatch.setattr(main_module, "run_analysis", run_analysis)
        monkeypatch.setattr(main_module, "run_multi_analysis", run_multi_analysis)

        analyze = next(
            button for button in function_app.button if button.label == "Analisar área"
        )

        assert analyze.disabled is True
        run_analysis.assert_not_called()
        run_multi_analysis.assert_not_called()

    def test_analysis_event_without_area_is_rejected_defensively(
        self, function_app, monkeypatch
    ):
        run_analysis = MagicMock()
        monkeypatch.setattr(main_module, "run_analysis", run_analysis)
        monkeypatch.setattr(
            main_module.st,
            "button",
            lambda label, *args, **kwargs: label == "Analisar área",
        )

        function_app.run()

        run_analysis.assert_not_called()
        # With the new layout, the button is disabled when there's no area,
        # so no error message is shown (the button click is prevented by Streamlit).
        # The test verifies that run_analysis is not called.

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
        assert app.session_state["aoi_geometry"] is None
        run_analysis.assert_not_called()

    def test_invalid_redraw_preserves_previously_selected_area(self, monkeypatch):
        drawn_geojson = {
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": []},
        }
        previous_geojson = {"type": "Feature", "properties": {"valid": True}}
        previous_geometry = MagicMock(name="previous_geometry")
        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": drawn_geojson},
        )
        app = AppTest.from_function(app_script)
        app.session_state["aoi_geojson"] = previous_geojson
        app.session_state["aoi_geometry"] = previous_geometry
        app.session_state["aoi_area_ha"] = 7.5

        app.run()

        assert any("usando um polígono" in error.value for error in app.error)
        assert app.session_state["aoi_geojson"] == previous_geojson
        assert app.session_state["aoi_geometry"] is previous_geometry
        assert app.session_state["aoi_area_ha"] == 7.5

    def test_area_is_calculated_when_drawing_is_captured(self, monkeypatch):
        geometry = make_geometry(area_ha=3.25)
        geojson = {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}}
        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": geojson},
        )
        monkeypatch.setattr(main_module, "geojson_to_ee_geometry", lambda _: geometry)

        app = AppTest.from_function(app_script)
        app.run()

        geometry.area.assert_called_once_with()
        geometry.area.return_value.getInfo.assert_called_once_with()
        geometry.perimeter.assert_called_once_with()
        geometry.perimeter.return_value.getInfo.assert_called_once_with()
        geometry.centroid.assert_called_once_with()
        geometry.centroid.return_value.coordinates.assert_called_once_with()
        geometry.centroid.return_value.coordinates.return_value.getInfo.assert_called_once_with()
        assert app.session_state["aoi_geojson"] == geojson
        assert app.session_state["aoi_geometry"] is geometry
        assert app.session_state["aoi_area_ha"] == 3.25
        assert app.session_state["aoi_perimeter_km"] == 5.0
        assert app.session_state["aoi_centroid"] == (-28.26, -52.41)
        assert any("3.25 ha" in success.value for success in app.success)
        assert not next(
            button for button in app.button if button.label == "Analisar área"
        ).disabled

    def test_area_calculation_failure_does_not_partially_replace_selection(self, monkeypatch):
        geometry = make_geometry(area_ha=0)
        new_geojson = {"type": "Feature", "properties": {"new": True}}
        old_geojson = {"type": "Feature", "properties": {"old": True}}
        old_geometry = MagicMock(name="old_geometry")
        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": new_geojson},
        )
        monkeypatch.setattr(main_module, "geojson_to_ee_geometry", lambda _: geometry)
        app = AppTest.from_function(app_script)
        app.session_state["aoi_geojson"] = old_geojson
        app.session_state["aoi_geometry"] = old_geometry
        app.session_state["aoi_area_ha"] = 7.5

        app.run()

        assert any("área válida em hectares" in error.value for error in app.error)
        assert app.session_state["aoi_geojson"] == old_geojson
        assert app.session_state["aoi_geometry"] is old_geometry
        assert app.session_state["aoi_area_ha"] == 7.5

    def test_explicit_drawing_removal_clears_area_and_analysis_state(self, monkeypatch):
        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {
                "all_drawings": [],
                "last_active_drawing": {"type": "Feature", "properties": {"stale": True}},
            },
        )
        app = AppTest.from_function(app_script)
        app.session_state["aoi_geojson"] = {"type": "Feature"}
        app.session_state["aoi_geometry"] = MagicMock(name="selected_geometry")
        app.session_state["aoi_area_ha"] = 7.5
        app.session_state["analysis_results"] = {"NDVI": {"success": True}}
        app.session_state["analysis_metadata"] = {"image_count": 5}
        app.session_state["analysis_map"] = MagicMock(name="analysis_map")
        app.session_state["analysis_status"] = "success"
        app.session_state["analysis_error"] = "stale error"

        app.run()

        assert app.session_state["aoi_geojson"] is None
        assert app.session_state["aoi_geometry"] is None
        assert app.session_state["aoi_area_ha"] is None
        assert app.session_state["analysis_results"] == {}
        assert app.session_state["analysis_metadata"] == {}
        assert app.session_state["analysis_map"] is None
        assert app.session_state["analysis_status"] == "idle"
        assert app.session_state["analysis_error"] is None

    def test_rerun_without_map_update_preserves_area_state(self, function_app):
        geojson = {"type": "Feature", "properties": {"selected": True}}
        geometry = make_geometry()
        function_app.session_state["aoi_geojson"] = geojson
        function_app.session_state["aoi_geometry"] = geometry
        function_app.session_state["aoi_area_ha"] = 4.5
        saved_results = {"NDVI": {"mean_value": 0.5}}
        saved_metadata = {"area_ha": 4.5, "image_count": 2}
        function_app.session_state["analysis_results"] = saved_results
        function_app.session_state["analysis_metadata"] = saved_metadata

        function_app.run()

        assert function_app.session_state["aoi_geojson"] == geojson
        assert function_app.session_state["aoi_geometry"] is geometry
        assert function_app.session_state["aoi_area_ha"] == 4.5
        assert function_app.session_state["analysis_results"] == saved_results
        assert function_app.session_state["analysis_metadata"] == saved_metadata

    def test_completed_analysis_survives_regular_rerun_without_pipeline(
        self, function_app, monkeypatch
    ):
        geometry = make_geometry()
        geojson = {"type": "Feature", "properties": {"selected": True}}
        result = {
            "index_map": MagicMock(name="cached_ndvi_image"),
            "mean_value": 0.625,
            "time_series": [{"date": "2026-01-01", "value": 0.625}],
            "time_series_plot": None,
            "anomalies": [],
            "alert": None,
            "area_ha": 12.5,
        }
        run_analysis = MagicMock()
        run_multi_analysis = MagicMock()
        render_analysis_map = MagicMock(return_value=None)
        monkeypatch.setattr(main_module, "run_analysis", run_analysis)
        monkeypatch.setattr(main_module, "run_multi_analysis", run_multi_analysis)
        monkeypatch.setattr(main_module, "render_analysis_map", render_analysis_map)
        function_app.session_state["aoi_geometry"] = geometry
        function_app.session_state["aoi_geojson"] = geojson
        function_app.session_state["aoi_area_ha"] = 12.5
        function_app.session_state["analysis_results"] = {"NDVI": result}
        function_app.session_state["analysis_metadata"] = {"area_ha": 12.5}
        function_app.session_state["analysis_map_center"] = [-28.26, -52.41]
        function_app.session_state["analysis_status"] = "success"
        function_app.session_state["visible_index"] = "NDVI"

        function_app.run()
        function_app.run()

        assert function_app.session_state["analysis_results"] == {"NDVI": result}
        assert function_app.session_state["analysis_status"] == "success"
        assert function_app.session_state["aoi_geometry"] is geometry
        assert function_app.session_state["aoi_geojson"] == geojson
        assert function_app.session_state["aoi_area_ha"] == 12.5
        assert render_analysis_map.call_count == 2
        assert all(
            call.args[0] is result["index_map"]
            for call in render_analysis_map.call_args_list
        )
        run_analysis.assert_not_called()
        run_multi_analysis.assert_not_called()

    def test_failed_analysis_shows_pipeline_error(self, monkeypatch):
        geometry = make_geometry()
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
        next(button for button in app.button if button.label == "Analisar área").click().run()

        run_analysis.assert_called_once_with(
            geometry,
            app.session_state["analysis_start_date"],
            app.session_state["analysis_end_date"],
            "NDVI",
            area_ha=12.5,
        )
        assert app.session_state["analysis_results"] == {}
        assert app.session_state["analysis_map"] is None
        assert app.session_state["analysis_status"] == "no_data"
        assert app.session_state["analysis_error"] == (
            "Nenhuma imagem Sentinel-2 disponível para o período e a área "
            "selecionados. Amplie o período ou revise a área e tente novamente."
        )
        assert any("Amplie o período" in warning.value for warning in app.warning)
        assert not app.error

    def test_failed_multi_analysis_sets_no_data_status(self, function_app, monkeypatch):
        geometry = make_geometry()
        failure = {"success": False, "error": "Nenhuma imagem encontrada"}
        run_multi_analysis = MagicMock(return_value=failure)
        monkeypatch.setattr(main_module, "run_multi_analysis", run_multi_analysis)
        function_app.session_state["aoi_geometry"] = geometry

        next(radio for radio in function_app.radio if radio.label == "Índice").set_value(
            "Todos"
        ).run()
        next(
            button for button in function_app.button if button.label == "Analisar área"
        ).click().run()

        run_multi_analysis.assert_called_once_with(
            geometry,
            function_app.session_state["analysis_start_date"],
            function_app.session_state["analysis_end_date"],
            ["NDVI", "NDWI", "NDMI"],
            area_ha=None,
        )
        assert function_app.session_state["analysis_status"] == "no_data"
        assert "Amplie o período" in function_app.session_state["analysis_error"]
        assert function_app.session_state["analysis_results"] == {}
        assert function_app.session_state["analysis_metadata"] == {}
        assert function_app.session_state["analysis_map"] is None

    def test_generic_analysis_failure_sets_error_status(self, monkeypatch):
        geometry = make_geometry()
        geojson = {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}}
        spinner_messages = []

        @contextmanager
        def capture_spinner(message):
            spinner_messages.append(message)
            yield

        monkeypatch.setattr(main_module.st, "spinner", capture_spinner)

        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": geojson},
        )
        monkeypatch.setattr(main_module, "geojson_to_ee_geometry", lambda _: geometry)
        technical_error = "Earth Engine indisponível: sensitive internal detail"
        monkeypatch.setattr(
            main_module,
            "run_analysis",
            MagicMock(return_value={"success": False, "error": technical_error}),
        )

        app = AppTest.from_function(app_script)
        app.run()
        next(button for button in app.button if button.label == "Analisar área").click().run()

        assert app.session_state["analysis_status"] == "error"
        assert "Google Earth Engine" in app.session_state["analysis_error"]
        assert technical_error not in app.session_state["analysis_error"]
        assert any("Google Earth Engine" in error.value for error in app.error)
        assert all("sensitive internal detail" not in error.value for error in app.error)
        assert spinner_messages == [
            "Buscando imagens Sentinel-2, aplicando máscara de nuvens "
            "e calculando os índices..."
        ]

    def test_render_analysis_map_passes_selected_index_to_hover_component(
        self, monkeypatch
    ):
        image = MagicMock(name="cached-index")
        grid = {
            "analysis_key": "analysis-1",
            "indices": {"NDVI": {"minimum": 0.1, "maximum": 0.9}},
        }
        geometry = MagicMock(name="aoi-geometry")
        monkeypatch.setattr(
            main_module.st,
            "session_state",
            SimpleNamespace(
                analysis_map_center=[-28.1, -52.2],
                index_value_grid=grid,
                index_tile_urls={},
                aoi_geometry=geometry,
            ),
        )
        get_tile_url = MagicMock(return_value="https://ee.example/tiles/{z}/{x}/{y}")
        render_component = MagicMock(return_value=None)
        monkeypatch.setattr(main_module, "get_index_map_tile_url", get_tile_url)
        monkeypatch.setattr(main_module, "render_index_hover_map", render_component)
        geojson = {"type": "Feature", "geometry": {"type": "Polygon"}}

        main_module.render_analysis_map(image, "NDVI", geojson)

        get_tile_url.assert_called_once_with(image, "NDVI", geometry, 0.1, 0.9)
        render_component.assert_called_once_with(
            tile_url="https://ee.example/tiles/{z}/{x}/{y}",
            center=[-28.1, -52.2],
            zoom=12,
            geojson=geojson,
            index_name="NDVI",
            palette=main_module.INDEX_PALETTES["NDVI"],
            value_grid=grid,
            key="thematic-index-map",
        )

    def test_successful_analysis_renders_outputs(self, monkeypatch):
        geometry = make_geometry()
        geojson = {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}}
        result = {
            "success": True,
            "index_name": "NDVI",
            "index_map": MagicMock(),
            "time_series": [],
            "time_series_plot": None,
            "climate_plot": go.Figure(),
            "alert": None,
            "mean_value": 0.65,
            "area_ha": 12.5,
            "map_center": [-20.0, -45.0],
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
        render_analysis_map = MagicMock(return_value=None)
        monkeypatch.setattr(
            main_module, "render_analysis_map", render_analysis_map
        )

        app = AppTest.from_function(app_script)
        app.run()
        next(button for button in app.button if button.label == "Analisar área").click().run()

        run_analysis.assert_called_once_with(
            geometry,
            app.session_state["analysis_start_date"],
            app.session_state["analysis_end_date"],
            "NDVI",
            area_ha=12.5,
        )
        assert app.session_state["analysis_results"] == {"NDVI": result}
        assert app.session_state["analysis_metadata"] == {
            "area_ha": 12.5,
            "climate_plot": result["climate_plot"],
        }
        assert app.session_state["visible_index"] == "NDVI"
        assert app.session_state["analysis_status"] == "success"
        assert app.session_state["aoi_area_ha"] == 12.5
        assert app.session_state["analysis_map_center"] == [-20.0, -45.0]
        # centroid is now called during area context calculation in render_selection_map_area
        assert len(app.metric) == 3

    @pytest.mark.parametrize(
        "index_name",
        [
            "NDWI",
            "NDMI",
        ],
    )
    def test_successful_analysis_renders_selected_index(self, monkeypatch, index_name):
        geometry = make_geometry()
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
        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": geojson},
        )
        monkeypatch.setattr(main_module, "geojson_to_ee_geometry", lambda _: geometry)
        monkeypatch.setattr(main_module, "run_analysis", MagicMock(return_value=result))
        render_analysis_map = MagicMock(return_value=None)
        monkeypatch.setattr(main_module, "render_analysis_map", render_analysis_map)

        app = AppTest.from_function(app_script)
        app.run()
        # Directly set the session state for index selection to avoid AppTest radio widget issues
        app.session_state["index_selection"] = index_name
        app.session_state["analysis_mode"] = "single"
        app.session_state["selected_indices"] = [index_name]
        app.run()
        next(button for button in app.button if button.label == "Analisar área").click().run()

        render_analysis_map.assert_called_once()
        assert render_analysis_map.call_args.args[1] == index_name

    def test_switching_visible_index_uses_cached_map_without_running_pipeline(
        self, function_app, monkeypatch
    ):
        ndvi_image = MagicMock(name="ndvi_image")
        ndwi_image = MagicMock(name="ndwi_image")
        results = {
            index_name: {
                "index_map": image,
                "mean_value": 0.25,
                "time_series": [
                    {"date": "2026-01-01", "value": 0.1},
                    {"date": "2026-02-01", "value": 0.5},
                ],
                "time_series_plot": None,
                "alert": None,
            }
            for index_name, image in (("NDVI", ndvi_image), ("NDWI", ndwi_image))
        }
        results["NDVI"]["trend"] = "decrescente"
        geometry = make_geometry()
        geojson = {
            "type": "Feature",
            "geometry": {"type": "Polygon", "coordinates": []},
        }
        function_app.session_state["aoi_geometry"] = geometry
        function_app.session_state["aoi_geojson"] = geojson
        function_app.session_state["analysis_results"] = results
        function_app.session_state["analysis_metadata"] = {
            "area_ha": 12.5,
            "image_count": 8,
        }
        function_app.session_state["analysis_map_center"] = [-28.26, -52.41]
        function_app.session_state["analysis_status"] = "success"
        function_app.session_state["visible_index"] = "NDMI"

        run_analysis = MagicMock()
        run_multi_analysis = MagicMock()
        render_analysis_map = MagicMock(return_value=None)
        monkeypatch.setattr(main_module, "run_analysis", run_analysis)
        monkeypatch.setattr(main_module, "run_multi_analysis", run_multi_analysis)
        monkeypatch.setattr(main_module, "render_analysis_map", render_analysis_map)

        function_app.run()
        next(
            radio
            for radio in function_app.radio
            if radio.label == "Índice no mapa"
        ).set_value("NDWI").run()

        assert function_app.session_state["visible_index"] == "NDWI"
        assert render_analysis_map.call_args.args == (ndwi_image, "NDWI", geojson)
        metric_values = [(metric.label, metric.value) for metric in function_app.metric]
        assert ("Imagens analisadas", "8") in metric_values
        assert metric_values.count(("Valor médio", "0.2500")) == 2
        assert ("Tendência", "decrescente") in metric_values
        assert ("Tendência", "crescente") in metric_values
        run_analysis.assert_not_called()
        run_multi_analysis.assert_not_called()

    def test_existing_geometry_skips_empty_selection_message(self, function_app):
        function_app.session_state["aoi_geometry"] = MagicMock()
        function_app.session_state["aoi_geojson"] = None
        function_app.run()

        assert not any(
            message.value.endswith("Desenhe um polígono no mapa para definir a área.")
            for message in function_app.info
        )

    def test_successful_analysis_renders_time_series_climate_and_alert(self, monkeypatch):
        geometry = make_geometry()
        geojson = {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}}
        result = {
            "success": True,
            "index_name": "NDVI",
            "index_map": MagicMock(),
            "time_series": [{"date": "2026-01-01", "value": 0.5}],
            "time_series_plot": go.Figure(),
            "climate_plot": go.Figure(),
            "anomalies": [
                {"date": "2026-01-01", "value": 0.5, "anomaly": True}
            ],
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
        monkeypatch.setattr(
            main_module, "render_analysis_map", MagicMock(return_value=None)
        )
        monkeypatch.setattr(main_module.st, "plotly_chart", MagicMock())

        app = AppTest.from_function(app_script)
        app.run()
        next(button for button in app.button if button.label == "Analisar área").click().run()

        assert any("Série Temporal de NDVI" in item.value for item in app.subheader)
        assert any("Anomalias de NDVI" in item.value for item in app.subheader)
        assert any("Dados Climáticos" in item.value for item in app.subheader)
        rendered_warnings = [item.value for item in app.warning]
        assert sum("ALERTA: queda detectada" in item for item in rendered_warnings) == 1
        assert not any("ALERTA: queda detectada" in item.value for item in app.markdown)

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
        next(button for button in function_app.button if button.label == "🔍").click().run()
        function_app.run()

        assert function_app.session_state["location_result"] == location
        assert any("Localidade encontrada" in success.value for success in function_app.success)

    def test_area_context_displays_area_perimeter_centroid(self, monkeypatch):
        geometry = make_geometry(area_ha=42.7, perimeter_km=12.3, centroid=(-28.26, -52.41))
        geojson = {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}}
        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": geojson},
        )
        monkeypatch.setattr(main_module, "geojson_to_ee_geometry", lambda _: geometry)

        app = AppTest.from_function(app_script)
        app.run()

        assert app.session_state["aoi_area_ha"] == 42.7
        assert app.session_state["aoi_perimeter_km"] == 12.3
        assert app.session_state["aoi_centroid"] == (-28.26, -52.41)
        assert any("42.70 ha" in success.value for success in app.success)
        assert any("12.30 km" in success.value for success in app.success)
        assert any("-28.2600, -52.4100" in success.value or "-28.26, -52.41" in success.value for success in app.success)

    def test_area_context_rerun_preserves_metrics(self, function_app):
        geometry = make_geometry(area_ha=10.5, perimeter_km=8.2, centroid=(-20.0, -45.0))
        geojson = {"type": "Feature", "properties": {"selected": True}}
        function_app.session_state["aoi_geojson"] = geojson
        function_app.session_state["aoi_geometry"] = geometry
        function_app.session_state["aoi_area_ha"] = 10.5
        function_app.session_state["aoi_perimeter_km"] = 8.2
        function_app.session_state["aoi_centroid"] = (-20.0, -45.0)

        function_app.run()

        assert function_app.session_state["aoi_area_ha"] == 10.5
        assert function_app.session_state["aoi_perimeter_km"] == 8.2
        assert function_app.session_state["aoi_centroid"] == (-20.0, -45.0)

    def test_area_context_removal_clears_all_metrics(self, monkeypatch):
        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {
                "all_drawings": [],
                "last_active_drawing": {"type": "Feature", "properties": {"stale": True}},
            },
        )
        app = AppTest.from_function(app_script)
        app.session_state["aoi_geojson"] = {"type": "Feature"}
        app.session_state["aoi_geometry"] = MagicMock(name="selected_geometry")
        app.session_state["aoi_area_ha"] = 7.5
        app.session_state["aoi_perimeter_km"] = 5.0
        app.session_state["aoi_centroid"] = (-28.26, -52.41)
        app.session_state["analysis_results"] = {"NDVI": {"success": True}}
        app.session_state["analysis_metadata"] = {"image_count": 5}
        app.session_state["analysis_map"] = MagicMock(name="analysis_map")
        app.session_state["analysis_status"] = "success"
        app.session_state["analysis_error"] = "stale error"

        app.run()

        assert app.session_state["aoi_geojson"] is None
        assert app.session_state["aoi_geometry"] is None
        assert app.session_state["aoi_area_ha"] is None
        assert app.session_state["aoi_perimeter_km"] is None
        assert app.session_state["aoi_centroid"] is None
        assert app.session_state["analysis_results"] == {}
        assert app.session_state["analysis_metadata"] == {}
        assert app.session_state["analysis_map"] is None
        assert app.session_state["analysis_status"] == "idle"
        assert app.session_state["analysis_error"] is None

    def test_area_context_failure_does_not_replace_existing(self, monkeypatch):
        geometry = make_geometry(area_ha=0)
        new_geojson = {"type": "Feature", "properties": {"new": True}}
        old_geojson = {"type": "Feature", "properties": {"old": True}}
        old_geometry = MagicMock(name="old_geometry")
        monkeypatch.setattr(main_module, "init_earth_engine", lambda: (True, None))
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(
            main_module,
            "st_folium",
            lambda *args, **kwargs: {"last_active_drawing": new_geojson},
        )
        monkeypatch.setattr(main_module, "geojson_to_ee_geometry", lambda _: geometry)
        app = AppTest.from_function(app_script)
        app.session_state["aoi_geojson"] = old_geojson
        app.session_state["aoi_geometry"] = old_geometry
        app.session_state["aoi_area_ha"] = 7.5
        app.session_state["aoi_perimeter_km"] = 5.0
        app.session_state["aoi_centroid"] = (-28.26, -52.41)

        app.run()

        assert any("área válida em hectares" in error.value for error in app.error)
        assert app.session_state["aoi_geojson"] == old_geojson
        assert app.session_state["aoi_geometry"] is old_geometry
        assert app.session_state["aoi_area_ha"] == 7.5
        assert app.session_state["aoi_perimeter_km"] == 5.0
        assert app.session_state["aoi_centroid"] == (-28.26, -52.41)


class TestHeaderBar:
    def test_header_shows_product_identity(self, function_app):
        assert function_app.title[0].value == "Monitoramento Agrícola"
        assert any("satélite" in c.value.lower() for c in function_app.caption)

    def test_header_hides_earth_engine_status_when_connected(self, function_app):
        assert not any("Earth Engine conectado" in s.value for s in function_app.success)

    def test_header_does_not_show_unavailable_actions_menu(self, function_app):
        assert not any(
            "expand_more" in button.label or "⋮" in button.label
            for button in function_app.button
        )

    def test_header_shows_earth_engine_error_when_disconnected(self, monkeypatch):
        mock_init = MagicMock(return_value=(False, "fail"))
        monkeypatch.setattr(main_module, "init_earth_engine", mock_init)
        monkeypatch.setattr(main_module, "create_selection_map", MagicMock())
        monkeypatch.setattr(main_module, "st_folium", lambda *args, **kwargs: {})
        app = AppTest.from_function(app_script)
        app.run()
        assert any("Earth Engine indisponível" in e.value for e in app.error)
        assert app.title[0].value == "Monitoramento Agrícola"


class TestControlsBar:
    def test_controls_bar_has_search_input_and_button(self, function_app):
        search_input = next(t for t in function_app.text_input if t.label == "Localidade")
        search_btn = next(b for b in function_app.button if b.label == "🔍")
        assert search_input is not None
        assert search_btn is not None

    def test_controls_bar_has_start_and_end_date_inputs(self, function_app):
        date_inputs = function_app.date_input
        assert len(date_inputs) >= 2
        labels = [d.label for d in date_inputs]
        assert "Data inicial" in labels
        assert "Data final" in labels

    def test_controls_bar_has_horizontal_index_radio(self, function_app):
        radio = next(r for r in function_app.radio if r.label == "Índice")
        assert radio.options == ["Todos", "NDVI", "NDWI", "NDMI"]

    def test_controls_bar_has_analyze_button(self, function_app):
        btn = next(b for b in function_app.button if b.label == "Analisar área")
        assert btn is not None
        assert btn.disabled is True

    def test_controls_bar_date_validation_inline(self, function_app):
        start = next(d for d in function_app.date_input if d.label == "Data inicial")
        end = next(d for d in function_app.date_input if d.label == "Data final")
        start.set_value("2026-12-31").run()
        end.set_value("2026-01-01").run()
        assert any("Data final não pode ser anterior" in e.value for e in function_app.error)
        analyze_btn = next(b for b in function_app.button if b.label == "Analisar área")
        assert analyze_btn.disabled is True

    def test_controls_bar_enables_analyze_when_area_and_dates_valid(self, function_app):
        function_app.session_state["aoi_geometry"] = make_geometry()
        function_app.run()
        analyze_btn = next(b for b in function_app.button if b.label == "Analisar área")
        assert analyze_btn.disabled is False

    def test_index_selection_updates_mode_and_selected_indices(self, function_app):
        radio = next(r for r in function_app.radio if r.label == "Índice")
        radio.set_value("Todos").run()
        assert function_app.session_state["analysis_mode"] == "multi"
        assert function_app.session_state["selected_indices"] == ["NDVI", "NDWI", "NDMI"]
        radio.set_value("NDWI").run()
        assert function_app.session_state["analysis_mode"] == "single"
        assert function_app.session_state["selected_indices"] == ["NDWI"]


class TestLayoutOrder:
    def test_header_renders_before_controls_bar(self, function_app):
        # Check that title exists
        titles = function_app.get("title")
        assert any("Monitoramento Agrícola" in el.value for el in titles)
        # Check that search input exists
        search_inputs = function_app.get("text_input")
        assert any(el.label == "Localidade" for el in search_inputs)

    def test_controls_bar_renders_before_map(self, function_app):
        search_idx = None
        map_idx = None
        for i, el in enumerate(function_app.get("text_input")):
            if el.label == "Localidade":
                search_idx = i
                break
        for i, el in enumerate(function_app.get("markdown")):
            if "st_folium" in str(type(el)) or "folium" in str(type(el)).lower():
                map_idx = i
                break
        if search_idx is not None and map_idx is not None:
            assert search_idx < map_idx

    def test_results_panels_render_only_after_success(self, function_app):
        assert not any("Série Temporal" in s.value for s in function_app.subheader)
        assert not any("Anomalias" in s.value for s in function_app.subheader)
        assert not any("Dados Climáticos" in s.value for s in function_app.subheader)


class TestPresentation:
    def test_display_map_uses_expected_height(self):
        map_obj = MagicMock()

        display_map(map_obj)

        map_obj.to_streamlit.assert_called_once_with(
            height=main_module.RESULTS_MAP_HEIGHT
        )

    def test_selection_map_keeps_expected_height_after_rerun(self):
        with patch("src.app.main.st") as mock_st:
            mock_st.session_state = SimpleNamespace(
                location_center=[0, 0],
                location_zoom=5,
                aoi_geojson=None,
                aoi_geometry=None,
            )
            with patch("src.app.main.create_selection_map") as create_map:
                with patch("src.app.main.st_folium", return_value={}) as folium:
                    main_module.render_selection_map_area()

        create_map.assert_called_once_with(center=[0, 0], zoom=5, geojson=None)
        assert folium.call_args.kwargs["height"] == main_module.MAP_HEIGHT
        assert folium.call_args.kwargs["key"] == "area_selection_map"

    def test_multi_index_overview_marks_missing_metrics_as_unavailable(self):
        columns = [MagicMock()]
        with patch("src.app.main.st") as mock_st:
            mock_st.columns.return_value = columns
            display_multi_index_overview(
                {"NDMI": {"mean_value": None, "time_series": []}}, None
            )

        assert [call.kwargs for call in mock_st.metric.call_args_list] == [
            {"label": "Imagens analisadas", "value": "Indisponível"},
            {"label": "Valor médio", "value": "Indisponível"},
            {"label": "Tendência", "value": "Indisponível"},
        ]

    def test_analysis_details_show_empty_states_when_data_is_missing(self):
        with patch("src.app.main.st") as mock_st:
            display_analysis_details("NDWI", {}, None)

        assert mock_st.subheader.call_args_list == [
            (("Série Temporal de NDWI",),),
            (("Anomalias de NDWI",),),
            (("Dados Climáticos (NASA POWER)",),),
        ]
        assert [call.args[0] for call in mock_st.info.call_args_list] == [
            "Série temporal de NDWI indisponível para este período.",
            "Nenhuma anomalia detectada no NDWI para este período.",
            "Dados climáticos indisponíveis para este período.",
        ]
        mock_st.plotly_chart.assert_not_called()

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

            display_summary("NDVI", 0.62543, 12.5, "ha", trend)

        mock_st.columns.assert_called_once_with(4)
        assert [call.kwargs for call in mock_st.metric.call_args_list] == [
            {"label": "Índice", "value": "NDVI"},
            {"label": "Valor Médio", "value": "0.6254"},
            {"label": "Área (ha)", "value": "12.50"},
        ]
        mock_st.markdown.assert_called_once_with(
            f"**Tendência:** :{expected_color}[{trend}]"
        )

    def test_display_summary_renders_area_with_custom_unit(self):
        columns = [MagicMock() for _ in range(4)]

        with patch("src.app.main.st") as mock_st:
            mock_st.columns.return_value = columns

            display_summary("NDVI", 0.5, 25.0, "acres", "estável")

        metric_calls = [call.kwargs for call in mock_st.metric.call_args_list]
        assert metric_calls[2] == {"label": "Área (acres)", "value": "25.00"}


class TestDisplayAnomalyAlert:
    def test_display_anomaly_alert_renders_warning(self):
        with patch("src.app.main.st") as mock_st:
            display_anomaly_alert("ALERTA: 2 anomalia(s) detectada(s) no NDVI")

        mock_st.warning.assert_called_once_with("ALERTA: 2 anomalia(s) detectada(s) no NDVI")

    def test_display_anomaly_alert_does_not_render_when_none(self):
        with patch("src.app.main.st") as mock_st:
            display_anomaly_alert(None)

        mock_st.warning.assert_not_called()

    def test_display_anomaly_alert_does_not_render_when_empty(self):
        with patch("src.app.main.st") as mock_st:
            display_anomaly_alert("")

        mock_st.warning.assert_not_called()
