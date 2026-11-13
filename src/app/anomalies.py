import numpy as np


def detect_anomalies(
    time_series: list[dict],
    window_size: int = 3,
    std_threshold: float = 1.0
) -> list[dict]:
    if not time_series:
        return []

    result = []
    for i, point in enumerate(time_series):
        new_point = point.copy()
        new_point["anomaly"] = False
        new_point["z_score"] = 0.0

        if i < window_size:
            result.append(new_point)
            continue

        window = time_series[i - window_size:i]
        values = [p["value"] for p in window]
        mean_val = np.mean(values)
        std_val = np.std(values, ddof=0)

        if std_val == 0:
            result.append(new_point)
            continue

        z_score = (point["value"] - mean_val) / std_val
        new_point["z_score"] = float(z_score)

        if z_score < -std_threshold:
            new_point["anomaly"] = True

        result.append(new_point)

    return result


def generate_alert(anomalies: list[dict], index_name: str) -> str | None:
    anomaly_dates = [p["date"] for p in anomalies if p.get("anomaly", False)]
    if not anomaly_dates:
        return None
    return f"ALERTA: {len(anomaly_dates)} anomalia(s) detectada(s) no {index_name} em: {', '.join(anomaly_dates)}"


def compute_trend(time_series: list[dict]) -> str:
    if len(time_series) < 2:
        return "estável"

    values = np.array([p["value"] for p in time_series])
    x = np.arange(len(values))

    coeff = np.polyfit(x, values, 1)
    slope = coeff[0]

    if slope > 0.01:
        return "crescente"
    elif slope < -0.01:
        return "decrescente"
    else:
        return "estável"