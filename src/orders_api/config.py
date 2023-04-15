from functools import lru_cache
from os import getenv

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    database_url: PostgresDsn


@lru_cache
def get_settings() -> Settings:
    settings = Settings()  # type: ignore
    if (db := getenv("POSTGRES_DB")) is not None:
        settings.database_url = PostgresDsn.build(
            scheme="postgresql",
            user=settings.database_url.user,
            password=settings.database_url.password,
            host=settings.database_url.host,
            port=settings.database_url.port,
            path=f"/{db}",
        )
    return settings
