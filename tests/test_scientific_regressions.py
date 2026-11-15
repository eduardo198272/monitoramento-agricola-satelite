"""Contract regressions: controlled inputs, never participant or field evidence."""

from datetime import date
from io import BytesIO
import json
from pathlib import Path
from unittest.mock import MagicMock, patch
import zipfile
import csv
import io

import openpyxl
import pandas as pd
import pytest

from src.app import climate, earth_engine, main, map_interaction
from src.app.export_csv import render_analysis_csv_zip
from src.app.export_xlsx import render_analysis_xlsx


@pytest.mark.parametrize("unit,factor", [
    ("MJ/m^2/day", 1), ("MJ/m²/dia", 1), ("kW-hr/m^2/day", 3.6),
    ("kWh/m²/day", 3.6), (None, None), ("W/m2", None),
])
def test_radiation_respects_response_units(unit, factor):
    payload = json.loads(
        Path("docs/artigo_final/evidencias/nasa_power_unidades.json").read_text()
    )
    if unit is None:
        payload["parameters"]["ALLSKY_SFC_SW_DWN"].pop("units")
    else:
        payload["parameters"]["ALLSKY_SFC_SW_DWN"]["units"] = unit
    response = MagicMock()
    response.json.return_value = payload
    with patch.object(climate.requests, "get", return_value=response):
        frame = climate.fetch_climate_data(None, "2025-01-01", "2025-01-02",
                                          coordinates=(-52, -28))
    summary = climate.summarize_climate_data(frame)
    if factor is None:
        assert summary["mean_solar_radiation_mj_m2_day"] is None
        assert frame.attrs["warnings"]
    else:
        assert summary["mean_solar_radiation_mj_m2_day"] == pytest.approx(21.315 * factor)


def test_exports_never_assume_unit_for_unlabelled_radiation():
    context = {
        "indices": {"NDVI": {"time_series": [], "anomalies": []}},
        "climate_data": [{"date": "2025-01-01", "solar_radiation": 21.64}],
    }
    workbook = openpyxl.load_workbook(BytesIO(render_analysis_xlsx(context)))
    assert workbook["Clima"]["D2"].value is None
    with zipfile.ZipFile(BytesIO(render_analysis_csv_zip(context))) as archive:
        rows = list(csv.DictReader(io.StringIO(archive.read("clima.csv").decode())))
    assert rows[0]["solar_radiation_mj_m2_day"] == ""


def test_end_date_is_inclusive_even_for_one_day():
    with patch.object(earth_engine, "ee") as ee:
        collection = MagicMock()
        earth_engine.filter_by_date(collection, date(2024, 2, 29), date(2024, 2, 29))
        ee.Filter.date.assert_called_once_with("2024-02-29", "2024-03-01")


def test_component_receives_exact_negative_tile_range(monkeypatch):
    component = MagicMock()
    monkeypatch.setattr(map_interaction, "_index_hover_component", component)
    grid = {"indices": {"NDWI": {"minimum": -0.6, "maximum": -0.1}}}
    map_interaction.render_index_hover_map(
        tile_url="tiles", center=[-28, -52], zoom=12, geojson=None,
        index_name="NDWI", palette=["white", "blue"], value_grid=grid, key="map",
    )
    assert component.call_args.kwargs["range"] == [-0.6, -0.1]


@pytest.mark.parametrize("changed", ["start_date", "end_date", "indices", "geometry"])
def test_analytical_changes_invalidate_all_products(monkeypatch, changed):
    snapshot = {
        "analysis": {"indices": {"NDVI": {}}},
        "geometry_geojson": {"type": "Polygon"},
        "start_date": date(2025, 1, 1), "end_date": date(2025, 2, 1),
    }
    state = {
        "analysis_snapshot": snapshot, "aoi_geojson": snapshot["geometry_geojson"],
        "analysis_start_date": snapshot["start_date"], "analysis_end_date": snapshot["end_date"],
        "selected_indices": ["NDVI"], "analysis_results": {"NDVI": {}},
        "export_payloads": {"pdf": b"old"}, "index_value_grid": {"old": True},
        "index_tile_urls": {"NDVI": "old"}, "analysis_status": "success",
    }
    if changed == "start_date":
        state["analysis_start_date"] = date(2025, 1, 2)
    elif changed == "end_date":
        state["analysis_end_date"] = date(2025, 2, 2)
    elif changed == "indices":
        state["selected_indices"] = ["NDWI"]
    else:
        state["aoi_geojson"] = {"type": "Polygon", "coordinates": []}
    # Attribute/dict interface equivalent to the isolated state used by Streamlit.
    class State(dict):
        __getattr__ = dict.__getitem__
        __setattr__ = dict.__setitem__
    monkeypatch.setattr(main.st, "session_state", State(state))
    assert main.invalidate_changed_analysis() is True
    assert main.st.session_state.analysis_results == {}
    assert main.st.session_state.export_payloads == {}
    assert main.st.session_state.index_value_grid is None
    assert main.st.session_state.index_tile_urls == {}


