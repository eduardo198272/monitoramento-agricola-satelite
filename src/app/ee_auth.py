import json
import os

import ee

from src.app.config import EE_PROJECT_ID


def initialize_earth_engine(project_id=EE_PROJECT_ID, ee_client=ee):
    if not project_id:
        raise ValueError("EE_PROJECT_ID must be configured before initializing Earth Engine.")

    service_account_json = os.getenv("EE_SERVICE_ACCOUNT_JSON")
    if service_account_json:
        try:
            account = json.loads(service_account_json)
            if (
                not isinstance(account, dict)
                or account.get("type") != "service_account"
                or not all(
                    isinstance(account.get(key), str) and account[key].strip()
                    for key in ("client_email", "private_key")
                )
            ):
                raise ValueError("Invalid service account")
        except (ValueError, RecursionError):
            raise ValueError("EE_SERVICE_ACCOUNT_JSON must contain a valid service account.") from None
        credentials = ee_client.ServiceAccountCredentials(
            account["client_email"], key_data=json.dumps(account)
        )
        ee_client.Initialize(credentials=credentials, project=project_id)
    elif os.getenv("EE_AUTH_MODE", "interactive") == "interactive":
        ee_client.Authenticate()
        ee_client.Initialize(project=project_id)
    else:
        raise ValueError("Configure EE_SERVICE_ACCOUNT_JSON for non-interactive authentication.")
