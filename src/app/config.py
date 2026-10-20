import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Sistema de Monitoramento Agricola"
VERSION = "0.1.0"

EE_PROJECT_ID = os.getenv("EE_PROJECT_ID")


def resolve_saved_locations_db_path(
    environ: dict[str, str] | None = None,
    *,
    home: Path | None = None,
    platform: str | None = None,
) -> Path:
    """Resolve the persistent SQLite path without creating files or directories."""
    environ = os.environ if environ is None else environ
    configured_path = environ.get("SAVED_LOCATIONS_DB_PATH")
    if configured_path:
        return Path(configured_path).expanduser()

    home = Path.home() if home is None else Path(home)
    platform = os.name if platform is None else platform
    if platform == "nt":
        data_root = Path(environ.get("LOCALAPPDATA", home / "AppData" / "Local"))
    elif environ.get("XDG_DATA_HOME"):
        data_root = Path(environ["XDG_DATA_HOME"]).expanduser()
    else:
        data_root = home / ".local" / "share"

    return data_root / "monitoramento-agricola-satelite" / "saved_locations.sqlite3"


SAVED_LOCATIONS_DB_PATH = resolve_saved_locations_db_path()