def test_visual_selection_does_not_invalidate(monkeypatch):
    class State(dict):
        __getattr__ = dict.__getitem__
        __setattr__ = dict.__setitem__
    snapshot = {"analysis": {"indices": {"NDVI": {}, "NDWI": {}}},
                "geometry_geojson": {}, "start_date": "2025-01-01", "end_date": "2025-02-01"}
    state = State(analysis_snapshot=snapshot, aoi_geojson={},
                  analysis_start_date="2025-01-01", analysis_end_date="2025-02-01",
                  selected_indices=["NDVI", "NDWI"], visible_index_control="NDWI")
    monkeypatch.setattr(main.st, "session_state", state)
    assert main.invalidate_changed_analysis() is False
    assert state.analysis_snapshot is snapshot


def test_same_date_observations_keep_distinct_anomaly_flags():
    records = [
        {"date": "2025-01-01", "value": 0.6, "observation_id": "tile-a"},
        {"date": "2025-01-01", "value": 0.2, "observation_id": "tile-b"},
    ]
    result = {"time_series": records, "anomalies": [
        {**records[0], "anomaly": False}, {**records[1], "anomaly": True},
    ]}
    context = {"indices": {"NDVI": result}}
    workbook = openpyxl.load_workbook(BytesIO(render_analysis_xlsx(context)))
    assert [workbook["NDVI"][f"D{row}"].value for row in (2, 3)] == [False, True]
    with zipfile.ZipFile(BytesIO(render_analysis_csv_zip(context))) as archive:
        rows = list(csv.DictReader(io.StringIO(archive.read("ndvi.csv").decode())))
    assert [row["anomaly"] for row in rows] == ["false", "true"]
    assert [row["observation_id"] for row in rows] == ["tile-a", "tile-b"]


def test_invalid_climate_and_explicit_source_units():
    assert climate.climate_records({"solar_radiation": 2, "solar_radiation_unit": "kWh/m²/day"})[0]["solar_radiation_mj_m2_day"] == 7.2
    assert climate.climate_records("not records") == []
    assert climate.climate_records(({"solar_radiation_mj_m2_day": 21.64}, "bad"))[0]["solar_radiation_mj_m2_day"] == 21.64
    for value in [None, True, "bad", float("inf"), float("nan"), -999]:
        assert climate.finite_number(value) is None
    assert climate.finite_number("21.64") == 21.64
    with pytest.raises(ValueError, match="data inicial"):
        climate.fetch_climate_data(None, "2025-02-01", "2025-01-01")


def test_climate_warnings_are_visible(monkeypatch):
    ui = MagicMock()
    monkeypatch.setattr(main, "st", ui)
    main.display_analysis_details("NDVI", {"climate_warnings": ["Unidade desconhecida"]}, None)
    ui.warning.assert_called_once_with("Unidade desconhecida")


def test_series_preserves_acquisition_ids(monkeypatch):
    from src.app import time_series
    ee = MagicMock()
    feature = MagicMock()
    feature.toDictionary.return_value.getInfo.return_value = {
        "date": "2025-01-01", "value": 0.6, "observation_id": "tile-a",
    }
    ee.Feature.return_value = feature
    monkeypatch.setattr(time_series, "ee", ee)
    result = time_series.compute_time_series(MagicMock(), MagicMock(), "NDVI", image_count=1)
    assert result == [{"date": "2025-01-01", "value": 0.6, "observation_id": "tile-a"}]


def test_csv_record_dict_is_preserved():
    from src.app.export_csv import _records
    assert _records({"value": 0.4}) == [{"value": 0.4}]
    assert _records(pd.DataFrame([{"value": 0.4}])) == [{"value": 0.4}]


