from datetime import date
from io import BytesIO
import re

from PIL import Image
import pytest
import pandas as pd
from reportlab.pdfgen import canvas

from src.app.export_maps import StaticMapResult
from src.app.export_pdf import render_analysis_pdf


@pytest.fixture
def export_context():
    return {
        "period": {"start_date": "2025-01-01", "end_date": "2025-03-31"},
        "area_ha": 3.2,
        "geometry_geojson": {
            "type": "Polygon",
            "coordinates": [[[-52, -28], [-51.9, -28], [-51.9, -27.9], [-52, -28]]],
        },
        "map_center": [-28.0, -51.95],
        "image_count": 12,
        "climate_summary": {"precipitation_mm": 82.5, "temperature_c": 23.1},
        "indices": {
            name: {
                "mean_value": value,
                "trend": "stable",
                "time_series": [
                    {"date": "2025-01-10", "value": value - 0.1},
                    {"date": "2025-02-10", "value": value},
                    {"date": "2025-03-10", "value": value + 0.1},
                ],
                "anomalies": [
                    {
                        "date": "2025-02-10",
                        "value": value,
                        "classification": "high",
                    }
                ],
                "index_map": object(),
            }
            for name, value in (("NDVI", 0.42), ("NDWI", 0.12), ("NDMI", 0.28))
        },
    }


def static_map_renderer(index_image, index_name, geometry_geojson, **kwargs):
    buffer = BytesIO()
    Image.new("RGB", (320, 220), (30, 90, 130)).save(buffer, format="PNG")
    return StaticMapResult(
        status="available",
        image_bytes=buffer.getvalue(),
        attribution="Test satellite attribution",
    )


def test_render_analysis_pdf_has_exactly_three_index_pages_in_fixed_order(
    export_context,
):
    pdf = render_analysis_pdf(
        export_context, map_renderer=static_map_renderer, generated_at=date(2025, 4, 1)
    )

    assert pdf.startswith(b"%PDF-")
    assert len(re.findall(rb"/Type\s*/Page\b", pdf)) == 3
    positions = [pdf.index(f"({name}) Tj".encode()) for name in ("NDVI", "NDWI", "NDMI")]
    assert positions == sorted(positions)


def test_pdf_pages_contain_real_metrics_dates_series_anomalies_and_map_attribution(
    export_context,
):
    pdf = render_analysis_pdf(
        export_context, map_renderer=static_map_renderer, generated_at=date(2025, 4, 1)
    )

    for text in (
        "2025-01-01 a 2025-03-31",
        "2025-04-01",
        "3.20 ha",
        "Media do indice",
        "0.42",
        "Tendencia",
        "stable",
        "2025-01-10",
        "Anomalias",
        "high",
        "82.50 mm",
        "Test satellite attribution",
    ):
        assert text.encode() in pdf


@pytest.mark.parametrize("missing", ["mean_value", "trend", "time_series", "anomalies"])
def test_pdf_identifies_unavailable_data_without_fabricating_values(
    export_context, missing
):
    export_context["indices"]["NDVI"].pop(missing)

    pdf = render_analysis_pdf(
        export_context, map_renderer=static_map_renderer, generated_at=date(2025, 4, 1)
    )

    assert b"indisponivel" in pdf.lower()
    assert len(re.findall(rb"/Type\s*/Page\b", pdf)) == 3


def test_pdf_marks_missing_map_and_continues_other_index_pages(export_context):
    def renderer(index_image, index_name, geometry_geojson, **kwargs):
        if index_name == "NDWI":
            return StaticMapResult(
                "unavailable", None, "Test satellite attribution", "tile failure"
            )
        return static_map_renderer(index_image, index_name, geometry_geojson, **kwargs)

    pdf = render_analysis_pdf(
        export_context, map_renderer=renderer, generated_at=date(2025, 4, 1)
    )

    assert b"Mapa indisponivel" in pdf
    assert b"tile failure" in pdf
    assert len(re.findall(rb"/Type\s*/Page\b", pdf)) == 3


def test_pdf_does_not_call_map_renderer_when_context_contains_prebuilt_map(
    export_context,
):
    export_context["indices"]["NDVI"]["static_map"] = static_map_renderer(
        None, "NDVI", export_context["geometry_geojson"]
    )

    def unexpected_renderer(*args, **kwargs):
        raise AssertionError("prebuilt map must be reused")

    pdf = render_analysis_pdf(
        export_context,
        map_renderer=unexpected_renderer,
        generated_at=date(2025, 4, 1),
    )

    assert pdf.startswith(b"%PDF-")


def test_pdf_shows_only_detected_anomalies_from_pipeline_records(export_context):
    export_context["indices"]["NDVI"]["anomalies"] = [
        {"date": "2025-01-10", "value": 0.32, "anomaly": False},
        {
            "date": "2025-02-10",
            "value": 0.22,
            "anomaly": True,
            "z_score": -1.5,
        },
    ]

    pdf = render_analysis_pdf(
        export_context, map_renderer=static_map_renderer, generated_at=date(2025, 4, 1)
    )

    assert b"2025-02-10" in pdf
    assert b"0.32" not in pdf
    assert b"z=-1.50" in pdf


def test_pdf_rejects_context_without_all_supported_indices(export_context):
    export_context["indices"].pop("NDMI")

    with pytest.raises(ValueError, match="NDVI, NDWI e NDMI"):
        render_analysis_pdf(export_context, map_renderer=static_map_renderer)


