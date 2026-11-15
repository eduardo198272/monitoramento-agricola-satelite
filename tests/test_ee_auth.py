import json
from unittest.mock import Mock

import pytest

from src.app.ee_auth import initialize_earth_engine


@pytest.fixture(autouse=True)
def isolated_auth_environment(monkeypatch):
    monkeypatch.delenv("EE_SERVICE_ACCOUNT_JSON", raising=False)
    monkeypatch.delenv("EE_AUTH_MODE", raising=False)


def test_initialize_earth_engine_authenticates_and_uses_project_id():
    ee_client = Mock()

    initialize_earth_engine("test-project", ee_client=ee_client)

    ee_client.Authenticate.assert_called_once_with()
    ee_client.Initialize.assert_called_once_with(project="test-project")


def test_initialize_earth_engine_requires_project_id():
    ee_client = Mock()

    with pytest.raises(ValueError, match="EE_PROJECT_ID"):
        initialize_earth_engine(None, ee_client=ee_client)

    ee_client.Authenticate.assert_not_called()
    ee_client.Initialize.assert_not_called()


def test_service_account_never_authenticates_interactively(monkeypatch):
    ee_client = Mock()
    account = {
        "type": "service_account",
        "client_email": "example@example.iam.gserviceaccount.com",
        "private_key": "test-only",
    }
    monkeypatch.setenv("EE_SERVICE_ACCOUNT_JSON", json.dumps(account))
    initialize_earth_engine("project", ee_client=ee_client)
    ee_client.Authenticate.assert_not_called()
    ee_client.ServiceAccountCredentials.assert_called_once_with(
        account["client_email"], key_data=json.dumps(account)
    )
    ee_client.Initialize.assert_called_once_with(
        credentials=ee_client.ServiceAccountCredentials.return_value, project="project"
    )


@pytest.mark.parametrize("payload", [
    "invalid-secret-value", "[]", "{}", "[" * 2000,
    '{"type":"service_account","client_email":1,"private_key":"key"}',
    '{"type":"service_account","client_email":"x","private_key":""}',
])
def test_invalid_credentials_do_not_leak_secret_or_open_auth(monkeypatch, payload):
    ee_client = Mock()
    monkeypatch.setenv("EE_SERVICE_ACCOUNT_JSON", payload)
    with pytest.raises(ValueError, match="EE_SERVICE_ACCOUNT_JSON") as error:
        initialize_earth_engine("project", ee_client=ee_client)
    assert payload not in str(error.value)
    ee_client.Authenticate.assert_not_called()
    ee_client.Initialize.assert_not_called()


def test_cloud_without_credentials_fails_without_prompt(monkeypatch):
    ee_client = Mock()
    monkeypatch.setenv("EE_AUTH_MODE", "service_account")
    with pytest.raises(ValueError, match="Configure EE_SERVICE_ACCOUNT_JSON"):
        initialize_earth_engine("project", ee_client=ee_client)
    ee_client.Authenticate.assert_not_called()
