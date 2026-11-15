"""Cloud entrypoint: isolated sessions and non-interactive Earth Engine auth."""

import os
from pathlib import Path
import sys

import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError


def main():
    # Also work when invoked through the Streamlit executable, not python -m.
    root = str(Path(__file__).resolve().parent)
    if root not in sys.path:
        sys.path.insert(0, root)

    # This entrypoint must never expose the machine's SQLite records to visitors.
    os.environ["SAVED_LOCATIONS_STORAGE"] = "session"
    os.environ["EE_AUTH_MODE"] = "service_account"
    try:
        for key in ("EE_PROJECT_ID", "EE_SERVICE_ACCOUNT_JSON"):
            if key in st.secrets:
                os.environ[key] = st.secrets[key]
    except StreamlitSecretNotFoundError:
        # The app will show the normal unavailable-service state without
        # attempting an interactive authentication flow on the cloud server.
        pass

    from src.app.main import main as run_app

    run_app()


if __name__ == "__main__":
    main()
