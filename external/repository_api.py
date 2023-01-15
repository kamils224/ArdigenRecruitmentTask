import re
from abc import abstractmethod, ABC

import httpx
from fastapi import HTTPException
from httpx import Response

from config import get_settings
from schemas import Repository


class BaseRepositoryApi(ABC):

    def __init__(self):
        self.async_client = httpx.AsyncClient()

    @abstractmethod
    async def get_user_repositories(self, username: str, page: int = 1, per_page: int = 10) -> list[Repository]:
        raise NotImplementedError


class GithubApi(BaseRepositoryApi):
    BASE_URL = get_settings().github_base_url

    async def get_user_repositories(self, username: str, page: int = 1, per_page: int = 10) -> list[Repository]:
        url = f"{self.BASE_URL}/users/{username}/repos"
        params = {"page": page, "per_page": per_page}

        async with self.async_client as client:
            response = await client.get(url, params=params)
            data = response.json()
            # API rate limit
            if response.status_code == 403:
                raise HTTPException(status_code=403, detail=data["message"])

        return [Repository.parse_obj(item) for item in data]
