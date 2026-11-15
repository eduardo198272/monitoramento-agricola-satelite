import os
from pathlib import Path
import runpy
import sys
from unittest.mock import MagicMock

import pytest
import streamlit
from streamlit.errors import StreamlitSecretNotFoundError


@pytest.mark.parametrize("with_secrets", [True, False])
def test_cloud_entrypoint_forces_session_storage_and_noninteractive_auth(
    monkeypatch, with_secrets
):
    import src.app.main as app

    run_app = MagicMock()
    monkeypatch.setattr(app, "main", run_app)
    # Track environment changes made inside the entrypoint for automatic cleanup.
    for key in ("SAVED_LOCATIONS_STORAGE", "EE_AUTH_MODE", "EE_PROJECT_ID", "EE_SERVICE_ACCOUNT_JSON"):
        monkeypatch.setenv(key, "before")
    if with_secrets:
        monkeypatch.setattr(streamlit, "secrets", {
            "EE_PROJECT_ID": "cloud-project", "EE_SERVICE_ACCOUNT_JSON": "test-json"
        })
    else:
        class MissingSecrets:
            def __contains__(self, key):
                raise StreamlitSecretNotFoundError("No secrets configured")

        monkeypatch.setattr(streamlit, "secrets", MissingSecrets())
    root = Path(__file__).resolve().parents[1]
    monkeypatch.setattr(sys, "path", [item for item in sys.path if item != str(root)])
    runpy.run_path(str(root / "streamlit_app.py"), run_name="__main__")
    run_app.assert_called_once_with()
    assert os.environ["SAVED_LOCATIONS_STORAGE"] == "session"
    assert os.environ["EE_AUTH_MODE"] == "service_account"
    assert os.environ["EE_PROJECT_ID"] == ("cloud-project" if with_secrets else "before")
    assert str(root) in sys.path


def test_importing_cloud_entrypoint_does_not_start_app(monkeypatch):
    import src.app.main as app

    run_app = MagicMock()
    monkeypatch.setattr(app, "main", run_app)
    root = Path(__file__).resolve().parents[1]
    namespace = runpy.run_path(str(root / "streamlit_app.py"))
    assert "main" in namespace
    run_app.assert_not_called()


def test_cloud_ui_download_and_separate_visitors(monkeypatch):
    from streamlit.testing.v1 import AppTest
    import src.app.main as app
    from src.app.saved_locations_service import _build_record
    from src.app.saved_locations_validation import prepare_saved_location

    for key in ("SAVED_LOCATIONS_STORAGE", "EE_AUTH_MODE"):
        monkeypatch.setenv(key, "before")
    monkeypatch.setattr(streamlit, "secrets", {})
    # Real Streamlit widgets and session contexts; only the remote EE boundary
    # is replaced, so the test requires no Google account or network access.
    monkeypatch.setattr(app, "init_earth_engine", lambda: (True, None))
    root = Path(__file__).resolve().parents[1]
    first = AppTest.from_file(str(root / "streamlit_app.py")).run(timeout=30)
    assert not first.exception
    polygon = {
        "type": "Polygon",
        "coordinates": [[[-45, -20], [-44, -20], [-44, -19], [-45, -20]]],
    }
    record = _build_record(prepare_saved_location("Área privada", polygon))
    first.session_state["_saved_location_records"] = {record["id"]: record}
    next(
        button for button in first.sidebar.button
        if button.label == "Preparar GeoJSON para download"
    ).click().run()
    assert not first.exception
    assert len(first.get("download_button")) == 1

    second = AppTest.from_file(str(root / "streamlit_app.py")).run(timeout=30)
    next(
        button for button in second.sidebar.button
        if button.label == "Preparar GeoJSON para download"
    ).click().run()
    assert not second.exception
    assert second.session_state["_saved_location_records"] == {}
    assert len(second.get("download_button")) == 0
    assert second.sidebar.error
