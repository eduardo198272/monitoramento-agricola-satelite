import importlib
import os
from unittest.mock import patch

from src.app import config


def test_application_metadata_is_defined():
    assert config.APP_NAME == "Sistema de Monitoramento Agricola"
    assert config.VERSION == "0.1.0"


def test_project_id_comes_from_environment():
    with patch.dict(os.environ, {"EE_PROJECT_ID": "test-project"}):
        refreshed_config = importlib.reload(config)

    assert refreshed_config.EE_PROJECT_ID == "test-project"
    importlib.reload(config)
