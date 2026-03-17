from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache



class Settings(BaseSettings):
    # App metadata
    PROJECT_NAME: str = "ATM Management"
    VERSION: str = "1.0"

    # Environment
    ENV: str = "development"

    # Database
    DATABASE_URL: str

    # Debug
    DEBUG: bool = False

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()