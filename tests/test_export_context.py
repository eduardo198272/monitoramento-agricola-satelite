from copy import deepcopy
from datetime import date

import pandas as pd
import pytest

from src.app.export_context import ExportContextError, build_export_context


@pytest.fixture
def valid_inputs():
    ring = [[-52.0, -28.0], [-51.9, -28.0], [-51.9, -27.9], [-52.0, -28.0]]
    geometry = {"type": "Polygon", "coordinates": [ring]}
    analysis = {
        "success": True,
        "indices": {
            name: {
                "mean_value": 0.42,
                "time_series": [{"date": "2025-01-10", "value": 0.42}],
                "trend": "stable",
                "anomalies": [],
                "index_map": object(),
            }
            for name in ("NDVI", "NDWI", "NDMI")
        },
        "area_ha": 3.2,
        "image_count": 12,
        "climate_data": [],
        "climate_summary": {"precipitation_mm": None},
        "map_center": [-28.0, -51.95],
    }
    return analysis, geometry


def test_build_export_context_normalizes_dates_and_keeps_pipeline_data(valid_inputs):
    analysis, geometry = valid_inputs
    geometry["crs"] = {"type": "name", "properties": {"name": "EPSG:4326"}}
    analysis["collection_metadata"] = {"collection": "confirmed"}

    context = build_export_context(
        analysis, geometry, "2025-01-01", "2025-03-01"
    )

    assert context["period"] == {"start_date": "2025-01-01", "end_date": "2025-03-01"}
    assert context["geometry_geojson"] == geometry
    assert context["area_ha"] == 3.2
    assert context["map_center"] == [-28.0, -51.95]
    assert set(context["indices"]) == {"NDVI", "NDWI", "NDMI"}
    assert context["image_count"] == 12
    assert context["climate_summary"]["precipitation_mm"] is None
    assert context["geometry_geojson"]["crs"] == geometry["crs"]
    assert context["collection_metadata"] == analysis["collection_metadata"]


def test_build_export_context_does_not_mutate_inputs(valid_inputs):
    analysis, geometry = valid_inputs
    original_analysis = deepcopy({key: value for key, value in analysis.items() if key != "indices"})
    original_geometry = deepcopy(geometry)
    original_indices = {
        name: {key: value for key, value in result.items() if key != "index_map"}
        for name, result in analysis["indices"].items()
    }

    build_export_context(analysis, geometry, "2025-01-01", "2025-03-01")

    assert {key: value for key, value in analysis.items() if key != "indices"} == original_analysis
    assert geometry == original_geometry
    assert {
        name: {key: value for key, value in result.items() if key != "index_map"}
        for name, result in analysis["indices"].items()
    } == original_indices


def test_build_export_context_detaches_mutable_data_and_keeps_map_references(valid_inputs):
    analysis, geometry = valid_inputs
    analysis["indices"]["NDVI"]["time_series"].append(
        {"date": "20250111", "value": 0.5}
    )
    analysis["indices"]["NDVI"]["anomalies"].append(
        {"date": "20250111", "value": 0.5, "classification": "high"}
    )
    analysis["climate_data"] = pd.DataFrame(
        {"date": ["20250110", "20250111"], "precipitation": [2.5, None]}
    )

    context = build_export_context(analysis, geometry, "2025-01-01", "2025-03-01")

    assert (
        context["indices"]["NDVI"]["index_map"]
        is analysis["indices"]["NDVI"]["index_map"]
    )
    assert context["indices"]["NDVI"]["time_series"][1]["date"] == "2025-01-11"
    assert context["indices"]["NDVI"]["anomalies"][0]["date"] == "2025-01-11"
    assert context["climate_data"].loc[0, "date"] == "2025-01-10"
    assert pd.isna(context["climate_data"].loc[1, "precipitation"])

    context["indices"]["NDVI"]["time_series"][0]["value"] = 0.9
    context["climate_data"].loc[0, "precipitation"] = 99
    context["geometry_geojson"]["coordinates"][0][0][0] = -50
    assert analysis["indices"]["NDVI"]["time_series"][0]["value"] == 0.42
    assert analysis["climate_data"].loc[0, "precipitation"] == 2.5
    assert geometry["coordinates"][0][0][0] == -52.0


def test_build_export_context_preserves_optional_nulls_and_date_types(valid_inputs):
    analysis, geometry = valid_inputs
    analysis["area_ha"] = None
    analysis["indices"]["NDMI"]["time_series"] = [
        {"date": date(2025, 1, 10), "value": None}
    ]
    analysis["indices"]["NDWI"]["time_series"] = [{"date": None, "value": None}]

    context = build_export_context(
        analysis, geometry, date(2025, 1, 1), date(2025, 3, 1)
    )

    assert context["area_ha"] is None
    assert context["indices"]["NDMI"]["time_series"] == [
        {"date": "2025-01-10", "value": None}
    ]
    assert context["indices"]["NDMI"]["time_series"][0]["value"] is None
    assert context["indices"]["NDWI"]["time_series"][0]["date"] is None


