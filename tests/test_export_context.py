from copy import deepcopy

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
    ],
)
def test_build_export_context_rejects_missing_or_invalid_geometry(valid_inputs, geometry):
    analysis, _ = valid_inputs

    with pytest.raises(ExportContextError, match="geometria|GeoJSON"):
        build_export_context(analysis, geometry, "2025-01-01", "2025-03-01")
