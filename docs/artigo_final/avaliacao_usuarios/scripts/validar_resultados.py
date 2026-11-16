"""Conferência independente dos CSV contra a planilha; não altera entradas."""

from collections import Counter
import argparse
import hashlib
import json
from pathlib import Path
import statistics

import pandas as pd


BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[2]


def validate(source, output=None):
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
    # A fonte definitiva acrescenta um registro e tem outra ordem.
    # Comparar multiconjuntos, sem remover as diferenças históricas dos carimbos.
    def answer_key(row):
        return tuple(None if pd.isna(v) else str(v) for v in row.iloc[1:])
    originals = Counter(answer_key(row) for _, row in before.iterrows())
    current = Counter(answer_key(row) for _, row in data.iterrows())
    assert not originals-current
    assert len(data) == 32 and len(before) == 31
    matched = {answer_key(row): row.iloc[0] for _, row in data.iterrows()}
    changed_dates = 0
    for _, row in before.iterrows():
        old, new = row.iloc[0], matched[answer_key(row)]
        changed_dates += old != new
        assert new == (old.replace(day=15) if old.day in {16,17} else old)
    assert changed_dates == 7
    quartiles = statistics.quantiles(numeric, n=4, method="inclusive")
    assert score.q1 == quartiles[0] and score.q3 == quartiles[2]
    for item in items[items.grupo == "tarefas"].itertuples():
        counts = Counter(f.iloc[:, item.coluna-1])
        attempted = len(f)-counts["Não tentei"]
        completed = counts["Consegui sem ajuda"]+counts["Consegui com ajuda"]
        assert item.tentaram == attempted and item.concluiram == completed
        assert abs(item.conclusao_pct_tentativas-100*completed/attempted) < 1e-9
    config = json.loads((BASE/"codificacao.json").read_text())
    codes = {r["text_sha256"]: r["codigos"] for r in config["registros"]}
    thematic_counts, filled = Counter(), 0
    for _, row in f.iterrows():
        texts = ["" if pd.isna(v) else " ".join(str(v).split()) for v in row.iloc[43:48]]
        digest = hashlib.sha256("\n".join(texts).encode()).hexdigest()
        mapping = codes[digest]
        filled += sum(bool(t) for t in texts)
        thematic_counts.update(set(c for values in mapping.values() for c in values))
    themes = pd.read_csv(BASE/"resultados/categorias_qualitativas.csv")
    assert filled == 142
    assert all(r.registros_com_tema == thematic_counts[r.codigo] and r.n_codificado == 32
               for r in themes.itertuples())
    crossings = pd.read_csv(BASE/"resultados/cruzamentos.csv")
    targets = {
        "experiencia_vs_compreensao": (4, 15, {"Frequentemente", "Ocasionalmente"}),
        "area_vs_utilidade_indices": (2, 27, {"Engenheiro agrônomo"}),
        "conhecimento_vs_autonomia": (3, 18, {"Avançado", "Especialista"}),
        "experiencia_vs_nota": (4, 48, {"Frequentemente", "Ocasionalmente"}),
        "compreensao_vs_intencao": (15, 41, {"4 – Concordo parcialmente", "5 – Concordo totalmente"}),
        "utilidade_mapas_vs_nota": (28, 48, {"4 – Útil", "5 – Muito útil"}),
    }
    positive_groups = {
        "Frequente/ocasional", "Agrônomo", "Avançado/especialista",
        "Concorda (4–5)", "Útil/muito útil (4–5)",
    }
    for row in crossings.itertuples():
        source_col, target_col, high = targets[row.cruzamento]
        selected = []
        for _, response in f.iterrows():
            source_value = response.iloc[source_col]
            if row.cruzamento in {"compreensao_vs_intencao", "utilidade_mapas_vs_nota"}:
                if not str(source_value).startswith(("1", "2", "3", "4", "5")):
                    continue
            if (source_value in high) != (row.grupo in positive_groups):
                continue
            value = response.iloc[target_col]
            if target_col == 48:
                selected.append(float(value))
            elif str(value).startswith(("1", "2", "3", "4", "5")):
                selected.append(int(str(value)[0]))
        assert row.n_valido == len(selected)
        assert row.mediana == statistics.median(selected)
        assert abs(row.media-statistics.mean(selected)) < 1e-9
        assert abs(row.dp_amostral-statistics.stdev(selected)) < 1e-9
        q1, _, q3 = statistics.quantiles(selected, n=4, method="inclusive")
        assert row.q1 == q1 and row.q3 == q3
    manifest = json.loads((ROOT/"docs/artigo_final/evidencias/demonstracao_real/manifesto.json").read_text())
    assert all(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
               for name,digest in manifest["code_sha256"].items())
    figures = sorted(p.name for p in (BASE/"figuras").iterdir() if p.suffix in {".pdf",".png",".svg"})
    assert len(figures) == 27
    result = {"passed": True, "registros_conferidos": len(f),
              "itens_conferidos": len(items), "distribuicoes": len(frequencies),
              "comparacao_calculos": "Counter/statistics contra pandas/NumPy",
              "respostas_originais_correspondentes": sum(originals.values()),
              "registro_adicional": 1, "celulas_discursivas": filled,
              "temas_conferidos": len(themes),
              "cruzamentos_conferidos": len(targets),
              "grupos_cruzados_conferidos": len(crossings),
              "respostas_preservadas": True, "carimbos_retificados_nesta_rodada": 0,
              "diferencas_historicas_carimbos": changed_dates,
              "arquivos_funcionais_inalterados": len(manifest["code_sha256"]),
              "figuras": figures,
              "fonte_sha256": hashlib.sha256(source.read_bytes()).hexdigest()}
    (output or BASE/"resultados/validacao.json").write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=BASE/"privado/snapshot_publico_32.xlsx")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    validate(args.input, args.output)
