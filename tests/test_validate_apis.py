import builtins
import importlib.util
import runpy
import sys
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest
import requests

import src.app.validate_apis as validate_apis


def test_print_header_and_result(capsys):
    validate_apis.print_header("Teste")
    validate_apis.print_result("API", True)
    validate_apis.print_result("Falha", False, "detalhes")

    output = capsys.readouterr().out
    assert "Teste" in output
    assert "API: [OK]" in output
    assert "Falha: [FAIL]" in output
    assert "detalhes" in output


def nasa_response(payload, status_code=200):
    response = MagicMock()
    response.status_code = status_code
    response.json.return_value = payload
    return response


def test_validate_nasa_power_api_success():
    payload = {
        "properties": {
            "parameter": {
                "PRECTOTCORR": {"20240101": 1.0},
                "T2M": {"20240101": 25.0},
            }
        }
    }

    with patch("src.app.validate_apis.requests.get", return_value=nasa_response(payload)) as get:
        with patch("src.app.validate_apis.time.time", side_effect=[10.0, 10.123]):
            assert validate_apis.validate_nasa_power_api() is True

    get.assert_called_once_with(
        "https://power.larc.nasa.gov/api/temporal/daily/point",
        params={
            "community": "ag",
            "parameters": "PRECTOTCORR,T2M",
            "start": "20240101",
            "end": "20240131",
            "latitude": -20.0,
            "longitude": -45.0,
            "format": "JSON",
        },
        timeout=30,
    )


@pytest.mark.parametrize(
    "payload",
    [
        {"properties": {"parameter": {"T2M": {}}}},
        {"properties": {"parameter": {"PRECTOTCORR": {}}}},
    ],
)
def test_validate_nasa_power_api_rejects_incomplete_data(payload):
    with patch("src.app.validate_apis.requests.get", return_value=nasa_response(payload)):
        assert validate_apis.validate_nasa_power_api() is False


def test_validate_nasa_power_api_rejects_http_error(mock_http_response):
    with patch(
        "src.app.validate_apis.requests.get",
        return_value=mock_http_response(status_code=503),
    ):
        assert validate_apis.validate_nasa_power_api() is False


@pytest.mark.parametrize(
    "error",
    [requests.exceptions.ConnectionError(), requests.exceptions.Timeout(), RuntimeError("boom")],
)
def test_validate_nasa_power_api_handles_request_errors(error):
    with patch("src.app.validate_apis.requests.get", side_effect=error):
        assert validate_apis.validate_nasa_power_api() is False


def ee_module():
    ee = MagicMock()
    ee.Geometry.Point.return_value = MagicMock(name="point")
    ee.Image.return_value.select.return_value.sample.return_value.first.return_value.get.return_value.getInfo.return_value = 123
    return ee


def test_validate_earth_engine_when_unavailable():
    with patch.object(validate_apis, "EE_AVAILABLE", False):
        assert validate_apis.validate_earth_engine() is False


def test_validate_earth_engine_requires_project_id():
    with patch.object(validate_apis, "EE_AVAILABLE", True):
        with patch("src.app.config.EE_PROJECT_ID", None):
            assert validate_apis.validate_earth_engine() is False


def test_validate_earth_engine_success():
    ee = ee_module()
    with patch.object(validate_apis, "EE_AVAILABLE", True), patch.object(validate_apis, "ee", ee):
        with patch("src.app.config.EE_PROJECT_ID", "test-project"):
            with patch("src.app.ee_auth.initialize_earth_engine") as initialize:
                assert validate_apis.validate_earth_engine() is True

    initialize.assert_called_once_with()
    ee.Geometry.Point.assert_called_once_with([-45.0, -20.0])
    ee.Image.assert_called_once_with("USGS/SRTMGL1_003")


def test_validate_earth_engine_handles_project_id_value_error():
    with patch.object(validate_apis, "EE_AVAILABLE", True):
        with patch("src.app.config.EE_PROJECT_ID", "test-project"):
            with patch(
                "src.app.ee_auth.initialize_earth_engine",
                side_effect=ValueError("EE_PROJECT_ID not configured"),
            ):
                assert validate_apis.validate_earth_engine() is False


def test_validate_earth_engine_handles_other_value_error():
    with patch.object(validate_apis, "EE_AVAILABLE", True):
        with patch("src.app.config.EE_PROJECT_ID", "test-project"):
            with patch(
                "src.app.ee_auth.initialize_earth_engine",
                side_effect=ValueError("invalid configuration"),
            ):
                assert validate_apis.validate_earth_engine() is False


