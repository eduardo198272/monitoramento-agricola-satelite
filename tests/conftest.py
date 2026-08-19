import sys
from unittest.mock import MagicMock

mock_ee = MagicMock()
sys.modules['ee'] = mock_ee