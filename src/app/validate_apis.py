#!/usr/bin/env python
"""Script de validacao das APIs do Sistema de Monitoramento Agricola."""

import sys
import os
import time
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

import requests

try:
    import ee
    EE_AVAILABLE = True
except ImportError:
    EE_AVAILABLE = False


def print_header(text: str) -> None:
    print(f"\n{'=' * 50}")
    print(f" {text}")
    print(f"{'=' * 50}")


def print_result(name: str, success: bool, details: str = "") -> None:
    status = "[OK]" if success else "[FAIL]"
    print(f"  {name}: {status}")
    if details:
        print(f"         {details}")


def validate_nasa_power_api() -> bool:
    print_header("NASA POWER API")

    url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    params = {
        "community": "ag",
        "parameters": "PRECTOTCORR,T2M",
        "start": "20240101",
        "end": "20240131",
        "latitude": -20.0,
        "longitude": -45.0,
        "format": "JSON",
    }

    try:
        start_time = time.time()
        response = requests.get(url, params=params, timeout=30)
        elapsed_ms = int((time.time() - start_time) * 1000)

        if response.status_code == 200:
            data = response.json()
            properties = data.get("properties", {})
            parameter_data = properties.get("parameter", {})

            has_precip = "PRECTOTCORR" in parameter_data
            has_temp = "T2M" in parameter_data

            print_result(
                "Status HTTP",
                True,
                f"{response.status_code} ({elapsed_ms}ms)"
            )
            print_result("Estrutura JSON", True)
            print_result("Dados PRECTOTCORR", has_precip)
            print_result("Dados T2M", has_temp)

            return has_precip and has_temp
        else:
            print_result("Status HTTP", False, str(response.status_code))
            return False

    except requests.exceptions.ConnectionError:
        print_result("Conexão", False, "Erro de rede - verifique sua conexão")
        return False
    except requests.exceptions.Timeout:
        print_result("Timeout", False, "API não respondeu em 30s")
        return False
    except Exception as e:
        print_result("Erro", False, str(e))
        return False


def validate_earth_engine() -> bool:
    print_header("Google Earth Engine")

    if not EE_AVAILABLE:
        print_result("Módulo ee", False, "earthengine-api não está instalada")
        return False

    try:
        from src.app.config import EE_PROJECT_ID
        from src.app.ee_auth import initialize_earth_engine

        print_result("Módulo Earth Engine", True)
        print_result("EE_PROJECT_ID configurado", EE_PROJECT_ID is not None,
                     EE_PROJECT_ID if EE_PROJECT_ID else "NÃO DEFINIDO")

        if not EE_PROJECT_ID:
            print_result("Autenticação", False, "EE_PROJECT_ID não definido no .env")
            return False

        print("\n  Tentando inicializar Earth Engine...")
        initialize_earth_engine()
        print_result("Autenticação EE", True, "ee.Initialize() bem-sucedido")

        point = ee.Geometry.Point([-45.0, -20.0])
        elevation = ee.Image("USGS/SRTMGL1_003").select("elevation")
        result = elevation.sample(point, 1).first().get("elevation").getInfo()

        print_result("Query de elevação", True, f"{result}m")

        return True

    except ValueError as e:
        if "EE_PROJECT_ID" in str(e):
            print_result("EE_PROJECT_ID", False, "Não encontrado no .env")
        else:
            print_result("Erro de configuração", False, str(e))
            print("\n  -> Execute: earthengine authenticate")
            print("     Apos autenticar, o projeto estarah pronto.")
        return False

    except Exception as e:
        error_msg = str(e)
        if "Authentication" in error_msg or "credential" in error_msg.lower():
            print_result("Autenticação", False, "Não autenticado")
            print("\n  -> Execute: earthengine authenticate")
            print("     E siga as instrucoes para autorizar.")
            return False
        else:
            print_result("Erro", False, error_msg)
            return False


def validate_python_modules() -> bool:
    print_header("Módulos Python")

    modules = [
        ("pandas", "pandas"),
        ("plotly", "plotly"),
        ("streamlit", "streamlit"),
        ("geemap", "geemap"),
    ]

    all_ok = True
    for name, import_name in modules:
        try:
            __import__(import_name)
            print_result(name, True)
        except ImportError:
            print_result(name, False, "não instalado")
            all_ok = False

    return all_ok


def validate_src_modules() -> bool:
    print_header("Módulos src.app")

    if not EE_AVAILABLE:
        print_result("Earth Engine (ee)", False, "não instalado")
        return False

    try:
        import importlib.util
        import sys

        spec = importlib.util.spec_from_file_location("config", str(project_root / "src" / "app" / "config.py"))
        config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config_module)

        EE_PROJECT_ID = config_module.EE_PROJECT_ID
        print_result("config", True)
        print_result("EE_PROJECT_ID", EE_PROJECT_ID is not None,
                     EE_PROJECT_ID if EE_PROJECT_ID else "NÃO DEFINIDO")

        if not EE_PROJECT_ID:
            print_result("Autenticação EE", False, "EE_PROJECT_ID não definido")
            return False

        print_result("ee.Initialize()", False, "Requer autenticação")
        print("  Para autenticar, execute: earthengine authenticate")

        return False

    except Exception as e:
        print_result("Erro", False, str(e)[:50])
        return False


def main():
    print("\n" + "=" * 50)
    print(" SISTEMA DE MONITORAMENTO AGRÍCOLA")
    print(" Validação de APIs e Módulos")
    print("=" * 50)

    results = {
        "NASA POWER API": validate_nasa_power_api(),
        "Python Modules": validate_python_modules(),
        "src.app Modules": validate_src_modules(),
        "Earth Engine": validate_earth_engine(),
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
        print(" TODAS AS VALIDACOES PASSARAM")
        print("   O sistema esta pronto para uso!")
    else:
        print(" ALGUMAS VALIDACOES FALHARAM")
        print("   Corrija os itens acima antes de usar o sistema.")
    print("=" * 50 + "\n")

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
