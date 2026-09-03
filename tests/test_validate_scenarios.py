import runpy
import json
from unittest.mock import MagicMock, patch

import pytest

import src.app.validate_scenarios as validate_scenarios


def configured_collection(size=5):
    collection = MagicMock(name="collection")
    collection.size.return_value.getInfo.return_value = size
    collection.map.return_value = collection
    return collection


def patch_scenario(collection, points, trend="estável"):
    return (
        patch(
            "src.app.validate_scenarios.ee.Geometry.Polygon",
            return_value=MagicMock(name="geometry"),
        ),
        patch("src.app.ee_auth.initialize_earth_engine"),
        patch("src.app.earth_engine.get_image_collection", return_value=collection),
        patch("src.app.earth_engine.mask_clouds", side_effect=lambda image: image),
        patch("src.app.earth_engine.calculate_ndvi", side_effect=lambda image: image),
        patch("src.app.time_series.compute_time_series", return_value=points),
        patch("src.app.anomalies.compute_trend", return_value=trend),
    )


def enter_patches(patches):
    for mocked in patches:
        mocked.start()


def stop_patches(patches):
    for mocked in reversed(patches):
        mocked.stop()


def run_scenario(function, collection, points, trend="estável"):
    patches = patch_scenario(collection, points, trend)
    enter_patches(patches)
    try:
        return function()
    finally:
        stop_patches(patches)


def points_with_values(values):
    return [
        {"date": f"2026-01-{index:02d}", "value": value}
        for index, value in enumerate(values, start=1)
    ]


def test_print_helpers(capsys):
    validate_scenarios.print_header("Cenario")
    validate_scenarios.print_result("Sucesso", True)
    validate_scenarios.print_result("Falha", False, "detalhes")

    output = capsys.readouterr().out
    assert "Cenario" in output
    assert "Sucesso: [OK]" in output
    assert "Falha: [FAIL]" in output
    assert "detalhes" in output


def test_create_test_geometry_uses_center_and_size():
    with patch.object(validate_scenarios.ee.Geometry, "Polygon") as polygon:
        geometry = validate_scenarios.create_test_geometry([-50.0, -15.0], 2.0)

    assert geometry is polygon.return_value
    coordinates = polygon.call_args.args[0][0]
    assert coordinates[0] == pytest.approx([-50.0 - 2 / 111, -15.0 - 2 / 111])
    assert coordinates[-1] == coordinates[0]


def test_result_helpers_and_json_output(tmp_path):
    result = validate_scenarios._scenario_result(
        "Soja", validate_scenarios.SOJA_CENTER, 1.0, validate_scenarios.SOJA_PERIOD
    )
    validate_scenarios._finish_result(
        result, True, {"mean": 0.7}, {"mean": True}, error="ignored"
    )
    assert result["success"] is True
    assert result["metrics"] == {"mean": 0.7}
    assert result["checks"] == {"mean": True}
    assert result["error"] == "ignored"

    validate_scenarios._finish_result(None, False)
    empty_result = validate_scenarios._scenario_result(
        "Milho", validate_scenarios.MILHO_CENTER, 0.7, validate_scenarios.MILHO_PERIOD
    )
    validate_scenarios._finish_result(empty_result, False, {}, {}, error="")
    output = tmp_path / "nested" / "results.json"
    validate_scenarios.write_results(output, {"Soja": result})
    assert json.loads(output.read_text(encoding="utf-8"))["Soja"]["success"] is True


def test_validate_soja_success():
    result = run_scenario(
        validate_scenarios.validate_soja,
        configured_collection(),
        points_with_values([0.2, 0.4, 0.7, 0.8, 0.6]),
        "crescente",
    )

    assert result is True


@pytest.mark.parametrize(
    "values, trend",
    [
        ([0.1, 0.2, 0.3, 0.4, 0.45], "estável"),
        ([0.1, 0.3, 0.4, 0.5, 0.7], "estável"),
        ([0.2, 0.3, 0.4, 0.5, 0.7], "desconhecida"),
    ],
)
def test_validate_soja_rejects_invalid_criteria(values, trend):
    assert run_scenario(
        validate_scenarios.validate_soja,
        configured_collection(),
        points_with_values(values),
        trend,
    ) is False


def test_validate_soja_rejects_empty_collection_and_short_series():
    assert run_scenario(
        validate_scenarios.validate_soja,
        configured_collection(size=0),
        points_with_values([]),
    ) is False
    assert run_scenario(
        validate_scenarios.validate_soja,
        configured_collection(),
        points_with_values([0.2, 0.3, 0.4, 0.5]),
    ) is False


def test_validate_soja_handles_exception():
    with patch("src.app.ee_auth.initialize_earth_engine", side_effect=RuntimeError("offline")):
        assert validate_scenarios.validate_soja() is False