def test_pdf_uses_injected_renderer_and_never_performs_http_requests(
    export_context, monkeypatch
):
    import requests

    monkeypatch.setattr(
        requests, "get", lambda *args, **kwargs: pytest.fail("HTTP request")
    )
    renderer_calls = []

    def renderer(index_image, index_name, geometry_geojson, **kwargs):
        renderer_calls.append(index_name)
        return static_map_renderer(index_image, index_name, geometry_geojson, **kwargs)

    pdf = render_analysis_pdf(
        export_context, map_renderer=renderer, generated_at=date(2025, 4, 1)
    )

    assert pdf.startswith(b"%PDF-")
    assert renderer_calls == ["NDVI", "NDWI", "NDMI"]


def test_pdf_normalizes_tabular_records_and_rejects_invalid_numbers():
    from src.app.export_pdf import _as_records, _format_number, _plot_time_series

    assert _as_records(pd.DataFrame([{"date": "2025-01-01", "value": 0.2}])) == [
        {"date": "2025-01-01", "value": 0.2}
    ]
    assert _as_records({"date": "2025-01-01"}) == [{"date": "2025-01-01"}]
    assert _as_records(({"value": 1}, "ignored")) == [{"value": 1}]
    assert _as_records(None) == []
    assert _as_records("unsupported") == []
    assert _format_number(0.25) == "0.25"
    assert _format_number(True) is None
    assert _format_number(float("inf")) is None
    assert _plot_time_series([], "NDVI") is None
    assert _plot_time_series(
        [{"date": "bad-date", "value": 0.2}, {"date": "2025-01-01", "value": None}],
        "NDVI",
    ) is None

    class BrokenTable:
        def to_dict(self, **kwargs):
            raise TypeError("not tabular")

    class NonRecordTable:
        def to_dict(self, **kwargs):
            return None

    assert _as_records(BrokenTable()) == []
    assert _as_records(NonRecordTable()) == []


def test_pdf_map_resolution_handles_prebuilt_bytes_dict_and_bad_renderer():
    from src.app.export_pdf import _resolve_static_map

    assert _resolve_static_map(
        {"static_map": b"png"}, "NDVI", {}, lambda *args, **kwargs: None
    ).image_bytes == b"png"
    dictionary_map = _resolve_static_map(
        {"static_map": {"status": "unavailable", "error": "missing"}},
        "NDVI", {}, lambda *args, **kwargs: None,
    )
    assert dictionary_map.status == "unavailable"
    failed = _resolve_static_map(
        {}, "NDVI", {}, lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("offline"))
    )
    assert failed.status == "unavailable"
    assert failed.error == "offline"
    invalid = _resolve_static_map(
        {}, "NDVI", {}, lambda *args, **kwargs: object()
    )
    assert "resultado inválido" in invalid.error


def test_pdf_wraps_long_text_and_handles_empty_text():
    from src.app.export_pdf import _draw_wrapped_text

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    end_y = _draw_wrapped_text(
        pdf, "texto longo que precisa ser truncado no espaço disponível",
        10, 100, 25, size=8, max_lines=1,
    )
    assert end_y == 90
    assert _draw_wrapped_text(pdf, "", 10, 100, 25) == 100
    _draw_wrapped_text(pdf, "extraordinarilylongword", 10, 100, 1)


def test_pdf_handles_empty_context_sections_and_corrupt_map(export_context):
    export_context["climate_summary"] = {}
    export_context["image_count"] = None
    export_context["area_ha"] = None
    export_context["indices"]["NDVI"]["time_series"] = []
    export_context["indices"]["NDVI"]["anomalies"] = None
    export_context["indices"]["NDVI"]["static_map"] = b"not-a-png"

    pdf = render_analysis_pdf(
        export_context, map_renderer=static_map_renderer, generated_at=date(2025, 4, 1)
    )

    assert len(re.findall(rb"/Type\s*/Page\b", pdf)) == 3
    assert b"Serie temporal indisponivel" in pdf
    assert b"Mapa indisponivel" in pdf


def test_pdf_summarizes_more_than_three_detected_anomalies(export_context):
    export_context["indices"]["NDVI"]["anomalies"] = [
        {
            "date": f"2025-02-{day:02}",
            "value": None if day == 1 else 0.2,
            "classification": "high",
        }
        for day in range(1, 5)
    ]

    pdf = render_analysis_pdf(
        export_context, map_renderer=static_map_renderer, generated_at=date(2025, 4, 1)
    )

    assert b"+ 1 outras" in pdf


def test_pdf_reports_empty_anomaly_list_as_no_detected_anomalies(export_context):
    export_context["indices"]["NDVI"]["anomalies"] = []

    pdf = render_analysis_pdf(
        export_context, map_renderer=static_map_renderer, generated_at=date(2025, 4, 1)
    )

    assert b"Nenhuma anomalia detectada" in pdf


def test_pdf_handles_empty_map_attribution_and_unavailable_map_without_error(
    export_context,
):
    export_context["indices"]["NDVI"]["static_map"] = static_map_renderer(
        None, "NDVI", export_context["geometry_geojson"]
    ).image_bytes
    export_context["indices"]["NDWI"]["static_map"] = {
        "status": "unavailable", "error": None
    }

    pdf = render_analysis_pdf(
        export_context, map_renderer=static_map_renderer, generated_at=date(2025, 4, 1)
    )

    assert len(re.findall(rb"/Type\s*/Page\b", pdf)) == 3


def test_pdf_rejects_non_dictionary_context():
    with pytest.raises(ValueError, match="dicionario"):
        render_analysis_pdf(None, map_renderer=static_map_renderer)
