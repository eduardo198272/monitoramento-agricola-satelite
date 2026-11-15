"""Retificação autorizada pelo autor: dias 16/17 de novembro de 2026 para 15."""

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import shutil

import openpyxl


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def correct(source, backup, audit):
    if backup.exists():
        raise ValueError("O backup não pode ser sobrescrito.")
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, backup)
    before_hash = sha256(source)
    workbook = openpyxl.load_workbook(source)
    sheet = workbook["Respostas ao formulário 1"]
    if sheet.cell(1, 1).value != "Carimbo de data/hora":
        raise ValueError("Coluna de carimbo não reconhecida.")
    before = [[cell.value for cell in row] for row in sheet.iter_rows()]
    changes = []
    for row in sheet.iter_rows(min_row=2):
        cell = row[0]
        value = cell.value
        if isinstance(value, datetime) and value.date().isoformat() in {
            "2026-11-16", "2026-11-17"
        }:
            corrected = value.replace(day=15)
            changes.append({"excel_row": cell.row, "before": value.isoformat(),
                            "after": corrected.isoformat()})
            cell.value = corrected
    if not changes:
        raise ValueError("Nenhum carimbo correspondente encontrado; arquivo não regravado.")
    workbook.save(source)
    checked = openpyxl.load_workbook(source, read_only=True)
    after = [[cell.value for cell in row]
             for row in checked["Respostas ao formulário 1"].iter_rows()]
    changed_rows = {change["excel_row"] for change in changes}
    for number, (old, new) in enumerate(zip(before, after), 1):
        assert old[1:] == new[1:], "Uma resposta foi alterada."
        if number not in changed_rows:
            assert old[0] == new[0]
        else:
            assert old[0].replace(day=15) == new[0]
    assert len(before) == len(after)
    assert workbook.sheetnames == checked.sheetnames
    audit.parent.mkdir(parents=True, exist_ok=True)
    audit.write_text(json.dumps({
        "authorization": "Autor informou erro de digitação nos dias 16 e 17; "
                         "solicitou retificação para dia 15, mantendo horários.",
        "original_sha256": before_hash,
        "corrected_sha256": sha256(source),
        "changed_cells": len(changes),
        "answers_unchanged": True,
        "changes_private": changes,
    }, ensure_ascii=False, indent=2) + "\n")
    return {"changed_cells": len(changes), "original_sha256": before_hash,
            "corrected_sha256": sha256(source), "answers_unchanged": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--backup", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--aplicar", action="store_true", required=True)
    args = parser.parse_args()
    print(json.dumps(correct(args.input, args.backup, args.audit), indent=2))


if __name__ == "__main__":
    main()
