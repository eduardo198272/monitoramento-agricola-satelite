"""Geração editorial explícita para este artigo, não um estilo ABNT universal.

Requer pybtex==0.26.1. Mantém o .bib de origem e gera .bib estruturado,
thebibliography compatível com natbib e inventário de TODAS as entradas.
Não consulta rede nem infere datas exatas de anos de acesso.
"""

from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import unicodedata

from pybtex.database import parse_file
from pybtex.database.output.bibtex import Writer


BASE = Path(__file__).resolve().parents[1]
# Evidências: fontes/datas_paginas.json do cache da quinta rodada.
DATES = {
    "ESA_SENTINEL2": "2026",  # page-last-modified 2026-08-11
    "GOOGLE_EE_ND": "2026",  # Last updated 2026-04-20
    "GOOGLE_EE_DATE": "2023",  # Last updated 2023-10-06
    "GOOGLE_EE_SAMPLE": "2023",
    "GOOGLE_EE_MEDIAN": "2023",
    "GOOGLE_EE_REDUCE": "2026",  # Last updated 2026-04-20
    "GOOGLE_EE_SERVICE_ACCOUNT": "2026",  # 2026-06-09
    "GOOGLE_EE_NONCOMMERCIAL": "2026",  # 2026-09-25
    "GOOGLE_EE_RESAMPLE": "2024",  # 2024-05-30
    "GOOGLE_EE_REGION": "2026",  # 2026-05-29
    "QGIS_VECTOR": "2026",  # Last updated 2026 Mar 16
    "QGIS_RASTER": "2026",
    "QGIS_MAP": "2026",
    "NUMPY_STD": "c2026",  # copyright, não data de publicação
    "NUMPY_POLYFIT": "c2026",
    "STREAMLIT_STATE": "c2026",
    "STREAMLIT_CLOUD_SECRETS": "c2026",
    "BIPM_SI": "2019",  # 9ª edição; não confundir com revisão on-line
}


def plain(value):
    """Somente para ordenar; preservar LaTeX e acentos no texto publicado."""
    value = re.sub(r"\\[\"'`^~]\{?([A-Za-z])\}?", r"\1", value)
    value = re.sub(r"[{}\\]", "", value)
    return "".join(c for c in unicodedata.normalize("NFKD", value)
                   if not unicodedata.combining(c)).casefold()


def surname(person):
    return " ".join(person.last_names)


def full_name(person):
    last = surname(person)
    if person.lineage_names:
        last += " " + " ".join(person.lineage_names)
    if not person.first_names and not person.middle_names:
        return r"\MakeUppercase{" + last + "}"
    # Abreviar uniformemente os prenomes; não expandir iniciais desconhecidas.
    given = person.first_names + person.middle_names
    initials = []
    for word in given:
        initials.append("-".join(part[0] + "." for part in word.split("-") if part))
    result = r"\MakeUppercase{" + last + "}, " + " ".join(initials)
    if person.prelast_names:
        result += " " + " ".join(person.prelast_names)
    return result


def citation_name(entry):
    authors = entry.persons["author"]
    names = [surname(p) for p in authors]
    if len(names) >= 4:
        return names[0] + r" \textit{et al.}"
    if len(names) == 3:
        return names[0] + r"\TCCsep{}" + names[1] + r"\TCCand{}" + names[2]
    # A macro é robusta: somente a composição distingue narrativa/parentética.
    return r"\TCCand{}".join(names)


def highlight(title):
    # Somente título principal, não subtítulo. Chaves internas preservadas.
    main, sep, subtitle = title.partition(": ")
    return r"\textbf{" + main + "}" + (sep + subtitle if sep else "")


