#!/usr/bin/env python
"""Script de validacao dos cenarios de cultura do MVP."""

import sys
import os
from pathlib import Path
from datetime import date, timedelta

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

import ee
import pandas as pd
import plotly.graph_objects as go


SOJA_CENTER = [-50.5, -15.5]
MILHO_CENTER = [-52.0, -25.0]
PASTAGEM_CENTER = [-50.0, -16.5]

SOJA_PERIOD = ("2024-07-01", "2024-11-30")
MILHO_PERIOD = ("2024-07-01", "2024-11-30")
PASTAGEM_PERIOD = ("2024-01-01", "2024-06-30")


def print_header(text: str) -> None:
    print(f"\n{'=' * 50}")
    print(f" {text}")
    print(f"{'=' * 50}")


def print_result(name: str, success: bool, details: str = "") -> None:
    status = "[OK]" if success else "[FAIL]"
    print(f"  {name}: {status}")
    if details:
        print(f"         {details}")


def create_test_geometry(center: list, size_km: float = 1.0) -> ee.Geometry:
    """Cria geometria de teste centered em coords."""
    half_deg = size_km / 111.0
    coords = [
        [center[0] - half_deg, center[1] - half_deg],
        [center[0] + half_deg, center[1] - half_deg],
        [center[0] + half_deg, center[1] + half_deg],
        [center[0] - half_deg, center[1] + half_deg],
        [center[0] - half_deg, center[1] - half_deg],
    ]
    return ee.Geometry.Polygon([coords])


def validate_soja() -> bool:
    print_header("Cenario Soja")

    try:
        from src.app.ee_auth import initialize_earth_engine
        from src.app.earth_engine import get_image_collection, calculate_ndvi, mask_clouds
        from src.app.time_series import compute_time_series
        from src.app.anomalies import compute_trend

        initialize_earth_engine()

        geometry = create_test_geometry(SOJA_CENTER, size_km=1.0)

        collection = get_image_collection(geometry, SOJA_PERIOD[0], SOJA_PERIOD[1])

        if collection.size().getInfo() == 0:
            print_result("Imagens encontradas", False, "Nenhuma imagem")
            return False

        collection = collection.map(mask_clouds)
        index_collection = collection.map(calculate_ndvi)

        time_series = compute_time_series(
            index_collection, geometry, "NDVI", scale=100
        )

        if len(time_series) < 5:
            print_result("Dados suficientes", False, f"Só {len(time_series)} pontos")
            return False

        values = [p["value"] for p in time_series]
        mean_value = sum(values) / len(values)
        min_value = min(values)
        max_value = max(values)
        trend = compute_trend(time_series)

        print_result("Imagens encontradas", True, f"{len(time_series)} pontos")
        print_result("NDVI medio", True, f"{mean_value:.3f}")
        print_result("NDVI min", True, f"{min_value:.3f}")
        print_result("NDVI max", True, f"{max_value:.3f}")
        print_result("Tendência", True, trend)

        valid_max = 0.50 <= max_value <= 0.95
        valid_min = 0.15 <= min_value <= 0.60
        valid_trend = trend in ["crescente", "estável", "decrescente"]

        print_result("NDVI max valido (0.50-0.95)", valid_max,
                     f"{max_value:.3f}" if not valid_max else "")
        print_result("NDVI min valido (0.15-0.60)", valid_min,
                     f"{min_value:.3f}" if not valid_min else "")
        print_result("Tendencia valida", valid_trend, trend)

        return valid_max and valid_min and valid_trend

    except Exception as e:
        print_result("Erro", False, str(e))
        return False


def validate_milho() -> bool:
    print_header("Cenario Milho")

    try:
        from src.app.ee_auth import initialize_earth_engine
        from src.app.earth_engine import get_image_collection, calculate_ndvi, mask_clouds
        from src.app.time_series import compute_time_series
        from src.app.anomalies import compute_trend

        initialize_earth_engine()

        geometry = create_test_geometry(MILHO_CENTER, size_km=0.7)

        collection = get_image_collection(geometry, MILHO_PERIOD[0], MILHO_PERIOD[1])

        if collection.size().getInfo() == 0:
            print_result("Imagens encontradas", False, "Nenhuma imagem")
            return False

        collection = collection.map(mask_clouds)
        index_collection = collection.map(calculate_ndvi)

        time_series = compute_time_series(
            index_collection, geometry, "NDVI", scale=100
        )

        if len(time_series) < 5:
            print_result("Dados suficientes", False, f"Só {len(time_series)} pontos")
            return False

        values = [p["value"] for p in time_series]
        mean_value = sum(values) / len(values)
        min_value = min(values)
        max_value = max(values)
        trend = compute_trend(time_series)

        print_result("Imagens encontradas", True, f"{len(time_series)} pontos")
        print_result("NDVI medio", True, f"{mean_value:.3f}")
        print_result("NDVI min", True, f"{min_value:.3f}")
        print_result("NDVI max", True, f"{max_value:.3f}")
        print_result("Tendencia", True, trend)

        valid_max = 0.45 <= max_value <= 0.95
        valid_min = 0.15 <= min_value <= 0.65
        valid_trend = trend in ["crescente", "estável", "decrescente"]

        print_result("NDVI max valido (0.45-0.95)", valid_max,
                     f"{max_value:.3f}" if not valid_max else "")
        print_result("NDVI min valido (0.15-0.65)", valid_min,
                     f"{min_value:.3f}" if not valid_min else "")
        print_result("Tendencia valida", valid_trend, trend)

        return valid_max and valid_min and valid_trend

    except Exception as e:
        print_result("Erro", False, str(e))
        return False


