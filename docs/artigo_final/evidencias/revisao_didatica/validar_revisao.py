"""Confere preservação documental da revisão didática; não mede legibilidade."""

from collections import Counter
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess


BASE = Path(__file__).resolve().parent
ARTICLE = BASE.parents[1]
ROOT = ARTICLE.parents[1]
REFERENCE = "1862dd7"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", type=Path, required=True)
    args = parser.parse_args()
    files = sorted(ARTICLE.glob("final_*.tex"))
    checks = {}
    diffs = []
    # Únicas repetições numéricas acrescentadas à prosa; nenhum valor foi removido.
    additions = {
        "final_3a_implementacao.tex": Counter({"32": 1}),  # definição de float32
        "final_3_metodos.tex": Counter({"20": 1}),  # explicação do filtro <20
        "final_4_resultados.tex": Counter({"11,73": 1}),  # tempo de testes, não latência
    }
    patterns = {
        "numbered_math": r"\\begin\{(?:equation|align)\}.*?\\end\{(?:equation|align)\}",
        "citations": r"\\cite\w*\{[^}]+\}",
        "labels": r"\\label\{[^}]+\}",
        "cross_references": r"\\(?:c|C|eq)?ref\{[^}]+\}",
        "survey_macros": r"\\(?:Usuarios|Us)[A-Za-z]+(?:\{\})?",
        "tables": r"\\begin\{tabular\}.*?\\end\{tabular\}",
        "figures": r"\\begin\{figure\*?\}.*?\\end\{figure\*?\}",
    }
    for path in files:
        relative = str(path.relative_to(ROOT))
        old = git("show", f"{REFERENCE}:{relative}")
        new = path.read_text()
        item = {}
        for name, pattern in patterns.items():
            before = re.findall(pattern, old, re.S)
            after = re.findall(pattern, new, re.S)
            same = before == after if name == "numbered_math" else Counter(before) == Counter(after)
            assert same, f"{name} mudou em {relative}"
            item[name] = {"unchanged": True, "count": len(after)}
        numeric = r"(?<![A-Za-z_])\d+(?:[.,]\d+)*"
        before = Counter(re.findall(numeric, old))
        after = Counter(re.findall(numeric, new))
        assert not before-after, f"Número removido em {relative}"
        assert after-before == additions.get(path.name, Counter()), f"Número inesperado em {relative}"
        item["numeric_additions_explained"] = dict(after-before)
        item["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        checks[relative] = item
        diffs.append("".join(difflib.unified_diff(
            old.splitlines(True), new.splitlines(True),
            fromfile=f"{REFERENCE}/{relative}", tofile=f"revisado/{relative}")))

    allowed = {str(p.relative_to(ROOT)) for p in files} | {
        "docs/artigo_final/Relatorio_Final.pdf",
        "docs/artigo_final/REVISAO_DIDATICA_ESCRITA.md",
        "docs/artigo_final/README.md",
    }
    changed = set(git("diff", REFERENCE, "--name-only").splitlines())
    assert changed <= allowed, f"Alterações fora do escopo: {changed-allowed}"
    compile_result = json.loads((BASE/"compilacao.json").read_text())
    pdf = args.build_dir/"Relatorio_Final.pdf"
    pdfhash = hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert compile_result["passed"] and not compile_result["undefined"]
    assert pdfhash == compile_result["pdf_sha256"]
    result = {
        "passed": True,
        "baseline_commit": git("rev-parse", REFERENCE).strip(),
        "scope": "Revisão didática; sem nova validação científica ou medição de legibilidade",
        "source_files": checks,
        "other_tracked_content_unchanged": True,
        "unchanged_includes": [
            "aplicação e testes", "bibliografia e classe institucional",
            "resultados gerados e gráficos de usuários", "figuras e capturas",
            "evidências históricas e auditoria científica",
        ],
        "analyzed_workbook_sha256": hashlib.sha256(
            (ROOT/"docs/Respostas – Avaliação da plataforma agrícola – TCC UPF.xlsx").read_bytes()
        ).hexdigest(),
        "pdf_sha256": pdfhash,
        "automated_validation_does_not_replace": [
            "aprovação final de cada seção pelo autor",
            "avaliação de leitura por leitores independentes",
            "resolução das pendências científicas e institucionais",
        ],
    }
    assert result["analyzed_workbook_sha256"] == "9adb66b330103ca858c37d7dc6cdb5e4e954f09f749a0c122fa6e6b2f4f5de59"
    (BASE/"preservacao.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    (BASE/"alteracoes.diff").write_text("\n".join(diffs))
    print("Preservação conferida nos dez arquivos; equações, citações, dados e figuras intactos.")


if __name__ == "__main__":
    main()
