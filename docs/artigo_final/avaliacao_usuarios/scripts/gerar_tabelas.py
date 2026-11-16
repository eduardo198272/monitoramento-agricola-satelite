"""Tabelas e indicadores derivados dos CSV, sem copiar respostas individuais."""

import json
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parents[1]
RESULTS = BASE / "resultados"


def tex(value):
    return str(value).replace("\\", r"\textbackslash{}").replace("&", r"\&").replace(
        "%", r"\%").replace("_", r"\_").replace("#", r"\#")


def number(value, digits=1):
    return f"{float(value):.{digits}f}".replace(".", ",")


def table(caption, label, layout, header, rows):
    title, _, note = caption.partition(". ")
    return "\n".join([
        r"\begin{table*}[htbp]", r"\centering\small",
        r"\caption{"+title+".}", r"\label{"+label+"}",
        r"\begin{tabular}{"+layout+"}", r"\hline",
        header+r"\\ \hline", *[row+r"\\" for row in rows],
        r"\hline", r"\end{tabular}",
        r"\fonteTCC{dados da pesquisa (2026).}",
        r"\notaTCC{"+note+"}", r"\end{table*}", ""])


def generate():
    items = pd.read_csv(RESULTS/"estatisticas_descritivas.csv").set_index("coluna")
    freq = pd.read_csv(RESULTS/"distribuicoes.csv")
    note = pd.read_csv(RESULTS/"avaliacao_geral.csv").iloc[0]
    quality = json.loads((RESULTS/"qualidade.json").read_text())
    macros = {"UsuariosN": str(quality["elegiveis"]), "UsuariosMedia": number(note.media,2),
              "UsuariosMediaEN": f"{note.media:.2f}",
              "UsuariosDP": number(note.dp_amostral,2),
              "UsuariosMediana": number(note.mediana,0), "UsuariosModa": str(int(note.modas)),
              "UsuariosMinimo": number(note.minimo,0), "UsuariosMaximo": number(note.maximo,0),
              "UsuariosQum": number(note.q1,0), "UsuariosQtres": number(note.q3,0)}
    for name, column in [("Compreensao",16),("Intuitividade",17),("Tempo",22),
                         ("Visual",24),("Indices",28),("Pixel",30),("Series",31),
                         ("Intencao",42),("Recomendacao",43),("Clima",39)]:
        row = items.loc[column]
        for suffix, field in [("N","n_valido"),("Pos","positivas_4_5"),
                              ("Neg","negativas_1_2"),("NC","nao_avaliou")]:
            macros[f"Us{name}{suffix}"] = number(row[field],0)
        macros[f"Us{name}Pct"] = number(row["positivas_4_5_pct_validas"])
    (RESULTS/"indicadores.tex").write_text(
        "% Gerado de CSV; atualizar pelo script, não manualmente.\n"+
        "\n".join(r"\newcommand{\%s}{%s}"%(key,value) for key,value in macros.items())+"\n")
    utility = items[items.grupo == "utilidade"]
    rows = []
    for _, r in utility.iterrows():
        rows.append(f"{tex(r.rotulo)} & {int(r.n_valido)} & {int(r.mediana)} & "
                    f"{number(r.q1)}--{number(r.q3)} & "
                    f"{int(r.positivas_4_5)}/{int(r.n_valido)} "
                    f"({number(r.positivas_4_5_pct_validas)}\\%) & "
                    f"{int(r.negativas_1_2)} & {int(r.nao_avaliou)}")
    (RESULTS/"tabela_utilidade.tex").write_text(table(
        "Utilidade percebida. Med.: mediana; Q1--Q3: quartis; 4--5: útil/muito útil; "
        "1--2: nada/pouco útil; NC: não conseguiu avaliar. Percentuais usam o n válido do item.",
        "tab:usuarios-utilidade", r"p{0.37\textwidth}cccp{0.18\textwidth}cc",
        "Recurso & n & Med. & Q1--Q3 & 4--5 & 1--2 & NC", rows))
    tasks = items[items.grupo == "tarefas"]
    rows = [f"{tex(r.rotulo)} & {int(r.sem_ajuda)} & {int(r.com_ajuda)} & "
            f"{int(r.tentativa_sem_sucesso)} & {int(r.nao_tentou)} & "
            f"{int(r.concluiram)}/{int(r.tentaram)} ({number(r.conclusao_pct_tentativas)}\\%)"
            for _,r in tasks.iterrows()]
    (RESULTS/"tabela_tarefas.tex").write_text(table(
        "Execução autodeclarada. SA: sem ajuda; CA: com ajuda; F: tentou sem sucesso; "
        "NT: não tentou. Conclusão: (SA+CA)/(SA+CA+F).",
        "tab:usuarios-tarefas", r"p{0.44\textwidth}ccccp{0.22\textwidth}",
        "Atividade & SA & CA & F & NT & Conclusão entre tentativas", rows))
    themes = pd.read_csv(RESULTS/"categorias_qualitativas.csv")
    selected = ["VISUAL","INTERACAO","ALERTA","QUALIDADE","DESEMPENHO","MOBILIDADE"]
    rows = []
    for code in selected:
        r = themes[themes.codigo==code].iloc[0]
        rows.append(f"{tex(r.categoria)} & {int(r.registros_com_tema)} & "
                    f"``{tex(r.trecho_anonimizado)}'' & {tex(r.implicacao)}")
    (RESULTS/"tabela_temas.tex").write_text(table(
        "Categorias temáticas selecionadas. "
        "n conta registros que mencionam o tema em qualquer uma das cinco perguntas; "
        "categorias não exclusivas. Frequências completas, definições e exemplos estão no material complementar.",
        "tab:usuarios-temas", r"p{0.20\textwidth}cp{0.30\textwidth}p{0.34\textwidth}",
        "Categoria & n & Trecho literal sem identificação & Implicação", rows))
    text = [
        "# Resultados da avaliação com usuários", "",
        "Análise descritiva das respostas coletadas no questionário de avaliação com usuários.",
        "Gerado pelos CSV; a amostragem por adesão e o autorrelato delimitam a interpretação.", "",
        f"Recebidas/elegíveis: **{quality['recebidos']}/{quality['elegiveis']}**. "
        f"Período das respostas analisadas: {' a '.join(quality['periodo_carimbos_corrigidos'])}.", "",
        "## Avaliação geral", "",
        f"n={int(note.n_valido)}; média={number(note.media,2)}; DP amostral={number(note.dp_amostral,2)}; "
        f"mediana={number(note.mediana,0)}; moda={int(note.modas)}; "
        f"Q1={number(note.q1,0)}; Q3={number(note.q3,0)}; "
        f"mínimo={number(note.minimo,0)}; máximo={number(note.maximo,0)}.", "",
        "## Distribuições e estatísticas por item", "",
        "Frequências completas, incluindo categorias de frequência zero, em `resultados/distribuicoes.csv`.",
        "Ausência, impossibilidade de avaliar e invalidade são contabilizadas separadamente.",
        "Médias/DP dos códigos ordinais são complementares; não representam intervalos de percepção comprovadamente iguais.", "",
        "| Item | n | Mediana | Q1–Q3 | Positivas 4–5 | Negativas 1–2 | Não avaliou |",
        "|---|---:|---:|---|---|---:|---:|"]
    for _,r in items[items.grupo.isin(["usabilidade","utilidade","aplicabilidade"])].iterrows():
        text.append(f"| {r.rotulo} | {int(r.n_valido)} | {int(r.mediana)} | "
                    f"{number(r.q1)}–{number(r.q3)} | {int(r.positivas_4_5)} "
                    f"({number(r.positivas_4_5_pct_validas)}%) | {int(r.negativas_1_2)} | {int(r.nao_avaliou)} |")
    text += ["", "## Codificação temática", "",
             f"{quality['celulas_discursivas_codificadas']} células discursivas codificadas; "
             f"{quality['registros_pendentes_codificacao']} registros pendentes. "
             "Contagem por registro, uma vez por tema, admitindo múltiplos temas. "
             "Não se atribuiu concordância entre codificadores ou saturação teórica.", "",
             "| Categoria / definição | n registros | Trecho representativo | Implicação |",
             "|---|---:|---|---|"]
    for r in themes.itertuples():
        text.append(f"| {r.categoria}: {r.descricao} | {r.registros_com_tema} | "
                    f"“{r.trecho_anonimizado}” | {r.implicacao} |")
    text += ["", "## Interpretação e limites", "",
              f"- Maior proporção de avaliações 4–5 não significa maior alcance: pixel tem {int(items.loc[30].nao_avaliou)} impossibilidades de avaliação.",
             "- Demarcação e séries/anomalias combinam interesse com dificuldade; percepção de facilidade não substitui conclusão de tarefa.",
             "- Relatos de comparação lado a lado, alertas coloridos e estação meteorológica são percepções/expectativas, não confirmação dessas funcionalidades.",
             "- As categorias de desempenho são relatos, não cronometração; as aplicações agronômicas propostas não foram demonstradas.",
             "- Gráficos, cruzamentos e avaliações negativas permanecem disponíveis, sem seleção somente de resultados favoráveis.",
             "- Dados referem-se à versão pública anterior às correções; não atribuir aos respondentes avaliação das correções locais.",
             "- A unidade de análise é a submissão ao questionário; os cruzamentos são exploratórios, sem testes de hipótese ou generalização populacional.",
             "- A codificação qualitativa e a interpretação requerem aprovação substantiva do autor.", ""]
    (BASE/"RESULTADOS.md").write_text("\n".join(text))


if __name__ == "__main__":
    generate()
