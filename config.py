from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    github_base_url: str = "https://api.github.com"


@lru_cache()
def get_settings():
    return Settings()
