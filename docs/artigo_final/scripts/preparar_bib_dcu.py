"""Projeta os metadados preservados para os campos suportados pelo dcu.

Não gera bibitems, não modifica o .bst e não redefine autores/anos.
DOI, data de acesso, versão e identificador eletrônico são expostos em note
porque o dcu original não lê esses campos. URL usa o suporte nativo do estilo.
Quando DOI e URL têm exatamente o mesmo endereço, só a URL nativa é exibida;
os dois campos continuam preservados nos metadados.
"""

from pathlib import Path
import re

from pybtex.database import parse_file
from pybtex.database.output.bibtex import Writer


BASE = Path(__file__).resolve().parents[1]


def main():
    data = parse_file(BASE / "referencias_normalizadas.bib")
    original = parse_file(BASE / "referencias.bib")
    for key, entry in data.entries.items():
        f = entry.fields
        notes = [f["note"]] if f.get("note") else []
        # Proteção BibTeX de siglas/nomes próprios: os caracteres do título
        # não mudam; evita que change.case$ do dcu os converta para minúsculas.
        protected = r"SI|GIS|POWER|NDVI|NDWI|NDMI|MODIS|API|Kiro|Tessl|Sentinel"
        f["title"] = re.sub(
            r"(?<!\{)\b(" + protected + r")\b(?!\})",
            r"{\1}", f["title"])
        # Localizadores bibliográficos existentes, não comentários de auditoria.
        old_note = original.entries[key].fields.get("note", "")
        for pattern in [r"Cap\.\s*\d+", r"Seção\s+\d+(?:\.\d+)*",
                        r"Registro NASA NTRS\s+\d+", r"^28 out\. 2026"]:
            match = re.search(pattern, old_note)
            if match:
                notes.append(match[0].rstrip(".") + ".")
        if f.get("eid"):
            notes.append("Identificador do artigo: " + f["eid"] + ".")
        if f.get("version"):
            notes.append("Versão " + f["version"] + ".")
        if entry.type == "misc":
            if f.get("edition"):
                notes.append(f["edition"] + ". ed.")
            if f.get("publisher"):
                notes.append((f["address"] + ": " if f.get("address") else "")
                             + f["publisher"] + ".")
        if f.get("doi") and f.get("url") != "https://doi.org/" + f["doi"]:
            notes.append(r"DOI: \url{https://doi.org/" + f["doi"] + "}.")
        if f.get("urldate"):
            notes.append("Acesso em: " + f["urldate"] + ".")
        if notes:
            f["note"] = " ".join(notes)
        # O argumento de \harvardurl é lido antes de \url: percentuais
        # literais virariam comentários TeX. A base conserva a URL original;
        # \url interpreta \% como %, inclusive no destino do hyperlink.
        if f.get("url"):
            f["url"] = re.sub(r"(?<!\\)%", r"\\%", f["url"])

    class SourceWriter(Writer):
        def _encode(self, text):
            return text

    SourceWriter(encoding="UTF-8").write_file(data, BASE / "referencias_institucionais.bib")
    print(f"{len(data.entries)} entradas projetadas para dcu; metadados de origem preservados.")


if __name__ == "__main__":
    main()
