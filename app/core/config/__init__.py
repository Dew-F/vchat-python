from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    database_url: str
    debug: bool = False
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")


settings = Settings()
