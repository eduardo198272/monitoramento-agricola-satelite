"""SQLite persistence for saved geographic locations."""

from contextlib import contextmanager
import json
import os
from pathlib import Path
import sqlite3
from typing import Iterator

from src.app.config import SAVED_LOCATIONS_DB_PATH

SCHEMA_VERSION = 1
IS_WINDOWS = os.name == "nt"


class SavedLocationStorageError(RuntimeError):
    """Storage could not be initialized or accessed safely."""


class SavedLocationConflictError(SavedLocationStorageError):
    """A saved-location uniqueness constraint was violated."""


class SavedLocationsRepository:
    """Persist location records in a local SQLite database.

    ``insert_location`` expects already validated and normalized values. Domain
    validation and mapping these records to UI-facing objects belong to the
    service layer.
    """

    def __init__(self, database_path: str | os.PathLike | None = None):
        self.database_path = Path(database_path or SAVED_LOCATIONS_DB_PATH).expanduser()

    def _ensure_parent_directory(self) -> None:
        parent = self.database_path.parent
        try:
            parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            if not IS_WINDOWS:
                # Tighten only the application-owned directory, not arbitrary
                # ancestors or a caller-provided parent directory.
                app_directory = parent
                while app_directory.name != "monitoramento-agricola-satelite":
                    if app_directory.parent == app_directory:
                        app_directory = None
                        break
                    app_directory = app_directory.parent
                if app_directory is not None:
                    app_directory.chmod(0o700)
        except OSError as error:
            raise SavedLocationStorageError("Não foi possível preparar o armazenamento.") from error

    @contextmanager
    def _connection(self) -> Iterator[sqlite3.Connection]:
        self._ensure_parent_directory()
        connection = None
        try:
            connection = sqlite3.connect(self.database_path, timeout=5.0)
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA foreign_keys = ON")
            yield connection
            connection.commit()
        except sqlite3.IntegrityError as error:
            if connection is not None:
                connection.rollback()
            raise SavedLocationConflictError(
                "Já existe uma localização com esses dados únicos."
            ) from error
        except (sqlite3.Error, OSError) as error:
            if connection is not None:
                connection.rollback()
            raise SavedLocationStorageError(
                "Não foi possível acessar o armazenamento de localizações."
            ) from error
        finally:
            if connection is not None:
                connection.close()

    def initialize(self) -> None:
        """Create the initial schema once and reject unsupported future schemas."""
        with self._connection() as connection:
            current_version = connection.execute("PRAGMA user_version").fetchone()[0]
            if current_version > SCHEMA_VERSION:
                raise SavedLocationStorageError(
                    "A versão do banco de localizações não é compatível."
                )
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS saved_locations (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL CHECK(length(name) BETWEEN 1 AND 100),
                    normalized_name TEXT NOT NULL UNIQUE,
                    geojson_json TEXT NOT NULL,
                    center_lat REAL NOT NULL,
                    center_lon REAL NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )
            if current_version < SCHEMA_VERSION:
                connection.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")

    def insert_location(self, record: dict) -> None:
        """Insert one prevalidated record; JSON is stored without key sorting."""
        try:
            geojson_json = json.dumps(record["geojson"], ensure_ascii=False)
            with self._connection() as connection:
                connection.execute(
                    """
                    INSERT INTO saved_locations (
                        id, name, normalized_name, geojson_json,
                        center_lat, center_lon, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        record["id"],
                        record["name"],
                        record["normalized_name"],
                        geojson_json,
                        record["center_lat"],
                        record["center_lon"],
                        record["created_at"],
                        record["updated_at"],
                    ),
                )
        except SavedLocationStorageError:
            raise
        except (KeyError, TypeError, ValueError) as error:
            raise SavedLocationStorageError(
                "O registro da localização não possui os campos necessários."
            ) from error

    def list_locations(self) -> list[dict]:
        """Return summary records in normalized-name then ID order."""
        with self._connection() as connection:
            rows = connection.execute(
                """
                SELECT id, name, center_lat, center_lon, created_at, updated_at
                FROM saved_locations
                ORDER BY normalized_name, id
                """
            ).fetchall()
        return [self._map_row(row) for row in rows]

    def get_location(self, location_id: str) -> dict | None:
        """Return the full stored record, or ``None`` when it is absent."""
        with self._connection() as connection:
            row = connection.execute(
                """
                SELECT id, name, normalized_name, geojson_json,
                       center_lat, center_lon, created_at, updated_at
                FROM saved_locations WHERE id = ?
                """,
                (location_id,),
            ).fetchone()
        if row is None:
            return None
        result = self._map_row(row)
        result["normalized_name"] = row["normalized_name"]
        try:
            result["geojson"] = json.loads(row["geojson_json"])
        except (json.JSONDecodeError, TypeError) as error:
            raise SavedLocationStorageError(
                "O registro de localização armazenado está corrompido."
            ) from error
        return result

    def delete_location(self, location_id: str) -> bool:
        """Delete a record and report whether it existed."""
        with self._connection() as connection:
            cursor = connection.execute(
                "DELETE FROM saved_locations WHERE id = ?", (location_id,)
            )
            return cursor.rowcount > 0

    @staticmethod
    def _map_row(row: sqlite3.Row) -> dict:
        return {
            "id": row["id"],
            "name": row["name"],
            "center": {"lat": row["center_lat"], "lon": row["center_lon"]},
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }
