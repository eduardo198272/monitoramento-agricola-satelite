"""Domain operations for saved geographic locations."""

from datetime import datetime, timezone
import uuid
from src.app.saved_locations_repository import (
    SavedLocationConflictError,
    SavedLocationsRepository,
)
from src.app.saved_locations_validation import prepare_saved_location


class SavedLocationDuplicateError(ValueError):
    """A location with the same normalized name already exists."""


class SavedLocationServiceError(RuntimeError):
    """A saved-location service operation could not be completed."""


class SavedLocationsService:
    """Validate and orchestrate location operations through a repository."""

    def __init__(self, repository: SavedLocationsRepository | None = None):
        self.repository = repository or SavedLocationsRepository()

    def save_location(self, name: str, geojson: dict) -> dict:
        """Validate and persist a location, returning its complete record."""
        prepared = prepare_saved_location(name, geojson)
        center = _bounding_box_center(prepared["geojson"])
        now = datetime.now(timezone.utc).isoformat()
        record = {
            **prepared,
            "id": str(uuid.uuid4()),
            "center_lat": center["lat"],
            "center_lon": center["lon"],
            "created_at": now,
            "updated_at": now,
        }

        self.repository.initialize()
        try:
            self.repository.insert_location(record)
        except SavedLocationConflictError as error:
            raise SavedLocationDuplicateError(
                "Já existe uma localização salva com esse nome."
            ) from error

        saved_location = self.repository.get_location(record["id"])
        if saved_location is None:
            raise SavedLocationServiceError(
                "A localização foi gravada, mas não pôde ser recuperada."
            )
        # The repository's complete read includes normalized_name, which is an
        # internal comparison key and not part of the public service contract.
        saved_location.pop("normalized_name", None)
        return saved_location

    def list_saved_locations(self) -> list[dict]:
        """Return repository summaries in their deterministic order."""
        self.repository.initialize()
        return self.repository.list_locations()

    def get_saved_location(self, location_id: str) -> dict | None:
        """Return one complete location, or ``None`` for an unknown ID."""
        self.repository.initialize()
        result = self.repository.get_location(location_id)
        if result is not None:
            result.pop("normalized_name", None)
        return result

    def delete_saved_location(self, location_id: str) -> bool:
        """Delete one location and return whether it existed."""
        self.repository.initialize()
        return self.repository.delete_location(location_id)


def _bounding_box_center(geojson: dict) -> dict[str, float]:
    """Calculate the WGS84 coordinate midpoint of all polygon positions."""
    geometry = geojson["geometry"] if geojson.get("type") == "Feature" else geojson
    positions = [position for ring in geometry["coordinates"] for position in ring]
    longitudes = [position[0] for position in positions]
    latitudes = [position[1] for position in positions]
    return {
        "lat": (min(latitudes) + max(latitudes)) / 2,
        "lon": (min(longitudes) + max(longitudes)) / 2,
    }
