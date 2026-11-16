"""Valida preservação da rodada PA; não certifica procedência, ciência ou aprovação."""

import argparse
from collections import Counter
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess

ARTICLE = Path(__file__).resolve().parents[1]
ROOT = ARTICLE.parents[1]
OUT = ARTICLE / "evidencias/revisao_final_pa"
BASELINE = "f31d0a5"


def git(*args, binary=False):
    return subprocess.check_output(
        ["git", "-c", "core.quotepath=false", *args], cwd=ROOT, text=not binary
    )


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path)
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    before = git("rev-parse", BASELINE).strip()
    paths = git("ls-tree", "-r", "--name-only", BASELINE).splitlines()
    protected = []
    for relative in paths:
        # Todos os arquivos fora do artigo, resultados, figuras e scripts antigos
        # da avaliação são protegidos; somente documentação/LaTeX da rodada muda.
        protect = not relative.startswith("docs/artigo_final/") or any(
            relative.startswith(f"docs/artigo_final/{directory}/")
            for directory in (
                "avaliacao_usuarios/resultados", "avaliacao_usuarios/figuras",
                "avaliacao_usuarios/scripts", "fig", "evidencias",
            )
        ) or relative.endswith(".cls")
        if relative == "docs/artigo_final/fig/conceitos.tex":
            old = git("show", f"{BASELINE}:{relative}")
            new = (ROOT / relative).read_text()
            # Apenas a primeira figura não fundamentada foi retirada.
            assert old.split("\\end{figure*}", 1)[1].strip() == new.strip()
            protect = False
        if relative in {
            "docs/artigo_final/avaliacao_usuarios/scripts/gerar_tabelas.py",
            "docs/artigo_final/avaliacao_usuarios/resultados/tabela_temas.tex",
        }:
            old = git("show", f"{BASELINE}:{relative}")
            assert old.replace(
                "para validação do autor", "conferida pelo autor"
            ) == (ROOT / relative).read_text()
            protect = False
        if protect:
            assert git("show", f"{BASELINE}:{relative}", binary=True) == (
                ROOT / relative
            ).read_bytes(), f"Arquivo protegido alterado: {relative}"
            protected.append(relative)
    equation_pattern = r"\\begin\{(?:equation|align)\}.*?\\end\{(?:equation|align)\}"
    equations = {}
    for name in (
        "final_2_fundamentacao.tex", "final_3_metodos.tex",
        "final_3a_implementacao.tex",
    ):
        old = git("show", f"{BASELINE}:docs/artigo_final/{name}")
        new = (ARTICLE / name).read_text()
        a = re.findall(equation_pattern, old, re.S)
        b = re.findall(equation_pattern, new, re.S)
        assert a == b, f"Equações alteradas: {name}"
        equations[name] = len(b)
    source = next((ROOT / "docs").glob("Respostas*.xlsx"))
    original = ARTICLE / "avaliacao_usuarios/dados_originais/respostas_recebidas.xlsx"
    assert digest(source) == "9adb66b330103ca858c37d7dc6cdb5e4e954f09f749a0c122fa6e6b2f4f5de59"
    assert digest(original) == "d61b9f11514f8d42f276abdb3e4e173782955c468fb50d774680032d342ce48a"
    import openpyxl

    a = list(openpyxl.load_workbook(original, data_only=True).worksheets[0].values)
    b = list(openpyxl.load_workbook(source, data_only=True).worksheets[0].values)
    assert len(a) == len(b) == 32
    assert all(x[1:] == y[1:] for x, y in zip(a, b))
    assert sum(x[0] != y[0] for x, y in zip(a[1:], b[1:])) == 7
    assert sum(bool(str(row[i] or "").strip()) for row in b[1:] for i in range(43, 48)) == 142
    codes = json.loads((ARTICLE / "avaliacao_usuarios/codificacao.json").read_text())
    assert len(codes["temas"]) == 13 and len(codes["registros"]) == 31
    assert sum(len(record["codigos"]) for record in codes["registros"]) == 142
    fixture_texts = ("Comentário sintético", "Texto sintético apenas para teste")
    assert not any(
        str(cell or "").strip() in fixture_texts
        for row in b[1:] for cell in row
    )
    screen = ROOT / "Imagens Artigo/Imagem3.1-Relatório gerado em pdf.png"
    excluded = ARTICLE / "evidencias/capturas_autor/relatorio_pdf_pendente.png"
    same_capture = digest(screen) == digest(excluded)
    # O manifesto registra a disponibilidade observada, sem presumir mudança.
    entries = re.findall(r"@\w+\{([^,]+),", (ARTICLE / "referencias.bib").read_text())
    old_entries = re.findall(
        r"@\w+\{([^,]+),",
        git("show", f"{BASELINE}:docs/artigo_final/referencias.bib"),
    )
    assert all(n == 1 for n in Counter(entries).values())
    added = sorted(set(entries) - set(old_entries))
    removed = sorted(set(old_entries) - set(entries))
    assert len(added) == 8 and not removed
    current_pa = (ARTICLE / "auditoria_cientifica/PENDENCIAS_AUTOR.md").read_text().split(
        "## Histórico anterior"
    )[0]
    assert len(re.findall(r"^\| PA\d\d \|", current_pa, re.M)) == 18
    changed = git("diff", BASELINE, "--name-only").splitlines()
    assert all(p.startswith("docs/artigo_final/") for p in changed)
    diffs = [git("diff", "--no-ext-diff", BASELINE, "--", "docs/artigo_final")]
    for relative in git("ls-files", "--others", "--exclude-standard", "docs/artigo_final").splitlines():
        path = ROOT / relative
        if path.suffix in {".tex", ".md", ".py"} and "evidencias/revisao_final_pa" not in relative:
            diffs.append("".join(difflib.unified_diff(
                [], path.read_text().splitlines(True), fromfile="/dev/null", tofile=relative
            )))
    (OUT / "comparacao.diff").write_text("\n".join(diffs))
    compilation = json.loads((OUT / "compilacao.json").read_text())
    assert compilation["passed"] and not compilation["undefined"]
    assert digest(args.build_dir / "Relatorio_Final.pdf") == compilation["pdf_sha256"]
    result = {
        "baseline": before,
        "mechanical_checks_passed": True,
        "scientific_acceptance_complete": False,
        "human_approval_of_current_revision": False,
        "protected_tracked_files_unchanged": len(protected),
        "equation_environments_unchanged": equations,
        "responses_unchanged": True,
        "source_sha256": digest(source),
        "original_sha256": digest(original),
        "historical_timestamp_differences": 7,
        "new_timestamp_changes": 0,
        "records": 31,
        "nonempty_discursive_cells": 142,
        "themes": 13,
        "known_synthetic_fixtures_found": 0,
        "independent_empirical_authentication": False,
        "pdf_capture_same_as_previously_excluded": same_capture,
        "pdf_capture_sha256": digest(screen),
        "pdf_capture_incorporated": False,
        "bibliography": {"entries": len(entries), "added": added, "removed": removed},
        "pa_items_documented": 18,
        "pdf_sha256": compilation["pdf_sha256"],
        "artifact_hashes": {
            name: digest(ARTICLE / name)
            for name in (
                "Relatorio_Final.pdf", "DECLARACAO_USO_IA.pdf",
                "DECLARACAO_USO_IA.tex", "referencias.bib", "REGISTRO_USO_IA.md",
            )
        },
        "no_new_application_tests_or_deployment_claimed": True,
        "remaining": [
            "independent source/export and closure of questionnaire",
            "exact public commit", "ethics and formal AI authorization",
            "primary-source verification", "spectral figure reconstruction",
            "updated report screenshot", "human final review and signature",
        ],
    }
    if args.cache_dir:
        cache = args.cache_dir
        result["source_cache_hashes"] = {
            name: digest(cache / name)
            for name in (
                "IN_03_2026_PROACAD.pdf", "CNS_510_2016.pdf", "izquierdo2026.pdf",
                "meroni2019.html", "parnas1972.pdf", "sdd.md",
                "nist-location.html", "boeckeler2025.html", "eosda-guide.html",
                "eosda-pricing.html", "onesoil-platform.html", "formulario.html",
            ) if (cache / name).exists()
        }
        result["new_http_accesses"] = json.loads((cache / "novos-acessos.json").read_text())
        if (cache / "conferencia-planilha.json").exists():
            (OUT / "conferencia-planilha.json").write_bytes(
                (cache / "conferencia-planilha.json").read_bytes()
            )
    (OUT / "validacao.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