def test_validate_milho_success():
    assert run_scenario(
        validate_scenarios.validate_milho,
        configured_collection(),
        points_with_values([0.2, 0.4, 0.6, 0.8, 0.7]),
        "decrescente",
    ) is True


@pytest.mark.parametrize(
    "values, trend",
    [
        ([0.1, 0.2, 0.3, 0.4, 0.44], "estável"),
        ([0.1, 0.3, 0.4, 0.5, 0.7], "estável"),
        ([0.2, 0.3, 0.4, 0.5, 0.7], "desconhecida"),
    ],
)
def test_validate_milho_rejects_invalid_criteria(values, trend):
    assert run_scenario(
        validate_scenarios.validate_milho,
        configured_collection(),
        points_with_values(values),
        trend,
    ) is False


def test_validate_milho_rejects_empty_collection_and_short_series():
    assert run_scenario(
        validate_scenarios.validate_milho,
        configured_collection(size=0),
        points_with_values([]),
    ) is False
    assert run_scenario(
        validate_scenarios.validate_milho,
        configured_collection(),
        points_with_values([0.2, 0.3, 0.4, 0.5]),
    ) is False


def test_validate_milho_handles_exception():
    with patch("src.app.ee_auth.initialize_earth_engine", side_effect=RuntimeError("offline")):
        assert validate_scenarios.validate_milho() is False


def test_validate_pastagem_success():
    assert run_scenario(
        validate_scenarios.validate_pastagem,
        configured_collection(),
        points_with_values([0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.6, 0.55, 0.5, 0.45]),
    ) is True


@pytest.mark.parametrize(
    "values",
    [
        [0.2] * 10,
        [0.3] * 9 + [0.9],
        [0.3] * 9 + [0.7],
        [0.3] * 9 + [0.2],
        [0.3] * 9 + [0.8],
    ],
)
def test_validate_pastagem_rejects_invalid_criteria(values):
    assert run_scenario(
        validate_scenarios.validate_pastagem,
        configured_collection(),
        points_with_values(values),
    ) is False


def test_validate_pastagem_rejects_empty_collection_and_short_series():
    assert run_scenario(
        validate_scenarios.validate_pastagem,
        configured_collection(size=0),
        points_with_values([]),
    ) is False
    assert run_scenario(
        validate_scenarios.validate_pastagem,
        configured_collection(),
        points_with_values([0.4] * 9),
    ) is False


def test_validate_pastagem_handles_exception():
    with patch("src.app.ee_auth.initialize_earth_engine", side_effect=RuntimeError("offline")):
        assert validate_scenarios.validate_pastagem() is False


def test_main_returns_zero_when_all_scenarios_pass(capsys):
    with patch.multiple(
        validate_scenarios,
        validate_soja=MagicMock(return_value=True),
        validate_milho=MagicMock(return_value=True),
        validate_pastagem=MagicMock(return_value=True),
    ):
        assert validate_scenarios.main() == 0

    output = capsys.readouterr().out
    assert "TODOS OS CENARIOS VALIDARAM COM SUCESSO" in output


def test_main_returns_one_when_a_scenario_fails(capsys):
    with patch.multiple(
        validate_scenarios,
        validate_soja=MagicMock(return_value=True),
        validate_milho=MagicMock(return_value=False),
        validate_pastagem=MagicMock(return_value=True),
    ):
        assert validate_scenarios.main() == 1

    output = capsys.readouterr().out
    assert "ALGUNS CENARIOS NAO VALIDARAM" in output


def test_main_writes_structured_results(tmp_path, monkeypatch):
    output = tmp_path / "results.json"
    monkeypatch.setenv("VALIDATION_OUTPUT", str(output))
    with patch.multiple(
        validate_scenarios,
        validate_soja=MagicMock(return_value=True),
        validate_milho=MagicMock(return_value=True),
        validate_pastagem=MagicMock(return_value=True),
    ):
        assert validate_scenarios.main() == 0

    saved = json.loads(output.read_text(encoding="utf-8"))
    assert saved["Soja"]["period"] == {
        "start": validate_scenarios.SOJA_PERIOD[0],
        "end": validate_scenarios.SOJA_PERIOD[1],
    }


def test_script_main_block_exits_without_external_services():
    collection = configured_collection()
    points = points_with_values([0.6] * 10)
    with patch("src.app.ee_auth.initialize_earth_engine"), patch(
        "src.app.earth_engine.get_image_collection", return_value=collection
    ), patch("src.app.earth_engine.mask_clouds", side_effect=lambda image: image), patch(
        "src.app.earth_engine.calculate_ndvi", side_effect=lambda image: image
    ), patch("src.app.time_series.compute_time_series", return_value=points), patch(
        "src.app.anomalies.compute_trend", return_value="estável"
    ), patch("sys.exit") as exit_mock:
        runpy.run_path(validate_scenarios.__file__, run_name="__main__")

        exit_mock.assert_called_once_with(1)