@pytest.mark.parametrize(
    "date_value",
    ["20250230", "not-a-date", [1, 2]],
)
def test_build_export_context_rejects_invalid_tabular_dates(valid_inputs, date_value):
    analysis, geometry = valid_inputs
    analysis["indices"]["NDVI"]["time_series"] = [
        {"date": date_value, "value": 0.2}
    ]

    with pytest.raises(ExportContextError, match="Data tabular inválida"):
        build_export_context(analysis, geometry, "2025-01-01", "2025-03-01")


def test_build_export_context_copies_structures_and_preserves_missing_climate_dates(
    valid_inputs,
):
    analysis, geometry = valid_inputs
    analysis["map_center"] = (-28.0, -51.95)
    analysis["climate_data"] = pd.DataFrame(
        {"date": [pd.NaT], "precipitation": [None]}
    )
    analysis["climate_summary"] = {"observed_on": None, "tags": ("source",)}

    context = build_export_context(analysis, geometry, "2025-01-01", "2025-03-01")

    assert context["map_center"] == (-28.0, -51.95)
    assert pd.isna(context["climate_data"].loc[0, "precipitation"])
    assert pd.isna(context["climate_data"].loc[0, "date"])
    assert context["climate_summary"]["observed_on"] is None
    assert context["climate_summary"]["tags"] == ("source",)
    context["climate_summary"]["tags"] += ("changed",)
    assert analysis["climate_summary"]["tags"] == ("source",)


def test_build_export_context_copies_climate_frame_without_date_column(valid_inputs):
    analysis, geometry = valid_inputs
    analysis["climate_data"] = pd.DataFrame({"precipitation": [2.5]})

    context = build_export_context(analysis, geometry, "2025-01-01", "2025-03-01")

    assert context["climate_data"].equals(analysis["climate_data"])
    assert context["climate_data"] is not analysis["climate_data"]


@pytest.mark.parametrize(
    "mutate, message",
    [
        (lambda analysis: analysis.update(success=False), "sucesso"),
        (lambda analysis: analysis["indices"].pop("NDMI"), "NDMI"),
        (lambda analysis: analysis.update(indices={"NDVI": {}}), "multiíndice"),
        (lambda analysis: analysis["indices"].update(NDWI=None), "NDWI"),
        (lambda analysis: analysis["indices"].update(NDMI={}), "NDMI"),
    ],
)
def test_build_export_context_rejects_failed_or_incomplete_analysis(
    valid_inputs, mutate, message
):
    analysis, geometry = valid_inputs
    mutate(analysis)

    with pytest.raises(ExportContextError, match=message):
        build_export_context(analysis, geometry, "2025-01-01", "2025-03-01")


@pytest.mark.parametrize(
    "start_date, end_date",
    [
        ("not-a-date", "2025-03-01"),
        ("2025-02-01", "2025-01-01"),
    ],
)
def test_build_export_context_rejects_invalid_or_reversed_dates(
    valid_inputs, start_date, end_date
):
    analysis, geometry = valid_inputs

    with pytest.raises(ExportContextError, match="período|data"):
        build_export_context(analysis, geometry, start_date, end_date)


@pytest.mark.parametrize(
    "geometry",
    [
        None,
        {},
        {"type": "Point", "coordinates": [-52.0, -28.0]},
        {"type": "Polygon", "coordinates": []},
        {"type": "Polygon", "coordinates": [[[0, 0], [1, 1], [2, 2]]]},
        {"type": "Polygon", "coordinates": [[[0, 0], [1, 1], [2, 2], [0, 0]]]},
        {
            "type": "Polygon",
            "coordinates": [[[0, 0], [1, 1], [2, 2], [0, 0], [0, 0]]],
        },
        {"type": "Polygon", "coordinates": [[[0, 0], [1, 1], [2, 2], [0, 0.5]]]},
        {"type": "Polygon", "coordinates": [[[0, 0], [181, 1], [2, 2], [0, 0]]]},
        {"type": "Polygon", "coordinates": [[[0, 0], [True, 1], [2, 2], [0, 0]]]},
    ],
)
def test_build_export_context_rejects_missing_or_invalid_geometry(valid_inputs, geometry):
    analysis, _ = valid_inputs

    with pytest.raises(ExportContextError, match="geometria|GeoJSON"):
        build_export_context(analysis, geometry, "2025-01-01", "2025-03-01")


def test_build_export_context_rejects_non_mapping_indices(valid_inputs):
    analysis, geometry = valid_inputs
    analysis["indices"] = None

    with pytest.raises(ExportContextError, match="multiíndice"):
        build_export_context(analysis, geometry, "2025-01-01", "2025-03-01")