def test_single_and_multi_share_metadata_without_duplicate_climate_calls(monkeypatch):
    from src.app import pipeline
    collection = MagicMock()
    collection.size.return_value.getInfo.return_value = 2
    image = collection.map.return_value.median.return_value
    image.select.return_value.reduceRegion.return_value.getInfo.return_value = {
        "NDVI": 0.55, "NDWI": 0.1, "NDMI": 0.2,
    }
    geometry = MagicMock()
    geometry.centroid.return_value.coordinates.return_value.getInfo.return_value = [-52, -28]
    frame = pd.DataFrame({"date": ["20250101", "20250102"],
                          "precipitation": [2, 3], "temperature": [20, 22],
                          "solar_radiation_mj_m2_day": [21.64, 20.99]})
    fetch = MagicMock(return_value=frame)
    monkeypatch.setattr(pipeline, "get_image_collection", lambda *a: collection)
    monkeypatch.setattr(pipeline, "fetch_climate_data", fetch)
    monkeypatch.setattr(pipeline, "compute_time_series", lambda *a, **k: [
        {"date": "2025-01-01", "value": 0.5}, {"date": "2025-01-02", "value": 0.6},
    ])
    single = pipeline.run_analysis(geometry, "2025-01-01", "2025-01-02", "NDVI", area_ha=2)
    fetch.reset_mock()
    multi = pipeline.run_multi_analysis(geometry, "2025-01-01", "2025-01-02",
                                       ["NDVI", "NDWI", "NDMI"], area_ha=2)
    fetch.assert_called_once()
    assert single["success"] and multi["success"]
    assert single["image_count"] == multi["image_count"] == 2
    assert single["trend"] == multi["indices"]["NDVI"]["trend"] == "crescente"
    assert single["climate_summary"] == multi["climate_summary"]
    assert single["climate_summary"]["mean_solar_radiation_mj_m2_day"] == pytest.approx(21.315)


def test_multi_summary_reaches_cards_without_mutation(monkeypatch):
    class State(dict):
        __getattr__ = dict.__getitem__
        __setattr__ = dict.__setitem__
    summary = {"total_precipitation_mm": 5, "mean_temperature_c": 21,
               "mean_solar_radiation_mj_m2_day": 21.315}
    state = State(
        analysis_results={"NDVI": {"mean_value": 0.6, "time_series": []}},
        analysis_metadata={"climate_summary": summary}, visible_index="NDVI",
        visible_index_control="NDVI",
    )
    ui = MagicMock()
    ui.session_state = state
    monkeypatch.setattr(main, "st", ui)
    detail = MagicMock()
    monkeypatch.setattr(main, "display_analysis_details", detail)
    monkeypatch.setattr(main, "display_summary", MagicMock())
    main.render_results_panels()
    assert detail.call_args.args[1]["climate_summary"] == summary
    assert "climate_summary" not in state.analysis_results["NDVI"]


def test_historical_radiation_is_consistent_in_all_export_formats():
    from src.app.export_pdf import render_analysis_pdf, _format_number
    from src.app.export_maps import StaticMapResult
    payload = json.loads(Path("docs/artigo_final/evidencias/nasa_power_unidades.json").read_text())
    response = MagicMock()
    response.json.return_value = payload
    with patch.object(climate.requests, "get", return_value=response):
        frame = climate.fetch_climate_data(None, "2025-01-01", "2025-01-02", coordinates=(-52, -28))
    summary = climate.summarize_climate_data(frame)
    context = {"indices": {"NDVI": {"time_series": [], "anomalies": []}},
               "climate_data": frame, "climate_summary": summary}
    workbook = openpyxl.load_workbook(BytesIO(render_analysis_xlsx(context)))
    assert workbook["Clima"]["D2"].value == 21.64
    assert workbook["Clima"]["D3"].value == 20.99
    with zipfile.ZipFile(BytesIO(render_analysis_csv_zip(context))) as archive:
        rows = list(csv.DictReader(io.StringIO(archive.read("clima.csv").decode())))
    assert [float(row["solar_radiation_mj_m2_day"]) for row in rows] == [21.64, 20.99]
    pdf = render_analysis_pdf(
        context, map_renderer=lambda *a, **k: StaticMapResult("unavailable", None, "")
    )
    assert _format_number(summary["mean_solar_radiation_mj_m2_day"]).encode() in pdf
    assert b"76.73" not in pdf
