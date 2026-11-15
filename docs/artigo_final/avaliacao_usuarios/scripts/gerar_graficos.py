"""Gráficos agregados; sem dados individuais e sem escalas truncadas."""

import argparse
from pathlib import Path
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE = Path(__file__).resolve().parents[1]
COLORS = ["#a63d32", "#dc8a43", "#a6a6a6", "#66a987", "#176044"]


def style():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.titleweight": "bold", "savefig.facecolor": "white",
                         "svg.fonttype": "none", "pdf.fonttype": 42})


def save(fig, output, name):
    output.mkdir(parents=True, exist_ok=True)
    for extension in ["pdf", "svg", "png"]:
        fig.savefig(output/f"{name}.{extension}", dpi=300, bbox_inches="tight",
                    metadata={"Creator": "Análise descritiva TCC UPF"}
                    if extension == "pdf" else None)
    plt.close(fig)


def wrap(text, width=48):
    return "\n".join(textwrap.wrap(text, width))


def categorical(freq, column, title, output, name):
    d = freq[freq.coluna == column].sort_values("frequencia")
    fig, ax = plt.subplots(figsize=(9, max(3, len(d)*.55+1.5)))
    ax.barh([wrap(v, 40) for v in d.categoria], d.frequencia, color="#28764e")
    for y, (_, row) in enumerate(d.iterrows()):
        label = f"{row.frequencia} ({row.percentual_valido:.1f}%)".replace(".", ",")
        ax.text(row.frequencia+.25, y, label, va="center", fontsize=9)
    ax.set_xlim(0, max(1, float(d.n_valido.max())*1.22))
    ax.set_xlabel(f"Registros (n válido = {int(d.n_valido.max())})")
    ax.set_title(title, loc="left", pad=14)
    save(fig, output, name)


def stacked(freq, items, group, title, output, name):
    d = items[items.grupo == group]
    task = group == "tarefas"
    colors = ["#176044", "#4391ac", "#cd6b3d", "#b5b5b5"] if task else COLORS
    categories = ["Consegui sem ajuda", "Consegui com ajuda",
                  "Tentei, mas não consegui", "Não tentei"] if task else list(range(1,6))
    legend = categories if task else (
        ["1 Nada útil", "2 Pouco útil", "3 Moderadamente útil", "4 Útil", "5 Muito útil"]
        if group == "utilidade" else
        ["1 Discordo totalmente", "2 Discordo parcialmente", "3 Neutro",
         "4 Concordo parcialmente", "5 Concordo totalmente"])
    labels = [wrap(row.rotulo, 42)+(f"\n(n={row.n_valido})" if task else
              f"\n(n={row.n_valido}; não avaliou={row.nao_avaliou})")
              for row in d.itertuples()]
    fig, ax = plt.subplots(figsize=(10, len(d)*.72+2))
    left = np.zeros(len(d))
    for category, color, label in zip(categories, colors, legend):
        values = []
        for row in d.itertuples():
            sub = freq[(freq.grupo == group) & (freq.coluna == row.coluna)]
            selected = sub[sub.categoria == category] if task else sub[sub.valor == category]
            values.append(float(selected.percentual_valido.iloc[0])
                          if len(selected) and row.n_valido else 0)
        ax.barh(np.arange(len(d)), values, left=left, color=color, label=label, edgecolor="white")
        for y, value in enumerate(values):
            if value >= 9:
                ax.text(left[y]+value/2, y, f"{value:.0f}%", ha="center", va="center",
                        color="white" if color in {"#176044", "#a63d32"} else "#111111", fontsize=9)
        left += np.asarray(values)
    assert np.allclose(left, np.where(d.n_valido.to_numpy()>0,100,0)), (
        "Distribuições não totalizam 100% nos itens válidos.")
    ax.set_yticks(np.arange(len(d)), labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xticks(range(0,101,20))
    ax.set_xlabel("Percentual das respostas válidas do item")
    ax.set_title(title, loc="left", pad=16)
    ax.legend(loc="upper left", bbox_to_anchor=(0, -.11), ncol=2 if task else 3,
              frameon=False, fontsize=9)
    fig.subplots_adjust(left=.40, bottom=.23, top=.92)
    save(fig, output, name)


def generate(results, output):
    style()
    freq = pd.read_csv(results/"distribuicoes.csv")
    items = pd.read_csv(results/"estatisticas_descritivas.csv")
    categorical(freq, 3, "Área de atuação declarada", output, "perfil_profissional")
    categorical(freq, 4, "Conhecimento em agricultura de precisão", output, "familiaridade")
    categorical(freq, 5, "Uso prévio de ferramentas de monitoramento por satélite", output, "experiencia")
    for group, title in [
        ("tarefas", "Execução autodeclarada das atividades — categorias do instrumento"),
        ("usabilidade", "Percepção de uso — concordância ordinal de 1 a 5"),
        ("utilidade", "Utilidade percebida — escala ordinal de 1 a 5"),
        ("aplicabilidade", "Compreensão, aplicabilidade e intenção — concordância de 1 a 5")]:
        stacked(freq, items, group, title, output, group)
    notes = pd.read_csv(results/"distribuicao_notas.csv")
    fig, ax = plt.subplots(figsize=(8,4))
    ax.bar(notes.nota, notes.frequencia, color="#28764e", width=.7)
    for row in notes.itertuples():
        if row.frequencia:
            ax.text(row.nota, row.frequencia+.1, str(row.frequencia), ha="center")
    ax.set_xticks(range(11));ax.set_xlim(-.6,10.6)
    ax.set_ylim(0,max(1,notes.frequencia.max()*1.25))
    ax.set_xlabel("Nota geral (0 a 10)");ax.set_ylabel("Registros")
    ax.set_title(f"Avaliação geral — n válido = {notes.frequencia.sum()}", loc="left")
    save(fig, output, "nota_geral")
    themes = pd.read_csv(results/"categorias_qualitativas.csv").sort_values("registros_com_tema")
    fig, ax = plt.subplots(figsize=(10,8))
    ax.barh([wrap(v,43) for v in themes.categoria], themes.registros_com_tema, color="#367e98")
    for y, row in enumerate(themes.itertuples()):
        ax.text(row.registros_com_tema+.2,y,str(row.registros_com_tema),va="center")
    ax.set_xlim(0,max(1,themes.n_codificado.max()*1.15))
    ax.set_xlabel(f"Registros com menção em ao menos uma resposta (n codificado = {themes.n_codificado.max()})")
    ax.set_title("Temas multirrótulo — percepções e propostas, não eficácia",loc="left")
    save(fig, output, "temas")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=BASE/"resultados")
    parser.add_argument("--output", type=Path, default=BASE/"figuras")
    args = parser.parse_args()
    generate(args.results, args.output)


if __name__ == "__main__":
    main()
