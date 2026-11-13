import ee

from src.app.config import EE_PROJECT_ID


def initialize_earth_engine(project_id=EE_PROJECT_ID, ee_client=ee):
    if not project_id:
        raise ValueError("EE_PROJECT_ID must be configured before initializing Earth Engine.")

    ee_client.Authenticate()
    ee_client.Initialize(project=project_id)
