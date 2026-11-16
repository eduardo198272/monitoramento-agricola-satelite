"""Casos exclusivamente sintéticos; nunca usados como respostas oficiais."""

import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest


BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("avaliacao_local", BASE/"analisar_respostas.py")
analysis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(analysis)


def frame(n=1):
    columns = [q["pergunta"] for q in json.loads((BASE.parent/"instrumento.json").read_text())]
    row = [""]*50
    row[0] = pd.Timestamp("2026-11-01 10:00")
    row[1] = row[14] = "Sim"
    row[2:5] = ["Outra", "Básico", "Nunca"]
    row[5:14] = ["Consegui sem ajuda"]*9
    row[15:24] = ["4 – Concordo parcialmente"]*9
    row[24:35] = ["4 – Útil"]*11
    row[35:43] = ["4 – Concordo parcialmente"]*8
    row[43:48] = ["Texto sintético apenas para teste"]*5
    row[48] = 7
    return pd.DataFrame([row.copy() for _ in range(n)], columns=columns)


def test_missing_and_unable_are_not_neutral():
    s = pd.Series(["1 – Discordo totalmente", "3 – Neutro",
                   "5 – Concordo totalmente", "", None, "Não consegui avaliar",
                   "Não se aplica", "valor inválido"])
    result, counts = analysis.analyze_item(s, analysis.AGREEMENT, analysis.AGREEMENT)
    assert result["n_valido"] == 3
    assert result["ausentes"] == 2
    assert result["nao_avaliou"] == result["nao_aplicavel"] == result["invalidas"] == 1
    assert result["mediana"] == 3
    assert result["q1"] == 2 and result["q3"] == 4 and result["iiq"] == 2
    assert counts["3 – Neutro"] == 1


def test_sample_sd_and_ties_in_modes():
    r = analysis.numbers_stats([1, 1, 3, 3])
    assert r["modas"] == "1;3"
    assert r["dp_amostral"] == pytest.approx(np.sqrt(4/3))
    assert analysis.numbers_stats([2])["dp_amostral"] is None
    assert analysis.numbers_stats([])["mediana"] is None


def test_tasks_attempt_denominator_excludes_not_tried():
    f = frame(4)
    for i, value in enumerate(analysis.TASKS):
        f.iloc[i,5] = value
    _, items, _, _, _, _ = analysis.analyze_frame(f)
    r = items[items.coluna==6].iloc[0]
    assert r.tentaram == 3 and r.concluiram == 2
    assert r.conclusao_pct_tentativas == pytest.approx(200/3)
    assert r.nao_tentou_pct_validas == 25


def test_consent_exploration_and_exact_duplicate():
    f = frame(4)
    f.iloc[1,1] = "Não"
    f.iloc[2,14] = "Não"
    _, _, _, _, _, q = analysis.analyze_frame(f)
    assert q["elegiveis"] == 1
    assert q["duplicatas_exatas_excluidas"] == 1
    assert q["sem_consentimento"] == 1
    assert q["sem_exploracao_declarada"] == 1


def test_out_of_range_general_note():
    f = frame()
    f.iloc[0,48] = 11
    _, _, _, note, _, _ = analysis.analyze_frame(f)
    assert note["n_valido"] == 0
    assert note["invalidas"] == 1
    assert note["media"] is None


def test_new_open_text_requires_manual_coding():
    themes, quality = analysis.qualitative(frame())
    assert quality["registros_pendentes_codificacao"] == 1
    assert quality["celulas_discursivas_codificadas"] == 0
    assert themes.registros_com_tema.sum() == 0


def test_empty_open_fields_receive_no_theme():
    f = frame()
    f.iloc[0,43:48] = ""
    themes, quality = analysis.qualitative(f)
    assert quality["registros_pendentes_codificacao"] == 0
    assert quality["celulas_discursivas_codificadas"] == 0
    assert themes.registros_com_tema.sum() == 0
    assert all(themes.n_codificado == 1)


def test_small_crossed_groups_are_suppressed():
    result = analysis.crossed(frame())
    assert all(result.estado.str.startswith("Suprimido"))
    assert "media" not in result.columns


def test_changed_headers_fail_before_analysis():
    f = frame().rename(columns={"Carimbo de data/hora":"Outra data"})
    with pytest.raises(ValueError):
        analysis.analyze_frame(f)
