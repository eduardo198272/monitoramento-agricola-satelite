from datetime import date
from unittest.mock import MagicMock

import pytest

import src.app.main as main_module


class SessionState(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as error:
            raise AttributeError(name) from error

    def __setattr__(self, name, value):
        self[name] = value


@pytest.fixture
def ui(monkeypatch):
    state = SessionState(
        analysis_status="success",
        analysis_mode="multi",
        selected_indices=["NDVI", "NDWI", "NDMI"],
        analysis_start_date=date(2025, 1, 1),
        analysis_end_date=date(2025, 3, 31),
        aoi_geojson={
            "type": "Polygon",
            "coordinates": [[[-52.0, -28.0], [-51.9, -28.0], [-51.9, -27.9], [-52.0, -27.9], [-52.0, -28.0]]],
        },
        analysis_snapshot={
            "analysis": {
                "success": True,
                "indices": {name: {"index_map": object(), "time_series": [], "anomalies": []}
                            for name in ("NDVI", "NDWI", "NDMI")},
            },
            "geometry_geojson": {
                "type": "Polygon",
                "coordinates": [[[-52.0, -28.0], [-51.9, -28.0], [-51.9, -27.9], [-52.0, -27.9], [-52.0, -28.0]]],
            },
            "start_date": date(2025, 1, 1),
            "end_date": date(2025, 3, 31),
        },
        export_payloads={},
    )
    stub = MagicMock()
    stub.session_state = state
    monkeypatch.setattr(main_module, "st", stub)
    return stub, state


def test_export_actions_are_hidden_for_single_index_analysis(ui):
    stub, state = ui
    state.analysis_mode = "single"

    main_module.render_export_actions()

    stub.download_button.assert_not_called()
    assert any("multiíndice" in str(call.args[0]).lower() for call in stub.info.call_args_list)


@pytest.mark.parametrize("state_changes", [
    {"analysis_status": "idle"},
    {"analysis_snapshot": None},
])
def test_export_actions_require_current_successful_snapshot(ui, state_changes):
    stub, state = ui
    state.update(state_changes)

    main_module.render_export_actions()

    stub.button.assert_not_called()
    stub.download_button.assert_not_called()


@pytest.mark.parametrize("invalid_snapshot", ["missing_index", "missing_geometry"])
def test_export_actions_are_hidden_for_incomplete_snapshot(ui, invalid_snapshot):
    stub, state = ui
    if invalid_snapshot == "missing_index":
        state.analysis_snapshot["analysis"]["indices"].pop("NDMI")
    else:
        state.analysis_snapshot["geometry_geojson"] = None

    main_module.render_export_actions()

    stub.button.assert_not_called()
    assert any("incompleta" in str(call.args[0]).lower() for call in stub.info.call_args_list)


@pytest.mark.parametrize("changed_field, changed_value", [
    ("analysis_start_date", date(2025, 1, 2)),
    ("analysis_end_date", date(2025, 4, 1)),
    ("aoi_geojson", {"type": "Polygon", "coordinates": [[1]]}),
])
def test_export_actions_reject_snapshot_that_does_not_match_current_inputs(
    ui, changed_field, changed_value
):
    stub, state = ui
    setattr(state, changed_field, changed_value)

    main_module.render_export_actions()

    stub.download_button.assert_not_called()
    assert any("nova análise" in str(call.args[0]).lower() for call in stub.info.call_args_list)


def test_export_generation_is_on_demand_and_downloads_cached_payload(ui, monkeypatch):
    stub, state = ui
    context_builder = MagicMock(return_value={"indices": {}})
    pdf_builder = MagicMock(return_value=b"pdf-data")
    monkeypatch.setattr(main_module, "build_export_context", context_builder)
    monkeypatch.setattr(main_module, "render_analysis_pdf", pdf_builder)
    stub.button.return_value = False

    main_module.render_export_actions()

    pdf_builder.assert_not_called()

    # The PDF generation control is clicked; other format controls are not.
    stub.button.side_effect = [True, False, False]
    main_module.render_export_actions()

    pdf_builder.assert_called_once_with(context_builder.return_value)
    context_builder.assert_called_once()
    assert state.export_payloads["pdf"] == b"pdf-data"

    stub.download_button.reset_mock()
    stub.button.side_effect = [False, False]
    main_module.render_export_actions()

    assert any(call.kwargs.get("data") == b"pdf-data" for call in stub.download_button.call_args_list)
    pdf_builder.assert_called_once()


def test_export_builder_failure_is_reported_and_does_not_remove_analysis(ui, monkeypatch):
    stub, state = ui
    monkeypatch.setattr(main_module, "build_export_context", MagicMock(return_value={}))
    monkeypatch.setattr(
        main_module, "render_analysis_xlsx", MagicMock(side_effect=RuntimeError("xlsx failed"))
    )
    stub.button.side_effect = [False, True, False]

    main_module.render_export_actions()

    stub.error.assert_called_once()
    assert state.analysis_status == "success"
    assert state.analysis_snapshot is not None
    assert "xlsx" not in state.export_payloads


def test_clear_analysis_state_invalidates_export_snapshot(stub_streamlit=None):
    state = SessionState(
        analysis_results={"NDVI": {}}, analysis_metadata={"image_count": 1},
        analysis_snapshot={"analysis": {}}, export_payloads={"pdf": b"old"},
        analysis_status="success", analysis_error=None, analysis_map=None,
        analysis_map_center=None, index_value_grid=None, index_preload_error=None,
        index_tile_urls={},
    )
    original = main_module.st
    main_module.st = MagicMock(session_state=state)
    try:
        main_module.clear_analysis_state()
    finally:
        main_module.st = original

    assert state.analysis_snapshot is None
    assert state.export_payloads == {}
