from datetime import date, datetime


def normalize_date(value: str | date) -> str:
    """Return an ISO ``YYYY-MM-DD`` date from a string or date object."""
    if isinstance(value, datetime):
        value = value.date()
    if isinstance(value, date):
        return value.isoformat()
    if not isinstance(value, str):
        raise ValueError(
            f"Data inválida: {value}. Use formato YYYY-MM-DD ou datetime.date"
        )

    try:
        parsed_date = date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(
            f"Data inválida: {value}. Use formato YYYY-MM-DD"
        ) from error

    if parsed_date.isoformat() != value:
        raise ValueError(f"Data inválida: {value}. Use formato YYYY-MM-DD")
    return parsed_date.isoformat()
