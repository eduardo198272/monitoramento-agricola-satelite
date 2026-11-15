"""Descriptive analysis of an explicitly mapped survey; no network operations."""

import argparse
import csv
import json
from pathlib import Path
import numpy as np


def analyze(rows, config):
    """Use valid denominators per question; never infer the questionnaire scale."""
    consent = config["consent_column"]
    eligible = [row for row in rows if row.get(consent) == config["consent_value"]]
    summaries, open_answers = {}, []
    for column, definition in config["questions"].items():
        kind = definition["type"]
        if kind not in {"categorical", "multiple", "ordinal", "open"}:
            raise ValueError("Tipo de questão não reconhecido")
        counts, missing, not_applicable, unable, invalid = {}, 0, 0, 0, 0
        numeric = []
        valid = 0
        for participant, row in enumerate(eligible, 1):
            answer = (row.get(column) or "").strip()
            if not answer:
                missing += 1
                continue
            if answer in definition.get("not_applicable", ["Não se aplica"]):
                not_applicable += 1
                continue
            if answer in definition.get("unable", ["Não consegui avaliar"]):
                unable += 1
                continue
            if kind == "open":
                open_answers.append({"participant": f"P{participant:03d}",
                                     "question": column, "text_for_manual_anonymization": answer,
                                     "code": "", "theme": ""})
            else:
                options = answer.split(definition["separator"]) if kind == "multiple" else [answer]
                options = list(dict.fromkeys(option.strip() for option in options))
                allowed = definition.get("values")
                if allowed is not None and any(option not in allowed for option in options):
                    invalid += 1
                    continue
                for option in options:
                    counts[option] = counts.get(option, 0) + 1
                if kind == "ordinal":
                    numeric.append(float(definition["values"][answer]))
            valid += 1
        result = {
            "eligible": len(eligible), "valid": valid, "missing": missing,
            "not_applicable": not_applicable, "unable": unable, "invalid": invalid,
            "frequencies": {
                answer: {"absolute": count, "relative_valid": count / valid}
                for answer, count in counts.items()
            },
        }
        if numeric:
            result["median"] = float(np.median(numeric))
            result["q1"], result["q3"] = map(float, np.percentile(numeric, [25, 75]))
            result["iqr"] = result["q3"] - result["q1"]
        summaries[column] = result
    return {"received": len(rows), "eligible": len(eligible),
            "excluded_by_consent": len(rows) - len(eligible), "questions": summaries}, open_answers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--natureza", choices=["reais", "sinteticos"], required=True)
    args = parser.parse_args()
    if args.natureza == "sinteticos" and "artigo_final" in args.output.parts:
        parser.error("Resultados sintéticos devem ficar fora dos entregáveis acadêmicos")
    text = args.input.read_text(encoding="utf-8-sig")
    dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;\t")
    rows = list(csv.DictReader(text.splitlines(), dialect=dialect))
    config = json.loads(args.config.read_text(encoding="utf-8"))
    if not config["questions"]:
        parser.error("Mapeie o instrumento real antes da análise")
    result, open_answers = analyze(rows, config)
    result["natureza"] = args.natureza
    result["sampling"] = "Não probabilística; não realizar inferência populacional"
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "resumo.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    # Private working material: manually anonymize before publishing any quotation.
    (args.output / "abertas_PARA_ANONIMIZAR.json").write_text(
        json.dumps(open_answers, ensure_ascii=False, indent=2)
    )


if __name__ == "__main__":
    main()
