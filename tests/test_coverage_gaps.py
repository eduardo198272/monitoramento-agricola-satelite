from datetime import date
import runpy
import sys
from types import ModuleType
from unittest.mock import MagicMock

import pytest

import src.app.main as main_module
import src.app.map_interaction as map_interaction


class SessionState(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as error:
            raise AttributeError(name) from error

    def __setattr__(self, name, value):
        self[name] = value


@pytest.fixture
def stub_streamlit(monkeypatch):
    stub = MagicMock()
    state = SessionState()
    stub.session_state = state
    monkeypatch.setattr(main_module, "st", stub)
    return stub, state


def test_earth_engine_initialization_returns_success_and_caches(monkeypatch):
    initialize = MagicMock()
    monkeypatch.setattr(main_module, "initialize_earth_engine", initialize)
    main_module.init_earth_engine.clear()
    try:
        assert main_module.init_earth_engine() == (True, None)
        assert main_module.init_earth_engine() == (True, None)
        initialize.assert_called_once_with()
    finally:
        main_module.init_earth_engine.clear()


def test_render_analysis_map_reports_missing_preloaded_index_grid(
    monkeypatch, stub_streamlit
):
    stub, _ = stub_streamlit
    stub.session_state.index_value_grid = None
    stub.session_state.index_preload_error = "preload failed"

    main_module.render_analysis_map(MagicMock(), "NDVI", None)

    stub.error.assert_called_once_with("preload failed")


def test_render_analysis_map_reuses_cached_tiles_and_default_center(
    monkeypatch, stub_streamlit
):
    stub, _ = stub_streamlit
    grid = {"indices": {"NDVI": {"minimum": 0.2, "maximum": 0.8}}}
    stub.session_state.index_value_grid = grid
    stub.session_state.index_tile_urls = {"NDVI": "cached-tile-url"}
    stub.session_state.analysis_map_center = None
    stub.session_state.aoi_geometry = MagicMock()
    render_map = MagicMock(return_value="map")
    get_tile = MagicMock()
    monkeypatch.setattr(main_module, "render_index_hover_map", render_map)
    monkeypatch.setattr(main_module, "get_index_map_tile_url", get_tile)

    result = main_module.render_analysis_map(MagicMock(), "NDVI", {"type": "Feature"})

    assert result == "map"
    get_tile.assert_not_called()
    assert render_map.call_args.kwargs["tile_url"] == "cached-tile-url"
    assert render_map.call_args.kwargs["center"] == main_module.DEFAULT_CENTER


@pytest.mark.parametrize(
    "summary",
    [
        None,
        {
            "total_precipitation_mm": None,
            "mean_temperature_c": None,
            "mean_solar_radiation_mj_m2_day": None,
        },
        {
            "total_precipitation_mm": 12.3,
            "mean_temperature_c": None,
            "mean_solar_radiation_mj_m2_day": 4.5,
        },
        {
            "total_precipitation_mm": None,
            "mean_temperature_c": 21.5,
            "mean_solar_radiation_mj_m2_day": None,
        },
    ],
)
def test_display_analysis_details_handles_climate_summary_availability(
    monkeypatch, summary
):
    stub = MagicMock()
    stub.columns.return_value = [MagicMock(), MagicMock(), MagicMock()]
    monkeypatch.setattr(main_module, "st", stub)
    main_module.display_analysis_details(
        "NDVI",
        {
            "time_series_plot": None,
            "anomalies": [],
            "climate_summary": summary,
        },
        climate_plot=None,
    )

    assert any(
        "indisponíveis" in str(call.args[0]).lower()
        for call in stub.info.call_args_list
    )
    if summary and any(value is not None for value in summary.values()):
        assert stub.metric.call_count == 3


def test_render_results_panels_recovers_an_invalid_visible_index(monkeypatch, stub_streamlit):
    stub, state = stub_streamlit
    state.analysis_results = {
        "NDVI": {"mean_value": 0.3, "time_series": [], "alert": None}
    }
    state.visible_index = "STALE"
    state.visible_index_control = "STALE"
    state.analysis_metadata = {}
    stub.radio.side_effect = lambda *args, **kwargs: setattr(
        state, kwargs["key"], kwargs["options"][0]
    )
    monkeypatch.setattr(main_module, "display_summary", MagicMock())
    monkeypatch.setattr(main_module, "display_anomaly_alert", MagicMock())
    monkeypatch.setattr(main_module, "display_analysis_details", MagicMock())

    main_module.render_results_panels()

    assert state.visible_index == "NDVI"
    assert state.visible_index_control == "NDVI"


def test_render_results_map_handles_empty_results_and_edit_action(
    monkeypatch, stub_streamlit
):
    stub, state = stub_streamlit
    state.analysis_results = {}
    assert main_module.render_results_map_area() is False
    stub.button.return_value = True
    state.analysis_results = {"NDVI": {"index_map": object()}}
    for key, value in {
        "analysis_metadata": {},
        "analysis_map": None,
        "analysis_map_center": None,
        "index_value_grid": None,
        "index_preload_error": None,
        "index_tile_urls": {},
        "analysis_status": "success",
        "analysis_error": None,
    }.items():
        setattr(state, key, value)

    assert main_module.render_results_map_area() is False
    assert state.analysis_results == {}
    assert state.analysis_status == "idle"


def test_render_results_map_reports_thematic_map_errors(monkeypatch, stub_streamlit):
    stub, state = stub_streamlit
    stub.button.return_value = False
    state.analysis_results = {"NDVI": {"index_map": object()}}
    state.visible_index_control = "NDVI"
    state.visible_index = "NDVI"
    state.aoi_geojson = {"type": "Feature"}
    monkeypatch.setattr(
        main_module, "render_analysis_map", MagicMock(side_effect=RuntimeError("tiles"))
    )

    assert main_module.render_results_map_area() is True
    stub.error.assert_called_once_with("Não foi possível carregar o mapa temático.")


def test_main_reports_missing_geometry_if_analyze_is_enabled(monkeypatch, stub_streamlit):
    stub, state = stub_streamlit
    state.analysis_start_date = date(2026, 1, 1)
    state.analysis_end_date = date(2026, 1, 31)
    monkeypatch.setattr(main_module, "load_styles", MagicMock())
    monkeypatch.setattr(main_module, "render_header_bar", MagicMock())
    monkeypatch.setattr(main_module, "render_controls_bar", lambda: (True, False))
    monkeypatch.setattr(main_module, "render_selection_map_area", MagicMock())

    main_module.main()

    stub.error.assert_called_once_with("Desenhe uma área no mapa antes de analisar")
    main_module.render_selection_map_area.assert_called_once_with()


def test_main_falls_back_to_selection_map_if_result_map_fails(
    monkeypatch, stub_streamlit
):
    stub, state = stub_streamlit
    state.analysis_status = "success"
    state.analysis_results = {"NDVI": {"index_map": object()}}
    monkeypatch.setattr(main_module, "load_styles", MagicMock())
    monkeypatch.setattr(main_module, "render_header_bar", MagicMock())
    monkeypatch.setattr(main_module, "render_controls_bar", lambda: (False, True))
    monkeypatch.setattr(main_module, "render_results_map_area", lambda: False)
    selection_map = MagicMock()
    monkeypatch.setattr(main_module, "render_selection_map_area", selection_map)

    main_module.main()

    selection_map.assert_called_once_with()


def test_main_module_entry_point_runs_app_with_stubbed_streamlit(monkeypatch):
    import streamlit_folium
    import src.app.ee_auth as ee_auth

    state = SessionState()
    class FakeStreamlit(ModuleType):
        def __getattr__(self, name):
            return MagicMock(name=f"streamlit.{name}")

    fake_streamlit = FakeStreamlit("streamlit")
    fake_streamlit.session_state = state
    fake_streamlit.cache_resource = lambda function: function
    fake_streamlit.columns = lambda columns, **kwargs: [
        MagicMock() for _ in columns
    ]
    fake_streamlit.container = MagicMock(return_value=MagicMock())
    fake_streamlit.date_input = lambda label, value=None, **kwargs: value
    fake_streamlit.radio = lambda *args, **kwargs: "NDVI"
    fake_streamlit.button = lambda *args, **kwargs: False
    fake_streamlit.text_input = lambda *args, **kwargs: ""
    monkeypatch.setitem(sys.modules, "streamlit", fake_streamlit)
    import src.app.styles as styles

    monkeypatch.setattr(styles, "load_styles", lambda: None)
    monkeypatch.setattr(ee_auth, "initialize_earth_engine", MagicMock())
    monkeypatch.setattr(streamlit_folium, "st_folium", lambda *args, **kwargs: {})

    runpy.run_path(main_module.__file__, run_name="__main__")


def test_map_interaction_forwards_all_component_parameters(monkeypatch):
    component = MagicMock(return_value={"sample": 0.42})
    monkeypatch.setattr(map_interaction, "_index_hover_component", component)
    params = {
        "tile_url": "tiles/{z}/{x}/{y}",
        "center": [-28.0, -52.0],
        "zoom": 11,
        "geojson": {"type": "Feature"},
        "index_name": "NDVI",
        "palette": ["white", "green"],
        "value_grid": {"indices": {}},
        "key": "map-test",
        "height": 480,
    }

    result = map_interaction.render_index_hover_map(**params)

    assert result == {"sample": 0.42}
    component.assert_called_once_with(**params, default=None, width="stretch")
