from src.app.config import resolve_saved_locations_db_path


def test_configured_saved_locations_path_is_used_without_side_effects(tmp_path):
    database_path = tmp_path / "private" / "locations.sqlite3"

    resolved = resolve_saved_locations_db_path(
        {"SAVED_LOCATIONS_DB_PATH": str(database_path)}, home=tmp_path, platform="nt"
    )

    assert resolved == database_path
    assert not database_path.parent.exists()


def test_windows_default_uses_local_app_data(tmp_path):
    resolved = resolve_saved_locations_db_path(
        {"LOCALAPPDATA": str(tmp_path / "LocalAppData")},
        home=tmp_path,
        platform="nt",
    )

    assert resolved == (
        tmp_path / "LocalAppData" / "monitoramento-agricola-satelite"
        / "saved_locations.sqlite3"
    )


def test_xdg_default_uses_user_data_directory(tmp_path):
    data_home = tmp_path / "xdg-data"

    resolved = resolve_saved_locations_db_path(
        {"XDG_DATA_HOME": str(data_home)}, home=tmp_path, platform="posix"
    )

    assert resolved == (
        data_home / "monitoramento-agricola-satelite" / "saved_locations.sqlite3"
    )


def test_posix_fallback_is_outside_temporary_directory(tmp_path):
    resolved = resolve_saved_locations_db_path({}, home=tmp_path, platform="posix")

    assert resolved == (
        tmp_path / ".local" / "share" / "monitoramento-agricola-satelite"
        / "saved_locations.sqlite3"
    )
    assert not resolved.parent.exists()
