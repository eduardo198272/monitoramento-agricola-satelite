import importlib
import re
from pathlib import Path


REQUIREMENTS_PATH = Path(__file__).resolve().parents[1] / "requirements.txt"
EXPORT_DEPENDENCIES = {
    "reportlab": "reportlab",
    "openpyxl": "openpyxl",
    "Pillow": "PIL",
    "matplotlib": "matplotlib",
}


def _requirements_by_name():
    requirements = {}
    for line in REQUIREMENTS_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, separator, version = line.partition("==")
        if separator:
            requirements[name.lower()] = version
    return requirements


def test_export_rendering_dependencies_are_pinned():
    requirements = _requirements_by_name()

    for distribution in EXPORT_DEPENDENCIES:
        version = requirements.get(distribution.lower())
        assert version, f"{distribution} deve estar fixado em requirements.txt"
        assert re.fullmatch(r"\d+(?:\.\d+)+(?:[a-zA-Z0-9.+-]*)?", version)


def test_export_rendering_dependencies_are_importable():
    for distribution, module in EXPORT_DEPENDENCIES.items():
        assert _requirements_by_name().get(distribution.lower()), (
            f"{distribution} deve estar declarado em requirements.txt"
        )
        try:
            importlib.import_module(module)
        except ImportError as error:
            raise AssertionError(
                f"{distribution} ({module}) não está importável no ambiente de teste"
            ) from error
