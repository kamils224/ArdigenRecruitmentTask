from abc import abstractmethod, ABC

import httpx
from fastapi import HTTPException
from pydantic import ValidationError

from config import get_settings
from schemas import Repository


class BaseRepositoryApi(ABC):
    def __init__(self):
        self.async_client = httpx.AsyncClient()

    @abstractmethod
    async def get_user_repositories(
        self, username: str, page: int = 1, per_page: int = 10
    ) -> list[Repository]:
        raise NotImplementedError


class GithubApi(BaseRepositoryApi):
    BASE_URL = get_settings().github_base_url

    async def get_user_repositories(
        self, username: str, page: int = 1, per_page: int = 10
    ) -> list[Repository]:
        url = f"{self.BASE_URL}/users/{username}/repos"
        params = {"page": page, "per_page": per_page}
        try:
            async with self.async_client as client:
                response = await client.get(url, params=params)
                data = response.json()
                if response.status_code in [403, 404]:
                    raise HTTPException(status_code=403, detail=data["message"])

            return [Repository.parse_obj(item) for item in data]
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=str(e))
