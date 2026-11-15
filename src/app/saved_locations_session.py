"""Repository backed only by one visitor's Streamlit session state."""

from copy import deepcopy

from src.app.saved_locations_repository import SavedLocationConflictError
from src.app.locations_geojson import export_locations_geojson


class SessionLocationsRepository:
    """Use an explicitly supplied mapping; never share records globally."""

    def __init__(self, records: dict):
        self.records = records

    def initialize(self) -> None:
        pass

    def insert_location(self, record: dict) -> None:
        self.insert_locations([record])

    def insert_locations(self, records: list[dict]) -> None:
        names = {record["normalized_name"] for record in self.records.values()}
        ids = set(self.records)
        pending = {}
        for record in records:
            if record["normalized_name"] in names or record["id"] in ids:
                raise SavedLocationConflictError("Já existe uma localização com esse nome.")
            names.add(record["normalized_name"])
            ids.add(record["id"])
            pending[record["id"]] = deepcopy(record)
        # Every accepted session must remain downloadable as one valid file.
        export_locations_geojson([*self.records.values(), *pending.values()])
        self.records.update(pending)

    def list_locations(self) -> list[dict]:
        records = sorted(
            self.records.values(), key=lambda record: (record["normalized_name"], record["id"])
        )
        return [self._public_record(record, full=False) for record in records]

    def get_location(self, location_id: str) -> dict | None:
        record = self.records.get(location_id)
        return None if record is None else self._public_record(record, full=True)

    def delete_location(self, location_id: str) -> bool:
        return self.records.pop(location_id, None) is not None

    @staticmethod
    def _public_record(record: dict, *, full: bool) -> dict:
        result = {
            key: record[key] for key in ("id", "name", "created_at", "updated_at")
        }
        result["center"] = {"lat": record["center_lat"], "lon": record["center_lon"]}
        if full:
            result["geojson"] = record["geojson"]
            result["normalized_name"] = record["normalized_name"]
        return deepcopy(result)
