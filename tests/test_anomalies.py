import pytest
from src.app.anomalies import detect_anomalies, generate_alert, compute_trend


class TestDetectAnomalies:
    def test_detect_anomalies_with_anomaly(self):
        time_series = [
            {"date": "2026-01-01", "value": 0.5},
            {"date": "2026-01-02", "value": 0.55},
            {"date": "2026-01-03", "value": 0.45},
            {"date": "2026-01-04", "value": 0.2},
            {"date": "2026-01-05", "value": 0.5},
        ]

        result = detect_anomalies(time_series, window_size=3, std_threshold=1.0)

        assert len(result) == 5
        assert result[3]["anomaly"] is True
        assert result[3]["z_score"] < -1.0
        assert result[0]["anomaly"] is False
        assert result[1]["anomaly"] is False
        assert result[2]["anomaly"] is False

    def test_detect_anomalies_no_anomaly(self):
        time_series = [
            {"date": "2026-01-01", "value": 0.5},
            {"date": "2026-01-02", "value": 0.5},
            {"date": "2026-01-03", "value": 0.5},
            {"date": "2026-01-04", "value": 0.5},
            {"date": "2026-01-05", "value": 0.5},
        ]

        result = detect_anomalies(time_series, window_size=3, std_threshold=1.0)

        assert all(not p["anomaly"] for p in result)

    def test_detect_anomalies_std_zero(self):
        time_series = [
            {"date": "2026-01-01", "value": 0.5},
            {"date": "2026-01-02", "value": 0.5},
            {"date": "2026-01-03", "value": 0.5},
            {"date": "2026-01-04", "value": 0.2},
        ]

        result = detect_anomalies(time_series, window_size=3, std_threshold=1.0)

        assert result[3]["anomaly"] is False

    def test_detect_anomalies_first_n_points_not_evaluated(self):
        time_series = [
            {"date": "2026-01-01", "value": 0.1},
            {"date": "2026-01-02", "value": 0.1},
            {"date": "2026-01-03", "value": 0.1},
        ]

        result = detect_anomalies(time_series, window_size=3, std_threshold=1.0)

        assert all(not p["anomaly"] for p in result)

    def test_detect_anomalies_empty_series(self):
        result = detect_anomalies([], window_size=3, std_threshold=1.0)
        assert result == []

    def test_detect_anomalies_custom_window_size(self):
        time_series = [
            {"date": "2026-01-01", "value": 0.5},
            {"date": "2026-01-02", "value": 0.55},
            {"date": "2026-01-03", "value": 0.45},
            {"date": "2026-01-04", "value": 0.5},
            {"date": "2026-01-05", "value": 0.5},
            {"date": "2026-01-06", "value": 0.1},
        ]

        result = detect_anomalies(time_series, window_size=5, std_threshold=1.0)

        assert result[5]["anomaly"] is True

    def test_detect_anomalies_positive_z_score_not_anomaly(self):
        time_series = [
            {"date": "2026-01-01", "value": 0.5},
            {"date": "2026-01-02", "value": 0.55},
            {"date": "2026-01-03", "value": 0.45},
            {"date": "2026-01-04", "value": 0.8},
        ]

        result = detect_anomalies(time_series, window_size=3, std_threshold=1.0)

        assert result[3]["anomaly"] is False
        assert result[3]["z_score"] > 0


class TestGenerateAlert:
    def test_generate_alert_with_anomalies(self):
        anomalies = [
            {"date": "2026-01-01", "value": 0.5, "anomaly": False},
            {"date": "2026-01-02", "value": 0.2, "anomaly": True},
            {"date": "2026-01-03", "value": 0.1, "anomaly": True},
        ]

        alert = generate_alert(anomalies, "NDVI")

        assert alert is not None
        assert "ALERTA" in alert
        assert "2 anomalia(s)" in alert
        assert "NDVI" in alert
        assert "2026-01-02" in alert
        assert "2026-01-03" in alert

    def test_generate_alert_no_anomalies(self):
        anomalies = [
            {"date": "2026-01-01", "value": 0.5, "anomaly": False},
            {"date": "2026-01-02", "value": 0.5, "anomaly": False},
        ]

        alert = generate_alert(anomalies, "NDVI")

        assert alert is None

    def test_generate_alert_empty_list(self):
        alert = generate_alert([], "NDVI")
        assert alert is None


class TestComputeTrend:
    def test_compute_trend_increasing(self):
        time_series = [
            {"date": "2026-01-01", "value": 0.2},
            {"date": "2026-01-02", "value": 0.4},
            {"date": "2026-01-03", "value": 0.6},
            {"date": "2026-01-04", "value": 0.8},
        ]

        trend = compute_trend(time_series)
        assert trend == "crescente"

    def test_compute_trend_decreasing(self):
        time_series = [
            {"date": "2026-01-01", "value": 0.8},
            {"date": "2026-01-02", "value": 0.6},
            {"date": "2026-01-03", "value": 0.4},
            {"date": "2026-01-04", "value": 0.2},
        ]

        trend = compute_trend(time_series)
        assert trend == "decrescente"

    def test_compute_trend_stable(self):
        time_series = [
            {"date": "2026-01-01", "value": 0.5},
            {"date": "2026-01-02", "value": 0.51},
            {"date": "2026-01-03", "value": 0.49},
            {"date": "2026-01-04", "value": 0.5},
        ]

        trend = compute_trend(time_series)
        assert trend == "estável"

    def test_compute_trend_insufficient_points(self):
        time_series = [{"date": "2026-01-01", "value": 0.5}]

        trend = compute_trend(time_series)
        assert trend == "estável"

    def test_compute_trend_empty_series(self):
        trend = compute_trend([])
        assert trend == "estável"

    def test_compute_trend_at_threshold(self):
        time_series = [
            {"date": "2026-01-01", "value": 0.0},
            {"date": "2026-01-02", "value": 0.01},
        ]

        trend = compute_trend(time_series)
        assert trend == "estável"