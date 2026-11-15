"""Conferência estrutural da revisão; não substitui leitura científica ou visual."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[3]
ARTICLE = ROOT / "docs/artigo_final"


def original(path, base):
    return subprocess.check_output(
        ["git", "show", f"{base}:{path.relative_to(ROOT).as_posix()}"],
        cwd=ROOT,
        text=True,
    )


def clean(text):
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def values(pattern, text):
    return re.findall(pattern, clean(text))


def citations(text):
    return {
        key.strip()
        for group in values(r"\\cite\w*\{([^}]+)\}", text)
        for key in group.split(",")
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="af120d5d25bbde5446541917ea0e9fe3c50c4425")
    parser.add_argument("--build-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    files = {}

    def visit(path):
        if path in files:
            return
        files[path] = path.read_text()
        for name in values(r"\\input\{([^}]+)\}", files[path]):
            visit(ARTICLE / f"{name}.tex")

    visit(ARTICLE / "Relatorio_Final.tex")
    current = "\n".join(files.values())
    previous = "\n".join(original(p, args.base) for p in files)
    bibliography = (ARTICLE / "referencias.bib").read_text()
    keys = values(r"@\w+\{([^,]+),", bibliography)
    labels = values(r"\\label\{([^}]+)\}", current)
    references = {
        key.strip()
        for group in values(r"\\(?:c|C|eq)?ref\{([^}]+)\}", current)
        for key in group.split(",")
    }
    structural = {
        "equations": r"\\begin\{(?:equation|align)\}.*?\\end\{(?:equation|align)\}",
        "headings": r"\\(?:sub)*section\{[^}]+\}",
        "objectives": r"\\item\[\s*\\textbf\{OE\d+\}\][^\n]*",
        "labels": r"\\label\{[^}]+\}",
    }
    preserved = {
        name: re.findall(pattern, previous, re.S) == re.findall(pattern, current, re.S)
        for name, pattern in structural.items()
    }
    preserved["cited_keys"] = citations(previous) == citations(current)
    preserved["institutional_class"] = (
        (ARTICLE / "CC-EC_TF-TC.cls").read_text()
        == original(ARTICLE / "CC-EC_TF-TC.cls", args.base)
    )
    manifest = json.loads(
        (ARTICLE / "evidencias/demonstracao_real/manifesto.json").read_text()
    )
    mismatches = [
        name
        for name, expected in manifest["code_sha256"].items()
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected
    ]
    log = (args.build_dir / "Relatorio_Final.log").read_text()
    bbl = (args.build_dir / "Relatorio_Final.bbl").read_text()
    compiled_keys = set(values(r"\\harvarditem(?:\[[^\]]*\])?\{[^}]*\}\{[^}]*\}\{[^}]*\}\{([^}]+)\}", bbl))
    # O estilo institucional pode variar na representação dos autores.
    aux = (args.build_dir / "Relatorio_Final.aux").read_text()
    compiled_keys.update(values(r"\\bibcite\{([^}]+)\}", aux))
    missing_citations = sorted(citations(current) - set(keys))
    missing_references = sorted(references - set(labels))
    missing_compiled = sorted(citations(current) - compiled_keys)
    unresolved = re.findall(
        r"^.*(?:Citation .*undefined|Reference .*undefined|There were undefined|^! ).*$",
        log,
        re.M,
    )
    captures = values(r"\\capturatcc\{([^}]+)\}", current)
    absent_captures = [
        name for name in captures if not (ARTICLE / f"fig/capturas/{name}.png").exists()
    ]
    pdf = args.build_dir / "Relatorio_Final.pdf"
    pdfinfo = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
    result = {
        "base": args.base,
        "sources": [str(p.relative_to(ROOT)) for p in files],
        "preserved": preserved,
        "equation_environments": len(re.findall(structural["equations"], current, re.S)),
        "cited_keys": sorted(citations(current)),
        "uncited_bibliography": sorted(set(keys) - citations(current)),
        "missing_citations": missing_citations,
        "missing_references": missing_references,
        "missing_compiled_keys": missing_compiled,
        "duplicate_bibliography_keys": [k for k, n in Counter(keys).items() if n > 1],
        "duplicate_labels": [k for k, n in Counter(labels).items() if n > 1],
        "unresolved_log": unresolved,
        "absent_optional_captures": absent_captures,
        "code_files_checked_against_demo": len(manifest["code_sha256"]),
        "code_mismatches": mismatches,
        "overfull_warnings": re.findall(r"Overfull \\[hv]box[^\n]*", log),
        "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "pdfinfo": pdfinfo.splitlines(),
    }
    result["passed"] = (
        all(preserved.values())
        and not any(
            result[name]
            for name in (
                "missing_citations", "missing_references", "missing_compiled_keys",
                "duplicate_bibliography_keys", "duplicate_labels", "unresolved_log",
                "code_mismatches",
            )
        )
    )
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