def main():
    data = parse_file(BASE / "referencias.bib")
    evidence = BASE / "evidencias/quinta_rodada"
    links_file = evidence / "links.json"
    links = {r["key"]: r for r in json.loads(links_file.read_text())} if links_file.exists() else {}
    texts = "\n".join(p.read_text() for p in BASE.glob("final_*.tex"))
    # As tabelas geradas também podem conter citações.
    texts += (BASE / "figuras_relatorio.tex").read_text()
    cited = {key.strip()
             for group in re.findall(r"\\cite\w*\*?(?:\[[^]]*\])*\{([^}]+)\}", texts)
             for key in group.split(",")}
    assert not cited - set(data.entries), cited - set(data.entries)
    audits = {}
    for key, entry in data.entries.items():
        f = entry.fields
        before = dict(f)
        note = f.pop("note", "")
        urls = re.findall(r"\\url\{([^}]+)\}", note)
        for url in urls:
            if "doi.org/" in url:
                f["doi"] = url.split("doi.org/", 1)[1]
            else:
                f.setdefault("url", url)
        access = re.search(r"(?:Acesso|Acessado) em:?\s*(\d{1,2})\s+([a-zç]+)\.?\s+(\d{4})",
                           note, re.I)
        if access:
            f["urldate"] = f"{access[1]} {access[2]}. {access[3]}"
        if f.get("url") and not f.get("urldate"):
            # Os três textos primários foram efetivamente consultados em 16/11.
            if key in {"GOTEL1994", "BJARNASON2015", "VAITHILINGAM2022"}:
                f["urldate"] = "16 nov. 2026"
        if f.get("doi") and not f.get("url"):
            f["url"] = "https://doi.org/" + f["doi"]
            # Conferência da rodada anterior documentada na auditoria científica.
            # Sem inventar data quando não constava do registro da entrada.
        if not f.get("urldate") and links.get(key, {}).get("consulta"):
            f["urldate"] = links[key]["access_date"]
        if key in DATES:
            f["year"] = DATES[key]
        elif not f.get("year"):
            # Século provável, NÃO um ano de publicação inventado.
            # Requer confirmação bibliográfica para reduzir a incerteza.
            f["year"] = "[20--?]"
        if key in {"WEISS2020", "PHIRI2020", "IZQUIERDO2026"}:
            f["eid"] = f.pop("pages")
        if key == "WAZLAWICK2020":
            entry.type = "book"
        if key == "ISO9241_2018":
            f["publisher"] = "ISO"
        if key == "BIPM_SI":
            f.update(address="Sèvres", publisher="BIPM", edition="9",
                     version="4.01, jun. 2026", doi="10.59161/AUEZ1291")
        if key.startswith("QGIS_"):
            f["version"] = "3.40"
        # Notas de acesso/auditoria ficam no inventário, não no verbete.
        audits[key] = {
            "tipo": entry.type, "citada": key in cited,
            "antes": before, "depois": dict(f),
            "nota_original": note,
            "data": ("Atualização/copyright/edição verificados"
                     if key in DATES else
                     "Século provável; confirmar data do documento"
                     if f["year"] == "[20--?]" else
                     "Ano anterior preservado; ver auditoria científica"),
            "lacunas": [],
        }
        if not f.get("address"):
            audits[key]["lacunas"].append("Local não identificado na entrada")
        if f.get("url") and not f.get("urldate"):
            audits[key]["lacunas"].append("Data efetiva de acesso não registrada na entrada")
        if entry.type in {"mastersthesis", "phdthesis"}:
            audits[key]["lacunas"].append("Conferir grau, instituição/unidade e extensão no original")
        if f["year"] == "[20--?]":
            audits[key]["lacunas"].append("Data apenas aproximada; século provável")

    def sort_key(key):
        entry = data.entries[key]
        authors = "; ".join(plain(str(p)) for p in entry.persons["author"])
        return authors, plain(entry.fields["year"]), plain(entry.fields["title"])

    ordered = sorted(cited, key=sort_key)
    groups = defaultdict(list)
    for key in ordered:
        entry = data.entries[key]
        groups[(citation_name(entry), entry.fields["year"].removeprefix("c"))].append(key)
    suffixes = {}
    for keys in groups.values():
        for i, key in enumerate(keys):
            suffixes[key] = chr(97+i) if len(keys) > 1 else ""
    lines = [
        "% Gerado por scripts/gerar_referencias_normalizadas.py; não editar.",
        r"\begin{thebibliography}{99}",
    ]
    for key in ordered:
        e = data.entries[key]
        f = e.fields
        suffix = suffixes[key]
        year = f["year"] + suffix
        labelyear = f["year"].removeprefix("c") + suffix
        author = "; ".join(full_name(p) for p in e.persons["author"])
        # Colchetes nas datas dentro de um argumento opcional precisam de grupo.
        label = citation_name(e) + "({" + labelyear + "})"
        parts = [r"\bibitem[" + label + "]{" + key + "}", author.rstrip(".") + "."]
        title = f["title"]
        if e.type == "article":
            parts += [title + ".", highlight(f["journal"]) + ", "
                      + f.get("address", "[S. l.]") + ","]
            for field, prefix in [("volume", "v."), ("number", "n."),
                                  ("pages", "p."), ("eid", "art.")]:
                if f.get(field):
                    parts.append(prefix + " " + f[field] + ",")
            parts.append(year + ".")
        elif e.type in {"inproceedings", "incollection"}:
            parts += [title + ".", "In:"]
            if e.persons.get("editor"):
                parts.append("; ".join(full_name(p) for p in e.persons["editor"])
                             + " (ed.).")
            parts += [highlight(f["booktitle"]) + ".",
                      f.get("address", "[S. l.]") + ": "
                      + f.get("publisher", "[s. n.]") + ", " + year + "."]
            if f.get("series"):
                parts.append("(" + f["series"] + ", v. " + f["volume"] + ").")
            if f.get("pages"):
                parts.append("p. " + f["pages"] + ".")
            if key == "BENDER2020":
                parts.append("cap. 11.")
        elif e.type in {"mastersthesis", "phdthesis"}:
            parts += [highlight(title) + ".", year + ".",
                      f.get("type", "Tese") + " -- " + f["school"] + ", "
                      + f.get("address", "[S. l.]") + ", " + year + "."]
        else:
            parts.append(highlight(title) + ".")
            if f.get("edition"):
                parts.append(f["edition"] + ". ed.")
            if f.get("version"):
                parts.append("Versão " + f["version"] + ".")
            publisher = f.get("publisher", f.get("institution"))
            if publisher:
                parts.append(f.get("address", "[S. l.]") + ": " + publisher
                             + ", " + year + ".")
            else:
                parts.append(f.get("address", "[S. l.]") + ", " + year + ".")
        if f.get("doi"):
            parts.append(r"DOI: \url{https://doi.org/" + f["doi"] + "}.")
        if f.get("url"):
            parts.append(r"Disponível em: \url{" + f["url"] + "}.")
        if f.get("urldate"):
            parts.append("Acesso em: " + f["urldate"] + ".")
        lines.append("\n".join(parts))
    lines.append(r"\end{thebibliography}")
    (BASE / "referencias_normalizadas.tex").write_text("\n\n".join(lines) + "\n")
    class SourceWriter(Writer):
        # As entradas já contêm LaTeX; não escapar _ ou & dentro de URLs.
        def _encode(self, text):
            return text

    SourceWriter(encoding="UTF-8").write_file(data, BASE / "referencias_normalizadas.bib")
    report = {
        "entradas": len(data.entries), "citadas": len(cited),
        "nao_citadas": sorted(set(data.entries)-cited),
        "duplicacoes_de_url": {url: n for url, n in
                               Counter(e.fields.get("url") for e in data.entries.values()).items()
                               if url and n > 1},
        "ordem": ordered, "entradas_auditadas": audits,
        "limite": "Geração editorial local; não certifica cumprimento integral da NBR 6023.",
    }
    evidence.mkdir(parents=True, exist_ok=True)
    (evidence / "referencias.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"{len(data.entries)} entradas examinadas; {len(cited)} citadas.")


if __name__ == "__main__":
    main()
