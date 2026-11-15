"""Regressions for fresh selections, component remounts and search resets."""

from copy import deepcopy
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from streamlit.testing.v1 import AppTest
import streamlit_folium

import src.app.main as main
from src.app.maps import create_selection_map


def feature(name="first", offset=0):
    return {
        "type": "Feature",
        "properties": {"name": name},
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [-52.41 + offset, -28.26], [-52.40 + offset, -28.26],
                [-52.40 + offset, -28.25], [-52.41 + offset, -28.26],
            ]],
        },
    }


def run_app():
    import src.app.main

    src.app.main.main()


def button(app, label):
    return next(item for item in app.button if item.label == label)


@pytest.fixture
def flow(monkeypatch):
    packet = [{}]
    first, second = feature(), feature("second", 0.1)
    geometries = {"first": object(), "second": object()}
    monkeypatch.setattr(main, "init_earth_engine", lambda: (True, None))
    create_map = MagicMock()
    monkeypatch.setattr(main, "create_selection_map", create_map)
    monkeypatch.setattr(main, "st_folium", lambda *args, **kwargs: deepcopy(packet[0]))
    monkeypatch.setattr(
        main, "geojson_to_ee_geometry",
        lambda geojson: geometries[geojson["properties"]["name"]],
    )
    monkeypatch.setattr(main, "calculate_area_context", lambda geometry: {
        "area_ha": 15.0, "perimeter_km": 2.0, "centroid": (-28.26, -52.41),
    })
    result = {
        "success": True, "index_name": "NDVI", "index_map": "image",
        "area_ha": 15.0, "mean_value": 0.5,
    }
    single = MagicMock(return_value=result)
    multi = MagicMock(return_value={
        "success": True, "indices": {
            name: {"index_map": f"image-{name}"} for name in main.SUPPORTED_INDICES
        },
        "area_ha": 15.0, "image_count": 1,
    })
    monkeypatch.setattr(main, "run_analysis", single)
    monkeypatch.setattr(main, "run_multi_analysis", multi)
    monkeypatch.setattr(main, "preload_index_values", MagicMock(return_value={}))
    monkeypatch.setattr(main, "render_analysis_map", MagicMock())
    monkeypatch.setattr(main, "render_results_panels", MagicMock())
    monkeypatch.setattr(main, "render_export_actions", MagicMock())
    app = AppTest.from_function(run_app).run()
    assert not app.exception
    return SimpleNamespace(
        app=app, packet=packet, first=first, second=second,
        geometries=geometries, single=single, multi=multi, create_map=create_map,
    )


def select(flow, geojson):
    flow.packet[0] = {"last_active_drawing": geojson, "all_drawings": [geojson]}
    flow.app.run()
    assert not flow.app.exception
    assert not button(flow.app, "Analisar área").disabled


def test_accepting_a_drawing_does_not_change_the_real_folium_component_identity(monkeypatch):
    """Exercise streamlit-folium's real JS hash, not a mocked map factory."""
    # Use a real dictionary-like Streamlit state without starting a browser.
    class State(dict):
        def __getattr__(self, name):
            return self[name]

        def __setattr__(self, name, value):
            self[name] = value

    state = State()
    ui = MagicMock(session_state=state)
    ui.button.return_value = False
    monkeypatch.setattr(main, "st", ui)
    main.initialize_ui_state()
    geojson = feature()
    component_calls = []

    def component(**kwargs):
        component_calls.append(kwargs)
        return {"last_active_drawing": geojson, "all_drawings": [geojson]}

    monkeypatch.setattr(streamlit_folium, "_component_func", component)
    monkeypatch.setattr(main, "create_selection_map", create_selection_map)
    monkeypatch.setattr(main, "st_folium", streamlit_folium.st_folium)
    monkeypatch.setattr(main, "geojson_to_ee_geometry", lambda _: "geometry")
    monkeypatch.setattr(main, "calculate_area_context", lambda _: {
        "area_ha": 15.0, "perimeter_km": 2.0, "centroid": (-28.26, -52.41),
    })

    main.render_selection_map_area()
    main.render_selection_map_area()

    assert state.aoi_geojson == geojson
    assert component_calls[0]["key"] == component_calls[1]["key"]
    assert component_calls[0]["script"] == component_calls[1]["script"]


@pytest.mark.parametrize("index", ["NDVI", "Todos"])
def test_change_area_requires_a_fresh_polygon_and_reanalysis_uses_it(flow, index):
    app = flow.app
    next(radio for radio in app.radio if radio.label == "Índice").set_value(index).run()
    select(flow, flow.first)
    button(app, "Analisar área").click().run()
    assert app.session_state["analysis_status"] == "success"
    pipeline = flow.single if index == "NDVI" else flow.multi
    assert pipeline.call_count == 1
    revision = app.session_state["selection_map_revision"]
    app.session_state["export_payloads"] = {"pdf": b"old"}
    flow.packet[0] = {}

    button(app, "Alterar área").click().run()

    assert not app.exception
    assert app.session_state["analysis_status"] == "idle"
    assert app.session_state["aoi_geojson"] is None
    assert app.session_state["aoi_geometry"] is None
    assert app.session_state["export_payloads"] == {}
    assert app.session_state["selection_map_revision"] > revision
    assert button(app, "Analisar área").disabled

    select(flow, flow.second)
    button(app, "Analisar área").click().run()
    assert not app.exception
    assert pipeline.call_count == 2
    assert pipeline.call_args.args[0] is flow.geometries["second"]
    assert app.session_state["analysis_status"] == "success"
    assert app.session_state["analysis_snapshot"]["geometry_geojson"] == flow.second
    app.run()
    assert pipeline.call_count == 2


