"""Análise descritiva local. Não autentica pessoas nem acessa Google Forms."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import platform
import re
import unicodedata

import numpy as np
import openpyxl
import pandas as pd


BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[2]
SHEET = "Respostas ao formulário 1"
TASKS = ["Consegui sem ajuda", "Consegui com ajuda",
         "Tentei, mas não consegui", "Não tentei"]
AGREEMENT = {f"{i} – {label}": i for i, label in enumerate([
    "Discordo totalmente", "Discordo parcialmente", "Neutro",
    "Concordo parcialmente", "Concordo totalmente"], 1)}
USEFULNESS = {f"{i} – {label}": i for i, label in enumerate([
    "Nada útil", "Pouco útil", "Moderadamente útil", "Útil", "Muito útil"], 1)}
GROUPS = {"perfil": range(2, 5), "tarefas": range(5, 14),
          "usabilidade": range(15, 24), "utilidade": range(24, 35),
          "aplicabilidade": range(35, 43), "abertas": range(43, 48)}


def normalized(value):
    if pd.isna(value):
        return ""
    return " ".join(unicodedata.normalize("NFC", str(value)).split())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_digest(row):
    return hashlib.sha256("\n".join(normalized(row.iloc[i])
                                   for i in range(43, 48)).encode()).hexdigest()


def numbers_stats(values):
    a = np.asarray(values, dtype=float)
    if not len(a):
        return {"media": None, "mediana": None, "dp_amostral": None,
                "q1": None, "q3": None, "iiq": None,
                "minimo": None, "maximo": None, "modas": ""}
    q1, q3 = np.percentile(a, [25, 75], method="linear")
    counts = Counter(a)
    maximum = max(counts.values())
    return {"media": float(a.mean()), "mediana": float(np.median(a)),
            "dp_amostral": float(a.std(ddof=1)) if len(a) > 1 else None,
            "q1": float(q1), "q3": float(q3), "iiq": float(q3-q1),
            "minimo": float(a.min()), "maximo": float(a.max()),
            "modas": ";".join(f"{v:g}" for v in sorted(counts)
                             if counts[v] == maximum)}


def analyze_item(series, allowed=None, ordinal=None):
    answers = series.map(normalized)
    missing = int((answers == "").sum())
    unable = int((answers == "Não consegui avaliar").sum())
    not_applicable = int((answers == "Não se aplica").sum())
    usable = answers[~answers.isin(["", "Não consegui avaliar", "Não se aplica"])]
    invalid_mask = ~usable.isin(allowed) if allowed is not None else pd.Series(
        False, index=usable.index)
    valid = usable[~invalid_mask]
    counts = valid.value_counts().to_dict()
    result = {"recebidas": len(series), "n_valido": len(valid),
              "ausentes": missing, "nao_avaliou": unable,
              "nao_aplicavel": not_applicable, "invalidas": int(invalid_mask.sum())}
    assert sum(result[k] for k in [
        "n_valido", "ausentes", "nao_avaliou", "nao_aplicavel", "invalidas"]) == len(series)
    if ordinal is not None:
        numeric = [ordinal[v] for v in valid]
        result.update(numbers_stats(numeric))
        for label, predicate in [
            ("negativas_1_2", lambda v: v <= 2),
            ("intermediarias_3", lambda v: v == 3),
            ("positivas_4_5", lambda v: v >= 4),
        ]:
            count = sum(predicate(v) for v in numeric)
            result[label] = count
            result[f"{label}_pct_validas"] = 100 * count / len(valid) if len(valid) else None
    return result, counts


def analyze_frame(frame):
    """A unidade é submissão elegível, não identidade individual verificada."""
    data = frame.copy()
    data.columns = [normalized(c) for c in data.columns]
    if data.shape[1] != 50:
        raise ValueError("Estrutura alterada: revisar o mapeamento das 50 colunas.")
    expected = {0: "Carimbo de data/hora", 1: "Você tem 18 anos ou mais",
                2: "Qual é sua área de atuação?", 3: "Qual é seu nível de conhecimento em agricultura de precisão?",
                4: "Você já utilizou ferramentas", 5: "Qual foi o resultado",
                14: "Você conseguiu explorar", 15: "Indique seu nível",
                24: "Como você avalia a utilidade", 35: "Indique seu nível",
                43: "Quais aspectos positivos", 48: "De 0 a 10",
                49: "Descreva o que impediu"}
    for i, prefix in expected.items():
        if not data.columns[i].startswith(prefix):
            raise ValueError(f"Cabeçalho inesperado na coluna {i+1}.")
    schema_path = BASE / "instrumento.json"
    if schema_path.exists():
        schema = json.loads(schema_path.read_text())
        if [q["pergunta"] for q in schema] != list(data.columns):
            raise ValueError("Cabeçalhos diferentes do instrumento mapeado; revisar antes de analisar.")
    exact_duplicate = data.duplicated(keep="first")
    response_duplicate = data.iloc[:, 1:].duplicated(keep=False)
    consent = data.iloc[:, 1].map(normalized).eq("Sim")
    explored = data.iloc[:, 14].map(normalized).eq("Sim")
    eligible = data[consent & explored & ~exact_duplicate]
    # Datas não são critério de exclusão automática; inconsistências são reportadas.
    result_rows, frequencies = [], []
    for group, indices in GROUPS.items():
        for index in indices:
            if group == "abertas":
                continue
            column = data.columns[index]
            ordinal = USEFULNESS if group == "utilidade" else (
                AGREEMENT if group in {"usabilidade", "aplicabilidade"} else None)
            allowed = TASKS if group == "tarefas" else ordinal
            item, counts = analyze_item(eligible[column], allowed, ordinal)
            item.update({"grupo": group, "coluna": index+1, "pergunta": column,
                         "rotulo": re.search(r"\[([^\]]+)\]", column).group(1)
                         if "[" in column else column})
            if group == "tarefas":
                attempted = sum(counts.get(k, 0) for k in TASKS[:3])
                completed = sum(counts.get(k, 0) for k in TASKS[:2])
                item.update({"tentaram": attempted, "concluiram": completed,
                             "conclusao_pct_tentativas": 100*completed/attempted
                             if attempted else None})
                for key, label in zip(["sem_ajuda", "com_ajuda", "tentativa_sem_sucesso",
                                       "nao_tentou"], TASKS):
                    item[key] = counts.get(label, 0)
                    item[f"{key}_pct_validas"] = (
                        100*counts.get(label,0)/item["n_valido"] if item["n_valido"] else None)
            result_rows.append(item)
            categories = list(allowed) if allowed is not None else sorted(counts)
            for category in categories:
                count = int(counts.get(category, 0))
                frequencies.append({"grupo": group, "coluna": index+1, "rotulo": item["rotulo"],
                                    "categoria": category,
                                    "valor": ordinal.get(category) if ordinal else None,
                                    "frequencia": count, "n_valido": item["n_valido"],
                                    "percentual_valido": 100*count/item["n_valido"]
                                    if item["n_valido"] else None})
    score = pd.to_numeric(eligible.iloc[:, 48], errors="coerce")
    valid_score = score[score.notna() & score.between(0, 10) & (score % 1 == 0)]
    note = {"n_valido": len(valid_score), "ausentes": int(eligible.iloc[:,48].isna().sum()),
            "invalidas": int(len(score)-len(valid_score)-eligible.iloc[:,48].isna().sum()),
            **numbers_stats(valid_score)}
    note_distribution = [{"nota": i, "frequencia": int((valid_score == i).sum()),
                          "percentual": float(100*(valid_score == i).sum()/len(valid_score))
                          if len(valid_score) else None}
                         for i in range(11)]
    quality = {"recebidos": len(data), "elegiveis": len(eligible),
               "duplicatas_exatas_excluidas": int(exact_duplicate.sum()),
               "linhas_em_duplicatas_sem_carimbo_requerem_revisao": int(response_duplicate.sum()),
               "sem_consentimento": int((~consent).sum()),
               "sem_exploracao_declarada": int((~explored).sum()),
               "unidade": "Submissão elegível; independência pessoal não comprovada",
               "procedencia": "Todos os registros declarados reais pelo autor; não há autenticação externa",
               "sinteticos_identificados": 0,
               "nao_confirmados_na_classificacao_operacional": 0}
    return eligible, pd.DataFrame(result_rows), pd.DataFrame(frequencies), note, note_distribution, quality


def crossed(eligible):
    rows = []
    # Um único agrupamento de perfil por cruzamento; sem combinações identificadoras.
    definitions = [
        ("experiencia_vs_compreensao", 4, lambda v: "Frequente/ocasional" if v in
         {"Frequentemente", "Ocasionalmente"} else "Poucas vezes/nunca", 15),
        ("area_vs_utilidade_indices", 2, lambda v: "Agrônomo" if v == "Engenheiro agrônomo"
         else "Demais áreas", 27),
        ("conhecimento_vs_autonomia", 3, lambda v: "Avançado/especialista" if v in
         {"Avançado", "Especialista"} else "Básico/intermediário", 18),
        ("experiencia_vs_nota", 4, lambda v: "Frequente/ocasional" if v in
         {"Frequentemente", "Ocasionalmente"} else "Poucas vezes/nunca", 48),
        ("compreensao_vs_intencao", 15, lambda v: "Concorda (4–5)" if
         AGREEMENT.get(v, 0) >= 4 else ("Discorda/neutro (1–3)" if v in AGREEMENT else None), 41),
        ("utilidade_mapas_vs_nota", 28, lambda v: "Útil/muito útil (4–5)" if
         USEFULNESS.get(v, 0) >= 4 else ("Nada/pouco/moderadamente útil (1–3)"
         if v in USEFULNESS else None), 48),
    ]
    for name, index, grouping, target in definitions:
        groups = eligible.iloc[:, index].map(normalized).map(grouping)
        for group in groups.dropna().unique():
            values = eligible.loc[groups == group].iloc[:, target]
            mapping = USEFULNESS if target == 27 else AGREEMENT
            numeric = (pd.to_numeric(values, errors="coerce") if target == 48
                       else values.map(normalized).map(mapping))
            numeric = numeric.dropna()
            if len(numeric) < 5:
                rows.append({"cruzamento": name, "grupo": group,
                             "estado": "Suprimido: menos de cinco respostas válidas"})
                continue
            rows.append({"cruzamento": name, "grupo": group,
                         "estado": "Descritivo; sem inferência causal",
                         "n_valido": len(numeric), **numbers_stats(numeric)})
    return pd.DataFrame(rows)


def qualitative(eligible):
    config = json.loads((BASE / "codificacao.json").read_text())
    known = {row["text_sha256"]: row["codigos"] for row in config["registros"]}
    by_theme = {code: set() for code in config["temas"]}
    by_question = {code: Counter() for code in config["temas"]}
    pending = 0
    coded_cells = 0
    for row_id, row in eligible.iterrows():
        mapping = known.get(text_digest(row))
        if mapping is None:
            pending += 1
            continue
        for index in range(43, 48):
            answer = normalized(row.iloc[index])
            codes = mapping.get(str(index), [])
            if answer and not codes:
                raise ValueError("Texto preenchido sem codificação manual.")
            if not answer and codes:
                raise ValueError("Códigos atribuídos a texto ausente.")
            coded_cells += bool(answer)
            for code in codes:
                by_theme[code].add(row_id)
                by_question[code][str(index)] += 1
    themes = []
    for code, definition in config["temas"].items():
        quote = definition["trecho"]
        # Citações só são publicadas se existirem literalmente no corpus elegível.
        if not any(quote in str(row.iloc[i]) for _, row in eligible.iterrows()
                   for i in range(43, 48)):
            quote = ""
        themes.append({"codigo": code, "categoria": definition["nome"],
                       "descricao": definition["descricao"],
                       "registros_com_tema": len(by_theme[code]),
                       "n_codificado": len(eligible)-pending,
                       "percentual_registros_codificados": 100*len(by_theme[code])/(len(eligible)-pending)
                       if len(eligible)>pending else None,
                       "aspectos_positivos": by_question[code]["43"],
                       "dificuldades": by_question[code]["44"],
                       "melhorias": by_question[code]["45"],
                       "aplicacoes": by_question[code]["46"],
                       "comentarios": by_question[code]["47"],
                       "trecho_anonimizado": quote, "implicacao": definition["implicacao"]})
    return pd.DataFrame(themes), {"registros_pendentes_codificacao": pending,
                                 "celulas_discursivas_codificadas": coded_cells}


def run(source, output, new_source_confirmed=False):
    before = digest(source)
    confirmed_snapshot = "9adb66b330103ca858c37d7dc6cdb5e4e954f09f749a0c122fa6e6b2f4f5de59"
    if before != confirmed_snapshot and not new_source_confirmed:
        raise ValueError("Fonte diferente do recorte confirmado. Conferir procedência e usar "
                         "--confirmar-procedencia somente com nova confirmação do responsável.")
    book = pd.ExcelFile(source)
    frame = pd.read_excel(book, sheet_name=SHEET)
    if frame.iloc[:, 43:48].astype(str).eq("Comentário sintético").any(axis=None):
        raise ValueError("Correspondência com fixture sintética: segregar e conferir antes de publicar.")
    eligible, items, frequencies, note, distribution, quality = analyze_frame(frame)
    output.mkdir(parents=True, exist_ok=True)
    items.to_csv(output / "estatisticas_descritivas.csv", index=False)
    frequencies.to_csv(output / "distribuicoes.csv", index=False)
    names = {"perfil": "perfil_participantes", "tarefas": "execucao_funcionalidades",
             "usabilidade": "avaliacao_usabilidade", "utilidade": "utilidade_funcionalidades",
             "aplicabilidade": "aplicabilidade"}
    for group, name in names.items():
        table = frequencies if group == "perfil" else items
        table[table.grupo == group].to_csv(output / f"{name}.csv", index=False)
    pd.DataFrame([note]).to_csv(output / "avaliacao_geral.csv", index=False)
    pd.DataFrame(distribution).to_csv(output / "distribuicao_notas.csv", index=False)
    crossed(eligible).to_csv(output / "cruzamentos.csv", index=False)
    themes, qual_quality = qualitative(eligible)
    themes.to_csv(output / "categorias_qualitativas.csv", index=False)
    original = BASE / "dados_originais/respostas_recebidas.xlsx"
    audit_path = BASE / "privado/retificacao_datas.json"
    audit = json.loads(audit_path.read_text()) if audit_path.exists() else {}
    dates = pd.to_datetime(eligible.iloc[:, 0], errors="coerce")
    quality.update(qual_quality)
    quality.update({
        "abas": {name: list(pd.read_excel(book, sheet_name=name).shape)
                 for name in book.sheet_names},
        "colunas": frame.shape[1],
        "original_sha256": digest(original) if original.exists() else audit.get("original_sha256"),
        "analisado_sha256": before,
        "retificacao_autorizada": {k: audit.get(k) for k in
                                 ["authorization", "changed_cells", "answers_unchanged"]},
        "periodo_carimbos_corrigidos": [str(dates.min().date()), str(dates.max().date())],
        "datas_invalidas": int(dates.isna().sum()),
        "ausentes_por_coluna": [{"coluna": i+1, "pergunta": normalized(c),
                                "ausentes": int(frame[c].isna().sum())}
                               for i, c in enumerate(frame.columns)],
        "sinteticos_comparados": {
            "arquivo": "tests/test_user_survey_analysis.py",
            "correspondencias_texto_distintivo": int(frame.iloc[:, 43:48].astype(str).eq(
                "Comentário sintético").any(axis=1).sum()),
            "limite": "Comparação com fixtures locais conhecidas; não certifica autenticidade externa"},
        "ambiente": {"python": platform.python_version(), "pandas": pd.__version__,
                     "numpy": np.__version__, "openpyxl": openpyxl.__version__},
        "versao_publica": "Avaliou-se versão anterior às correções; commit e intervalo de publicação não fornecidos",
        "nota": note,
    })
    inventory = []
    for index, column in enumerate(frame.columns):
        group = next((name for name, indices in GROUPS.items() if index in indices),
                     "nota" if index == 48 else "triagem" if index in {1,14,49} else "carimbo")
        ordinal = USEFULNESS if group == "utilidade" else AGREEMENT
        inventory.append({
            "coluna": index+1, "pergunta": normalized(column), "grupo": group,
            "categorias_observadas": sorted(set(frame.iloc[:, index].map(normalized))-{""})
            if group not in {"abertas", "carimbo"} and index != 49 else [],
            "escala_mapeada": ordinal if group in {
                "utilidade", "usabilidade", "aplicabilidade"} else None,
        })
    (BASE / "instrumento.json").write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2)+"\n")
    assert digest(source) == before, "A análise modificou a fonte."
    (output / "qualidade.json").write_text(json.dumps(quality, ensure_ascii=False, indent=2)+"\n")
    return quality


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=BASE / "resultados")
    parser.add_argument("--confirmar-procedencia", action="store_true",
                        help="Registrar nova confirmação do responsável para uma fonte atualizada.")
    args = parser.parse_args()
    print(json.dumps(run(args.input, args.output, args.confirmar_procedencia),
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
