"""Synthetic cases only, isolated from academic participant evidence."""
import importlib.util
from pathlib import Path
import pytest

spec = importlib.util.spec_from_file_location(
    "survey_analysis", Path("docs/artigo_final/experimentos/analisar_pesquisa.py")
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_denominators_and_ordinal_distribution():
    rows = [
        {"consent": "Sim", "score": "5"},
        {"consent": "Sim", "score": "3"},
        {"consent": "Sim", "score": "Não se aplica"},
        {"consent": "Sim", "score": "Não consegui avaliar"},
        {"consent": "Sim", "score": ""},
        {"consent": "Não", "score": "1"},
    ]
    config = {"consent_column": "consent", "consent_value": "Sim",
              "questions": {"score": {"type": "ordinal", "values": {"3": 3, "5": 5}}}}
    result, quotes = module.analyze(rows, config)
    assert result["eligible"] == 5
    question = result["questions"]["score"]
    assert question["valid"] == 2
    assert question["not_applicable"] == question["unable"] == question["missing"] == 1
    assert question["median"] == 4
    assert question["iqr"] == 1
    assert question["frequencies"]["5"] == {"absolute": 1, "relative_valid": 0.5}
    assert quotes == []


def test_multiple_open_invalid_and_zero_answers():
    config = {"consent_column": "ok", "consent_value": "Sim", "questions": {
        "tools": {"type": "multiple", "separator": ";", "values": ["mapa", "CSV"]},
        "comment": {"type": "open"},
        "profile": {"type": "categorical", "values": ["estudante"]},
    }}
    result, quotes = module.analyze([
        {"ok": "Sim", "tools": "mapa;CSV;mapa", "comment": "Comentário sintético",
         "profile": "não mapeado"},
    ], config)
    assert result["questions"]["tools"]["frequencies"]["mapa"]["absolute"] == 1
    assert result["questions"]["profile"]["invalid"] == 1
    assert quotes[0]["participant"] == "P001"
    empty, _ = module.analyze([], config)
    assert empty["questions"]["profile"]["valid"] == 0
    with pytest.raises(ValueError):
        module.analyze([], {"consent_column": "ok", "consent_value": "Sim",
                           "questions": {"x": {"type": "unrecognized"}}})