def test_successful_search_clears_selection_and_results_without_starting_analysis(
    flow, monkeypatch
):
    app = flow.app
    select(flow, flow.first)
    button(app, "Analisar área").click().run()
    location = {
        "display_name": "Nova localidade", "latitude": -27.0, "longitude": -51.0,
        "boundingbox": ["-27.1", "-26.9", "-51.1", "-50.9"],
    }
    search = MagicMock(return_value=location)
    monkeypatch.setattr(main, "search_location", search)
    next(item for item in app.text_input if item.label == "Localidade").set_value(
        "Nova localidade"
    ).run()
    revision = app.session_state["selection_map_revision"]
    app.session_state["export_payloads"] = {"pdf": b"old"}
    app.session_state["pending_saved_location_id"] = "old-location"
    app.session_state["pending_saved_location_name"] = "Old location"
    app.session_state["show_save_location_dialog"] = True
    flow.packet[0] = {}
    button(app, "🔍").click().run()

    assert not app.exception
    search.assert_called_once_with("Nova localidade")
    assert app.session_state["location_center"] == [-27.0, -51.0]
    assert app.session_state["aoi_geojson"] is None
    assert app.session_state["aoi_geometry"] is None
    assert app.session_state["analysis_results"] == {}
    assert app.session_state["analysis_snapshot"] is None
    assert app.session_state["export_payloads"] == {}
    assert app.session_state["index_value_grid"] is None
    assert app.session_state["index_tile_urls"] == {}
    assert app.session_state["aoi_area_ha"] is None
    assert app.session_state["aoi_perimeter_km"] is None
    assert app.session_state["aoi_centroid"] is None
    assert app.session_state["pending_saved_location_id"] is None
    assert app.session_state["pending_saved_location_name"] is None
    assert app.session_state["show_save_location_dialog"] is False
    assert app.session_state["selection_map_revision"] > revision
    assert app.session_state["analysis_status"] == "idle"
    assert button(app, "Analisar área").disabled
    assert flow.create_map.call_args.kwargs["geojson"] is None
    assert flow.single.call_count == 1


@pytest.mark.parametrize("failure", [None, RuntimeError("geocoder offline")])
def test_failed_search_keeps_completed_analysis_and_selected_area(flow, monkeypatch, failure):
    app = flow.app
    select(flow, flow.first)
    button(app, "Analisar área").click().run()
    app.session_state["export_payloads"] = {"pdf": b"current"}
    before_revision = app.session_state["selection_map_revision"]
    before_center = app.session_state["location_center"]
    search = MagicMock(return_value=None)
    if failure:
        search.side_effect = failure
    monkeypatch.setattr(main, "search_location", search)
    next(item for item in app.text_input if item.label == "Localidade").set_value(
        "Unknown"
    ).run()
    button(app, "🔍").click().run()

    assert not app.exception
    assert app.warning
    assert app.session_state["aoi_geojson"] == flow.first
    assert app.session_state["analysis_status"] == "success"
    assert app.session_state["export_payloads"] == {"pdf": b"current"}
    assert app.session_state["location_center"] == before_center
    assert app.session_state["selection_map_revision"] == before_revision
    assert flow.single.call_count == 1


def test_replayed_deletion_does_not_resurrect_old_geometry(flow):
    select(flow, flow.first)
    flow.packet[0] = {"all_drawings": [], "last_active_drawing": flow.first}
    flow.app.run()
    flow.app.run()

    assert not flow.app.exception
    assert flow.app.session_state["aoi_geometry"] is None
    assert flow.app.session_state["aoi_geojson"] is None
    assert button(flow.app, "Analisar área").disabled


def test_empty_initial_payload_and_replays_do_not_erase_a_restored_polygon(flow):
    app = flow.app
    app.session_state["aoi_geojson"] = flow.first
    app.session_state["aoi_geometry"] = flow.geometries["first"]
    app.session_state["selection_map_seed"] = flow.first
    app.session_state["ignore_next_empty_drawings"] = True
    flow.packet[0] = {"all_drawings": None, "last_active_drawing": None}
    app.run()
    assert app.session_state["ignore_next_empty_drawings"] is True
    flow.packet[0] = {"all_drawings": [], "last_active_drawing": None}
    app.run()
    app.run()
    assert app.session_state["aoi_geojson"] == flow.first
    select(flow, flow.second)
    flow.packet[0] = {"all_drawings": [], "last_active_drawing": flow.second}
    app.run()
    assert app.session_state["aoi_geojson"] is None


def test_restored_polygon_can_be_registered_without_recalculating_geometry(flow, monkeypatch):
    select(flow, flow.first)
    app = flow.app
    app.session_state["selection_map_seed"] = flow.first
    app.session_state["selection_map_last_event"] = None
    app.session_state["ignore_next_empty_drawings"] = True
    convert = MagicMock(side_effect=AssertionError("Geometry must not be recalculated"))
    monkeypatch.setattr(main, "geojson_to_ee_geometry", convert)
    app.run()

    assert not app.exception
    assert not app.error
    assert app.session_state["ignore_next_empty_drawings"] is False
    assert app.session_state["aoi_geojson"] == flow.first
    assert flow.create_map.call_args.kwargs["geojson"] == flow.first
    convert.assert_not_called()
