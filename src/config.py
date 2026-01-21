from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/railways_db"
    ECHO_SQL: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
