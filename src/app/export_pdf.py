"""Three-page PDF reports for normalized agricultural analysis snapshots."""

from datetime import date, datetime
from io import BytesIO
import logging
import math
from typing import Any, Callable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from src.app.export_context import SUPPORTED_INDICES
from src.app.export_maps import StaticMapResult, render_static_index_map

logger = logging.getLogger(__name__)

PAGE_SIZE = landscape(A4)
PAGE_WIDTH, PAGE_HEIGHT = PAGE_SIZE
PAGE_MARGIN = 30
INDEX_COLORS = {"NDVI": "#238b45", "NDWI": "#2171b5", "NDMI": "#d95f0e"}


def _as_records(value: Any) -> list[dict]:
    if value is None:
        return []
    if hasattr(value, "to_dict"):
        try:
            records = value.to_dict(orient="records")
            if isinstance(records, list):
                return records
        except TypeError:
            pass
    if isinstance(value, dict):
        return [value]
    if isinstance(value, (list, tuple)):
        return [dict(item) for item in value if isinstance(item, dict)]
    return []


def _format_number(value: Any, decimals: int = 2) -> str | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    if not math.isfinite(value):
        return None
    return f"{value:.{decimals}f}"


def _draw_wrapped_text(pdf, text: str, x: float, y: float, max_width: float,
                       *, font="Helvetica", size=8, leading=10, max_lines=3):
    words = str(text).split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if pdf.stringWidth(candidate, font, size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(" .,;") + "..."
    pdf.setFont(font, size)
    for line in lines:
        pdf.drawString(x, y, line)
        y -= leading
    return y


def _plot_time_series(records: list[dict], index_name: str) -> bytes | None:
    points = []
    for record in records:
        value = _format_number(record.get("value"), decimals=8)
        date_value = record.get("date")
        if value is None or not date_value:
            continue
        try:
            parsed_date = datetime.fromisoformat(str(date_value)[:10])
        except ValueError:
            continue
        points.append((parsed_date, float(value)))
    if not points:
        return None

    figure, axis = plt.subplots(figsize=(5.4, 2.7), dpi=120)
    try:
        dates, values = zip(*points)
        axis.plot(
            dates,
            values,
            color=INDEX_COLORS[index_name],
            marker="o",
            markersize=3.5,
            linewidth=1.6,
        )
        axis.set_ylim(-1, 1)
        axis.set_ylabel(index_name, fontsize=8)
        axis.tick_params(axis="both", labelsize=7)
        axis.grid(True, linestyle="--", alpha=0.3)
        figure.autofmt_xdate(rotation=25, ha="right")
        figure.tight_layout(pad=1.1)
        buffer = BytesIO()
        figure.savefig(buffer, format="png", dpi=120, facecolor="white")
        return buffer.getvalue()
    finally:
        plt.close(figure)


def _resolve_static_map(
    index_result: dict,
    index_name: str,
    geometry: dict,
    map_renderer: Callable,
) -> StaticMapResult:
    prebuilt = index_result.get("static_map")
    if isinstance(prebuilt, StaticMapResult):
        return prebuilt
    if isinstance(prebuilt, bytes):
        return StaticMapResult("available", prebuilt, "")
    if isinstance(prebuilt, dict):
        return StaticMapResult(
            status=prebuilt.get("status", "unavailable"),
            image_bytes=prebuilt.get("image_bytes"),
            attribution=prebuilt.get("attribution", ""),
            error=prebuilt.get("error"),
        )
    try:
        result = map_renderer(
            index_result.get("index_map"), index_name, geometry,
            width=1000, height=680,
        )
        if isinstance(result, StaticMapResult):
            return result
        raise TypeError("O renderer do mapa retornou um resultado inválido")
    except Exception as error:
        logger.warning("Unable to render PDF map for %s", index_name, exc_info=True)
        return StaticMapResult("unavailable", None, "", str(error))


def _draw_metric(pdf, label: str, value: str, x: float, y: float) -> None:
    pdf.setFillColor(colors.HexColor("#52616b"))
    pdf.setFont("Helvetica", 8)
    pdf.drawString(x, y, label)
    pdf.setFillColor(colors.HexColor("#17252a"))
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(x, y - 15, value)


def _draw_page(
    pdf,
    context: dict,
    index_name: str,
    generated: str,
    map_renderer: Callable,
) -> None:
    result = context["indices"].get(index_name) or {}
    pdf.setFillColor(colors.HexColor(INDEX_COLORS[index_name]))
    pdf.rect(0, PAGE_HEIGHT - 8, PAGE_WIDTH, 8, stroke=0, fill=1)
    pdf.setFillColor(colors.HexColor("#142d4e"))
    pdf.setFont("Helvetica-Bold", 23)
    pdf.drawString(PAGE_MARGIN, PAGE_HEIGHT - 42, index_name)

    period = context.get("period") or {}
    period_label = (
        f"{period.get('start_date', 'indisponivel')} a "
        f"{period.get('end_date', 'indisponivel')}"
    )
    area = _format_number(context.get("area_ha"))
    area_label = f"{area} ha" if area is not None else "indisponivel"
    pdf.setFillColor(colors.HexColor("#52616b"))
    pdf.setFont("Helvetica", 8)
    pdf.drawString(PAGE_MARGIN, PAGE_HEIGHT - 59, f"Periodo: {period_label}")
    pdf.drawRightString(PAGE_WIDTH - PAGE_MARGIN, PAGE_HEIGHT - 59,
                        f"Gerado em: {generated}  |  Area: {area_label}")

    top = PAGE_HEIGHT - 84
    col_gap = 18
    left_width = 325
    right_x = PAGE_MARGIN + left_width + col_gap
    right_width = PAGE_WIDTH - PAGE_MARGIN - right_x
    _draw_metric(
        pdf, "Media do indice",
        _format_number(result.get("mean_value")) or "Indisponivel",
        PAGE_MARGIN, top,
    )
    _draw_metric(
        pdf, "Tendencia",
        str(result.get("trend")) if result.get("trend") is not None else "Indisponivel",
        PAGE_MARGIN + 112, top,
    )
    count = context.get("image_count")
    _draw_metric(
        pdf, "Imagens analisadas",
        str(count) if isinstance(count, (int, float)) and not isinstance(count, bool)
        else "Indisponivel",
        PAGE_MARGIN + 224, top,
    )

    climate = context.get("climate_summary")
    climate_y = top - 39
    pdf.setFillColor(colors.HexColor("#142d4e"))
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawString(PAGE_MARGIN, climate_y, "Contexto climatico")
    if isinstance(climate, dict) and climate:
        parts = []
        for key, suffix in (
            ("precipitation_mm", "mm"),
            ("temperature_c", "C"),
            ("solar_radiation_mj_m2_day", "MJ/m2/dia"),
        ):
            number = _format_number(climate.get(key))
            if number is not None:
                parts.append(f"{key.replace('_', ' ')}: {number} {suffix}")
        climate_text = " | ".join(parts) if parts else "Indisponivel"
    else:
        climate_text = "Indisponivel"
    _draw_wrapped_text(
        pdf, climate_text, PAGE_MARGIN, climate_y - 13, PAGE_WIDTH - 2 * PAGE_MARGIN,
        size=7.5, leading=9, max_lines=1,
    )

    section_y = climate_y - 39
    pdf.setFillColor(colors.HexColor("#142d4e"))
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(PAGE_MARGIN, section_y, "Serie temporal")
    records = _as_records(result.get("time_series"))
    chart = _plot_time_series(records, index_name)
    chart_x, chart_y, chart_width, chart_height = (
        PAGE_MARGIN, 106, left_width, 168
    )
    if chart:
        pdf.drawImage(
            ImageReader(BytesIO(chart)), chart_x, chart_y,
            width=chart_width, height=chart_height, preserveAspectRatio=True,
            anchor="c", mask="auto",
        )
        valid_dates = sorted(
            str(record.get("date"))[:10]
            for record in records
            if record.get("date") and _format_number(record.get("value"), 8) is not None
        )
        pdf.setFillColor(colors.HexColor("#52616b"))
        pdf.setFont("Helvetica", 6.5)
        pdf.drawString(
            chart_x, chart_y - 8,
            f"Amostras: {len(valid_dates)} | {valid_dates[0]} a {valid_dates[-1]}",
        )
    else:
        pdf.setFillColor(colors.HexColor("#687780"))
        pdf.setFont("Helvetica-Oblique", 9)
        pdf.drawString(chart_x, chart_y + chart_height / 2, "Serie temporal indisponivel")

    anomaly_y = 88
    pdf.setFillColor(colors.HexColor("#142d4e"))
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawString(PAGE_MARGIN, anomaly_y, "Anomalias")
    raw_anomalies = result.get("anomalies")
    anomalies = _as_records(raw_anomalies)
    if anomalies and any("anomaly" in item for item in anomalies):
        anomalies = [item for item in anomalies if item.get("anomaly") is True]
    if anomalies:
        anomaly_parts = []
        for anomaly in anomalies[:3]:
            value = _format_number(anomaly.get("value"))
            details = [str(anomaly.get("date", "data indisponivel"))]
            classification = anomaly.get("classification")
            if classification is not None:
                details.append(str(classification))
            z_score = _format_number(anomaly.get("z_score"))
            if z_score is not None:
                details.append(f"z={z_score}")
            if value is not None:
                details.append(value)
            anomaly_parts.append(" - ".join(details))
        if len(anomalies) > 3:
            anomaly_parts.append(f"+ {len(anomalies) - 3} outras")
        anomaly_text = "; ".join(anomaly_parts)
    elif result.get("anomalies") is not None:
        anomaly_text = "Nenhuma anomalia detectada"
    else:
        anomaly_text = "Indisponivel"
    _draw_wrapped_text(
        pdf, anomaly_text, PAGE_MARGIN, anomaly_y - 13, left_width,
        size=7.5, leading=9, max_lines=2,
    )

    pdf.setFillColor(colors.HexColor("#142d4e"))
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(right_x, section_y, "Mapa tematico")
    static_map = _resolve_static_map(
        result, index_name, context.get("geometry_geojson") or {}, map_renderer
    )
    map_x, map_y, map_width, map_height = right_x, 115, right_width, 310
    if static_map.status == "available" and static_map.image_bytes:
        try:
            image = Image.open(BytesIO(static_map.image_bytes)).convert("RGB")
            pdf.drawImage(
                ImageReader(image), map_x, map_y, width=map_width,
                height=map_height, preserveAspectRatio=True, anchor="c",
            )
            if static_map.attribution:
                pdf.setFillColor(colors.HexColor("#52616b"))
                pdf.setFont("Helvetica", 6)
                attribution = static_map.attribution[:180]
                pdf.drawRightString(map_x + map_width, map_y - 10, attribution)
        except Exception as error:
            logger.warning("Invalid static map image for %s", index_name, exc_info=True)
            static_map = StaticMapResult("unavailable", None, "", str(error))
    if static_map.status != "available" or not static_map.image_bytes:
        pdf.setStrokeColor(colors.HexColor("#cbd2d9"))
        pdf.setFillColor(colors.HexColor("#f4f6f8"))
        pdf.roundRect(map_x, map_y, map_width, map_height, 5, stroke=1, fill=1)
        pdf.setFillColor(colors.HexColor("#52616b"))
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawCentredString(map_x + map_width / 2, map_y + map_height / 2 + 8,
                              "Mapa indisponivel")
        if static_map.error:
            _draw_wrapped_text(
                pdf, static_map.error, map_x + 12, map_y + map_height / 2 - 10,
                map_width - 24, size=7, leading=9, max_lines=3,
            )

    pdf.setStrokeColor(colors.HexColor("#d7dee5"))
    pdf.line(PAGE_MARGIN, 24, PAGE_WIDTH - PAGE_MARGIN, 24)
    pdf.setFillColor(colors.HexColor("#687780"))
    pdf.setFont("Helvetica", 7)
    pdf.drawString(PAGE_MARGIN, 13, "Relatorio de monitoramento agricola - dados da analise")
    pdf.drawRightString(PAGE_WIDTH - PAGE_MARGIN, 13, f"{index_name} | {area_label}")
    pdf.showPage()


def render_analysis_pdf(
    export_context: dict,
    *,
    map_renderer: Callable | None = None,
    generated_at: date | datetime | None = None,
) -> bytes:
    """Render a three-page NDVI/NDWI/NDMI PDF without persisting files.

    A map renderer can be injected for offline use. If a prebuilt ``static_map``
    is present in the snapshot, it is reused instead of rendering a new one.
    """
    if not isinstance(export_context, dict):
        raise ValueError("O contexto de exportacao deve ser um dicionario")
    indices = export_context.get("indices")
    if not isinstance(indices, dict) or any(name not in indices for name in SUPPORTED_INDICES):
        raise ValueError("O contexto deve conter NDVI, NDWI e NDMI")

    generated_at = generated_at or datetime.now().date()
    generated_label = generated_at.isoformat()
    renderer = map_renderer or render_static_index_map
    output = BytesIO()
    pdf = canvas.Canvas(output, pagesize=PAGE_SIZE, pageCompression=0, invariant=1)
    pdf.setTitle("Relatorio de monitoramento agricola")
    pdf.setAuthor("Monitoramento Agricola por Satelite")
    for index_name in SUPPORTED_INDICES:
        _draw_page(pdf, export_context, index_name, generated_label, renderer)
    pdf.save()
    return output.getvalue()
