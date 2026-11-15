"""Conferência independente dos CSV contra a planilha; não altera entradas."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import statistics

import pandas as pd


BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[2]


def validate(source):
    data = pd.read_excel(source)
    frequencies = pd.read_csv(BASE/"resultados/distribuicoes.csv")
    items = pd.read_csv(BASE/"resultados/estatisticas_descritivas.csv")
    score = pd.read_csv(BASE/"resultados/avaliacao_geral.csv").iloc[0]
    # Triagem independente da rotina de análise.
    f = data[(data.iloc[:,1].str.strip()=="Sim") & (data.iloc[:,14].str.strip()=="Sim")]
    f = f.drop_duplicates()
    for item in items.itertuples():
        raw = f.iloc[:,item.coluna-1].dropna().map(lambda v:" ".join(str(v).split()))
        valid = raw[~raw.isin(["", "Não consegui avaliar", "Não se aplica"])]
        counts = Counter(valid)
        subset = frequencies[frequencies.coluna==item.coluna]
        assert sum(subset.frequencia) == item.n_valido == len(valid)
        assert abs(subset.percentual_valido.sum()-100) < 1e-9
        for cell in subset.itertuples():
            assert cell.frequencia == counts[cell.categoria]
            assert abs(cell.percentual_valido-100*counts[cell.categoria]/len(valid))<1e-9
        if item.grupo in {"utilidade","usabilidade","aplicabilidade"}:
            numeric = [int(v[0]) for v in valid]
            quartiles = statistics.quantiles(numeric, n=4, method="inclusive")
            assert item.mediana == statistics.median(numeric)
            assert abs(item.q1-quartiles[0]) < 1e-9
            assert abs(item.q3-quartiles[2]) < 1e-9
            assert abs(item.media-statistics.mean(numeric)) < 1e-9
            assert abs(item.dp_amostral-statistics.stdev(numeric)) < 1e-9
    numeric = f.iloc[:,48].tolist()
    assert abs(score.media-statistics.mean(numeric)) < 1e-9
    assert abs(score.dp_amostral-statistics.stdev(numeric)) < 1e-9
    assert score.mediana == statistics.median(numeric)
    assert str(int(score.modas)) == str(statistics.mode(numeric))
    before = pd.read_excel(BASE/"dados_originais/respostas_recebidas.xlsx")
    assert data.iloc[:,1:].equals(before.iloc[:,1:])
    assert sum(data.iloc[:,0] != before.iloc[:,0]) == 7
    for old, new in zip(before.iloc[:,0], data.iloc[:,0]):
        assert new == (old.replace(day=15) if old.day in {16,17} else old)
    manifest = json.loads((ROOT/"docs/artigo_final/evidencias/demonstracao_real/manifesto.json").read_text())
    assert all(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
               for name,digest in manifest["code_sha256"].items())
    figures = sorted(p.name for p in (BASE/"figuras").iterdir() if p.suffix in {".pdf",".png",".svg"})
    assert len(figures) == 27
    result = {"passed": True, "registros_conferidos": len(f),
              "itens_conferidos": len(items), "distribuicoes": len(frequencies),
              "comparacao_calculos": "Counter/statistics contra pandas/NumPy",
              "respostas_preservadas": True, "carimbos_retificados": 7,
              "arquivos_funcionais_inalterados": len(manifest["code_sha256"]),
              "figuras": figures,
              "fonte_sha256": hashlib.sha256(source.read_bytes()).hexdigest()}
    (BASE/"resultados/validacao.json").write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == "__main__":
    validate(next((ROOT/"docs").glob("Respostas*.xlsx")))
