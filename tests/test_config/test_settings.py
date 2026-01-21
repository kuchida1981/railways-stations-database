from src.config import settings


def test_settings_load() -> None:
    assert settings.DATABASE_URL
    assert isinstance(settings.ECHO_SQL, bool)