def validate_pastagem() -> bool:
    print_header("Cenario Pastagem")

    try:
        from src.app.ee_auth import initialize_earth_engine
        from src.app.earth_engine import get_image_collection, calculate_ndvi, mask_clouds
        from src.app.time_series import compute_time_series
        from src.app.anomalies import compute_trend
        import numpy as np

        initialize_earth_engine()

        geometry = create_test_geometry(PASTAGEM_CENTER, size_km=0.5)

        collection = get_image_collection(geometry, PASTAGEM_PERIOD[0], PASTAGEM_PERIOD[1])

        if collection.size().getInfo() == 0:
            print_result("Imagens encontradas", False, "Nenhuma imagem")
            return False

        collection = collection.map(mask_clouds)
        index_collection = collection.map(calculate_ndvi)

        time_series = compute_time_series(
            index_collection, geometry, "NDVI", scale=100
        )

        if len(time_series) < 10:
            print_result("Dados suficientes", False, f"Só {len(time_series)} pontos")
            return False

        values = [p["value"] for p in time_series]
        mean_value = sum(values) / len(values)
        min_value = min(values)
        max_value = max(values)
        std_value = np.std(values)
        trend = compute_trend(time_series)
        amplitude = max_value - min_value

        print_result("Imagens encontradas", True, f"{len(time_series)} pontos")
        print_result("NDVI medio", True, f"{mean_value:.3f}")
        print_result("NDVI min", True, f"{min_value:.3f}")
        print_result("NDVI max", True, f"{max_value:.3f}")
        print_result("Desvio padrao", True, f"{std_value:.3f}")
        print_result("Amplitude", True, f"{amplitude:.3f}")
        print_result("Tendencia", True, trend)

        valid_mean = 0.40 <= mean_value <= 0.75
        valid_max = 0.55 <= max_value <= 0.85
        valid_min = 0.30 <= min_value <= 0.60
        valid_std = std_value < 0.20
        valid_amplitude = amplitude < 0.50
        valid_trend = trend in ["crescente", "estável", "decrescente"]

        print_result("NDVI medio valido (0.40-0.75)", valid_mean,
                     f"{mean_value:.3f}" if not valid_mean else "")
        print_result("NDVI max valido (0.55-0.85)", valid_max,
                     f"{max_value:.3f}" if not valid_max else "")
        print_result("NDVI min valido (0.30-0.60)", valid_min,
                     f"{min_value:.3f}" if not valid_min else "")
        print_result("Desvio padrao < 0.20", valid_std,
                     f"{std_value:.3f}" if not valid_std else "")
        print_result("Amplitude < 0.50", valid_amplitude,
                     f"{amplitude:.3f}" if not valid_amplitude else "")

        return valid_mean and valid_max and valid_min and valid_std and valid_amplitude

    except Exception as e:
        print_result("Erro", False, str(e))
        return False


def main():
    print("\n" + "=" * 50)
    print(" VALIDACAO DE CENARIOS DE CULTURA")
    print(" MVP - Monitoramento Agricola")
    print("=" * 50)

    results = {
        "Soja": validate_soja(),
        "Milho": validate_milho(),
        "Pastagem": validate_pastagem(),
    }

    print_header("RESUMO")

    all_ok = True
    for name, ok in results.items():
        status = "[OK]" if ok else "[FAIL]"
        print(f"  {status} {name}")
        if not ok:
            all_ok = False

    print("\n" + "=" * 50)
    if all_ok:
        print(" TODOS OS CENARIOS VALIDARAM COM SUCESSO")
        print(" O MVP esta pronto para uso!")
    else:
        print(" ALGUNS CENARIOS NAO VALIDARAM")
        print(" Revise os resultados acima.")
    print("=" * 50 + "\n")

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
