"""Confere compilação e preservação de contratos; não aprova conteúdo acadêmico."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess


BASE = Path(__file__).resolve().parents[1]
ARTICLE = BASE.parent
ROOT = BASE.parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", type=Path, required=True)
    args = parser.parse_args()
    files = {}

    def visit(path):
        if path in files:
            return
        files[path] = re.sub(r"(?<!\\)%[^\n]*", "", path.read_text())
        for name in re.findall(r"\\input\{([^}]+)\}", files[path]):
            visit(ARTICLE/f"{name}.tex")

    visit(ARTICLE/"Relatorio_Final.tex")
    text = "\n".join(files.values())
    citations = {key.strip() for group in re.findall(r"\\cite\w*\{([^}]+)\}",text)
                 for key in group.split(",")}
    keys = re.findall(r"@\w+\{([^,]+),",(ARTICLE/"referencias.bib").read_text())
    labels = re.findall(r"\\label\{([^}]+)\}",text)
    refs = {key.strip() for group in re.findall(r"\\(?:c|C|eq)?ref\{([^}]+)\}",text)
            for key in group.split(",")}
    log = (args.build_dir/"Relatorio_Final.log").read_text()
    aux = (args.build_dir/"Relatorio_Final.aux").read_text()
    compiled = set(re.findall(r"\\bibcite\{([^}]+)\}",aux))
    errors = re.findall(r"^.*(?:undefined|^! |Float too large|Too many unprocessed floats).*$",
                        log,re.M)
    assert not citations-set(keys), "Citação sem entrada."
    assert not citations-compiled, "Citação não compilada."
    assert not refs-set(labels), "Referência sem rótulo."
    assert not errors, errors
    assert all(n == 1 for n in Counter(labels).values())
    assert all(n == 1 for n in Counter(keys).values())
    original = subprocess.check_output(
        ["git","show","af120d5:docs/artigo_final/CC-EC_TF-TC.cls"],cwd=ROOT)
    assert original == (ARTICLE/"CC-EC_TF-TC.cls").read_bytes()
    env = r"\\begin\{(?:equation|align)\}.*?\\end\{(?:equation|align)\}"
    equations = re.findall(env,text,re.S)
    old = []
    # Comparar apenas as fontes com equações: inserções textuais não mudam a matemática.
    for name in ["final_2_fundamentacao.tex","final_3_metodos.tex","final_3a_implementacao.tex"]:
        raw = subprocess.check_output(["git","show",f"af120d5:docs/artigo_final/{name}"],
                                      cwd=ROOT,text=True)
        old.extend(re.findall(env,raw,re.S))
    assert equations == old
    pdf = args.build_dir/"Relatorio_Final.pdf"
    result = {"passed":True, "sources":len(files), "cited_keys":sorted(citations),
              "undefined":errors, "equation_environments_unchanged":len(equations),
              "institutional_class_unchanged":True,
              "figures":len(re.findall(r"\\contentsline \{figure\}",aux)),
              "tables":len(re.findall(r"\\contentsline \{table\}",aux)),
              "overfull":re.findall(r"Overfull \\[hv]box[^\n]*",log),
              "pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),
              "pdfinfo":subprocess.check_output(["pdfinfo",str(pdf)],text=True).splitlines(),
              "source_hashes":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in files}}
    (BASE/"resultados/compilacao.json").write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
