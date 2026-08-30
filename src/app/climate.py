import ee
import requests
import pandas as pd
import plotly.graph_objects as go

NASA_POWER_API = "https://power.larc.nasa.gov/api/temporal/daily/point"

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
    start_date: str,
    end_date: str,
    parameters: list[str] = None
) -> pd.DataFrame:
    if parameters is None:
        parameters = DEFAULT_PARAMETERS.copy()

    centroid = geometry.centroid()
    coords = centroid.coordinates().getInfo()
    if coords is None:
        raise ValueError("Geometry does not have valid coordinates")

    longitude, latitude = coords[0], coords[1]

    params = {
        "parameters": ",".join(parameters),
        "start": start_date.replace("-", ""),
        "end": end_date.replace("-", ""),
        "latitude": latitude,
        "longitude": longitude,
        "format": "JSON",
    }

    response = requests.get(NASA_POWER_API, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    properties = data.get("properties", {})
    parameter_data = properties.get("parameter", {})

    records = {}
    for param_code in parameters:
        param_mapping = parameter_data.get(param_code, {})
        for date_str, value in param_mapping.items():
            if date_str not in records:
                records[date_str] = {"date": date_str}
            mapped_name = PARAMETER_NAMES.get(param_code, param_code.lower())
            records[date_str][mapped_name] = None if value == -999 else value

    df = pd.DataFrame(list(records.values()))
    if "date" in df.columns:
        df = df.sort_values("date").reset_index(drop=True)

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