@pytest.mark.parametrize("error", [RuntimeError("Authentication failed"), RuntimeError("credential missing")])
def test_validate_earth_engine_handles_authentication_errors(error):
    with patch.object(validate_apis, "EE_AVAILABLE", True):
        with patch("src.app.config.EE_PROJECT_ID", "test-project"):
            with patch("src.app.ee_auth.initialize_earth_engine", side_effect=error):
                assert validate_apis.validate_earth_engine() is False


def test_validate_earth_engine_handles_generic_error():
    with patch.object(validate_apis, "EE_AVAILABLE", True):
        with patch("src.app.config.EE_PROJECT_ID", "test-project"):
            with patch("src.app.ee_auth.initialize_earth_engine", side_effect=RuntimeError("service down")):
                assert validate_apis.validate_earth_engine() is False


def test_validate_python_modules_success():
    assert validate_apis.validate_python_modules() is True


def test_validate_python_modules_reports_missing_module():
    original_import = builtins.__import__

    def import_without_geemap(name, *args, **kwargs):
        if name == "geemap":
            raise ImportError("missing geemap")
        return original_import(name, *args, **kwargs)

    with patch("builtins.__import__", side_effect=import_without_geemap):
        assert validate_apis.validate_python_modules() is False


def test_validate_src_modules_when_ee_unavailable():
    with patch.object(validate_apis, "EE_AVAILABLE", False):
        assert validate_apis.validate_src_modules() is False


def test_validate_src_modules_without_project_id():
    config = SimpleNamespace(EE_PROJECT_ID=None)
    spec = MagicMock()
    with patch.object(validate_apis, "EE_AVAILABLE", True):
        with patch.object(importlib.util, "module_from_spec", return_value=config):
            with patch.object(importlib.util, "spec_from_file_location", return_value=spec):
                assert validate_apis.validate_src_modules() is False
    spec.loader.exec_module.assert_called_once_with(config)


def test_validate_src_modules_with_project_id():
    config = SimpleNamespace(EE_PROJECT_ID="test-project")
    spec = MagicMock()
    with patch.object(validate_apis, "EE_AVAILABLE", True):
        with patch.object(importlib.util, "module_from_spec", return_value=config):
            with patch.object(importlib.util, "spec_from_file_location", return_value=spec):
                assert validate_apis.validate_src_modules() is False


def test_validate_src_modules_handles_load_error():
    spec = MagicMock()
    spec.loader.exec_module.side_effect = RuntimeError("load failed")
    with patch.object(validate_apis, "EE_AVAILABLE", True):
        with patch.object(importlib.util, "module_from_spec", return_value=MagicMock()):
            with patch.object(importlib.util, "spec_from_file_location", return_value=spec):
                assert validate_apis.validate_src_modules() is False


def test_script_imports_without_earth_engine():
    with patch.dict(sys.modules, {"ee": None}):
        namespace = runpy.run_path(validate_apis.__file__, run_name="validate_apis_without_ee")

    assert namespace["EE_AVAILABLE"] is False


def test_script_main_block_runs_without_external_services():
    payload = {
        "properties": {
            "parameter": {
                "PRECTOTCORR": {"20240101": 1.0},
                "T2M": {"20240101": 25.0},
            }
        }
    }
    with patch.dict(sys.modules, {"ee": None}):
        with patch("requests.get", return_value=nasa_response(payload)):
            with patch("time.time", side_effect=[10.0, 10.123]):
                with patch("sys.exit") as exit_mock:
                    runpy.run_path(validate_apis.__file__, run_name="__main__")

    exit_mock.assert_called_once_with(1)


def test_main_returns_zero_when_everything_passes():
    with patch.multiple(
        validate_apis,
        validate_nasa_power_api=MagicMock(return_value=True),
        validate_python_modules=MagicMock(return_value=True),
        validate_src_modules=MagicMock(return_value=True),
        validate_earth_engine=MagicMock(return_value=True),
    ):
        assert validate_apis.main() == 0


def test_main_returns_one_when_any_validation_fails():
    with patch.multiple(
        validate_apis,
        validate_nasa_power_api=MagicMock(return_value=True),
        validate_python_modules=MagicMock(return_value=False),
        validate_src_modules=MagicMock(return_value=True),
        validate_earth_engine=MagicMock(return_value=True),
    ):
        assert validate_apis.main() == 1
