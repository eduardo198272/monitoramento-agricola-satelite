import ee
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import date
import logging
import math

from src.app.utils import normalize_date

NASA_POWER_API = "https://power.larc.nasa.gov/api/temporal/daily/point"

COMMUNITY = "ag"
logger = logging.getLogger(__name__)


def finite_number(value):
    """Accept finite numbers only; no sentinel, boolean or invalid strings."""
    if value is None or isinstance(value, bool):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) and number != -999 else None


def radiation_to_mj(value, unit):
    """Normalize a declared daily energy unit; never infer it from magnitude."""
    number = finite_number(value)
    if number is None:
        return None
    normalized = str(unit or "").casefold().replace("²", "2").replace("^", "")
    normalized = normalized.replace(" ", "").replace("-hr", "h").replace("/dia", "/day")
    factor = {"mj/m2/day": 1.0, "kwh/m2/day": 3.6}.get(normalized)
    if factor is None:
        logger.warning("Radiação indisponível: unidade de origem ausente ou desconhecida.")
        return None
    return number * factor


def climate_records(data):
    """Produce export-safe records with explicitly normalized radiation."""
    units = {}
    if isinstance(data, pd.DataFrame):
        units = data.attrs.get("units", {})
        records = data.to_dict(orient="records")
    elif isinstance(data, dict):
        records = [data]
    elif isinstance(data, (list, tuple)):
        records = [record for record in data if isinstance(record, dict)]
    else:
        records = []
    result = []
    for record in records:
        row = dict(record)
        if "solar_radiation_mj_m2_day" in row:
            radiation = finite_number(row["solar_radiation_mj_m2_day"])
        else:
            radiation = radiation_to_mj(
                row.get("solar_radiation"),
                row.get("solar_radiation_unit", units.get("solar_radiation")),
            )
        row["solar_radiation_mj_m2_day"] = radiation
        result.append(row)
    return result

DEFAULT_PARAMETERS = ["PRECTOTCORR", "T2M", "ALLSKY_SFC_SW_DWN"]

PARAMETER_NAMES = {
    "PRECTOTCORR": "precipitation",
    "T2M": "temperature",
    "T2M_MAX": "temperature_max",
    "T2M_MIN": "temperature_min",
    "ALLSKY_SFC_SW_DWN": "solar_radiation",
}


def fetch_climate_data(
    geometry: ee.Geometry,
    start_date: str | date,
    end_date: str | date,
    parameters: list[str] = None,
    coordinates: tuple[float, float] | None = None,
) -> pd.DataFrame:
    start_date = normalize_date(start_date)
    end_date = normalize_date(end_date)
    if start_date > end_date:
        raise ValueError("A data inicial deve ser anterior ou igual à final")
    if parameters is None:
        parameters = DEFAULT_PARAMETERS.copy()

    if coordinates is None:
        centroid = geometry.centroid()
        coordinates = centroid.coordinates().getInfo()
    if coordinates is None:
        raise ValueError("Geometry does not have valid coordinates")

    longitude, latitude = coordinates[0], coordinates[1]

    params = {
        "community": COMMUNITY,
        "parameters": ",".join(parameters),
        "start": start_date.replace("-", ""),
        "end": end_date.replace("-", ""),
        "latitude": latitude,
        "longitude": longitude,
        "format": "JSON",
        "time-standard": "UTC",
    }

    response = requests.get(NASA_POWER_API, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    properties = data.get("properties", {})
    parameter_data = properties.get("parameter", {})
    radiation_unit = data.get("parameters", {}).get("ALLSKY_SFC_SW_DWN", {}).get("units")

    records = {}
    for param_code in parameters:
        param_mapping = parameter_data.get(param_code, {})
        for date_str, value in param_mapping.items():
            if date_str not in records:
                records[date_str] = {"date": date_str}
            mapped_name = PARAMETER_NAMES.get(param_code, param_code.lower())
            records[date_str][mapped_name] = finite_number(value)
            if param_code == "ALLSKY_SFC_SW_DWN":
                records[date_str]["solar_radiation_mj_m2_day"] = radiation_to_mj(value, radiation_unit)

    df = pd.DataFrame(list(records.values()))
    if "date" in df.columns:
        df = df.sort_values("date").reset_index(drop=True)
    df.attrs["units"] = {"solar_radiation": radiation_unit}
    df.attrs["warnings"] = []
    if "ALLSKY_SFC_SW_DWN" in parameters and radiation_to_mj(1, radiation_unit) is None:
        df.attrs["warnings"].append(
            "Radiação solar indisponível: unidade NASA POWER ausente ou não reconhecida."
        )

    return df


def plot_climate_data(climate_df: pd.DataFrame) -> go.Figure:
    if climate_df.empty:
        fig = go.Figure()
        fig.update_layout(
            title="Dados Climáticos - Precipitação e Temperatura",
            xaxis_title="Data",
        )
        return fig

    fig = go.Figure()

    if "precipitation" in climate_df.columns:
        fig.add_trace(go.Bar(
            x=climate_df["date"],
            y=climate_df["precipitation"],
            name="Precipitação",
            marker_color="#4C72B0",
            yaxis="y",
        ))

    if "temperature" in climate_df.columns:
        fig.add_trace(go.Scatter(
            x=climate_df["date"],
            y=climate_df["temperature"],
            name="Temperatura",
            mode="lines+markers",
            line=dict(color="#C44E52", width=2),
            marker=dict(size=6),
            yaxis="y2",
        ))

    fig.update_layout(
        title="Dados Climáticos - Precipitação e Temperatura",
        xaxis_title="Data",
        yaxis=dict(
            title="Precipitação (mm/dia)",
            side="left",
            showgrid=True,
        ),
        yaxis2=dict(
            title="Temperatura (°C)",
            side="right",
            overlaying="y",
            showgrid=False,
        ),
        template="plotly_white",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        hovermode="x unified",
    )

    return fig


def summarize_climate_data(climate_df: pd.DataFrame) -> dict:
    """
    Retorna resumo agregado dos dados climáticos.

    Args:
        climate_df: DataFrame com colunas opcionais 'precipitation', 'temperature',
                    radiação normalizada ou unidade de origem explícita.

    Returns:
        Dicionário com chaves:
        - total_precipitation_mm: soma de precipitação válida (mm)
        - mean_temperature_c: média de temperatura válida (°C)
        - mean_solar_radiation_mj_m2_day: média válida em MJ/m²/dia.
        Valores ausentes ou sem dados válidos resultam em None.
    """
    if climate_df is None or climate_df.empty:
        return {
            "total_precipitation_mm": None,
            "mean_temperature_c": None,
            "mean_solar_radiation_mj_m2_day": None,
        }

    result = {
        "total_precipitation_mm": None,
        "mean_temperature_c": None,
        "mean_solar_radiation_mj_m2_day": None,
    }

    if "precipitation" in climate_df.columns:
        valid_precip = climate_df["precipitation"].map(finite_number).dropna()
        if not valid_precip.empty:
            result["total_precipitation_mm"] = float(valid_precip.sum())

    if "temperature" in climate_df.columns:
        valid_temp = climate_df["temperature"].map(finite_number).dropna()
        if not valid_temp.empty:
            result["mean_temperature_c"] = float(valid_temp.mean())

    radiation = pd.Series(
        [record["solar_radiation_mj_m2_day"] for record in climate_records(climate_df)],
        dtype=float,
    ).dropna()
    if not radiation.empty:
        result["mean_solar_radiation_mj_m2_day"] = float(radiation.mean())

    return result
