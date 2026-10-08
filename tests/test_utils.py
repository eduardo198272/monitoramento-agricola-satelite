from datetime import date, datetime

import pytest

from src.app.utils import normalize_date


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-02-29", "2024-02-29"),
        (date(2024, 2, 29), "2024-02-29"),
        (datetime(2024, 2, 29, 23, 59), "2024-02-29"),
    ],
)
def test_normalize_date_accepts_iso_string_and_date_objects(value, expected):
    assert normalize_date(value) == expected


@pytest.mark.parametrize("value", ["2024/02/29", "20240229", "2023-02-29"])
def test_normalize_date_rejects_non_iso_or_invalid_dates(value):
    with pytest.raises(ValueError, match="Use formato YYYY-MM-DD"):
        normalize_date(value)


def test_normalize_date_rejects_unsupported_types():
    with pytest.raises(ValueError, match="datetime.date"):
        normalize_date(20240229)
