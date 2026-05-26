from unittest.mock import Mock

import pytest

from src.app.ee_auth import initialize_earth_engine


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
