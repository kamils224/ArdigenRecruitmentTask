from fastapi.testclient import TestClient

from external.repository_api import BaseRepositoryApi
from main import app
from schemas import Repository
from services import get_user_repository_service, UserRepositoryService

fake_data = [
    {
        "id": 158076526,
        "name": "BirthdayAttack",
        "description": "Simulation of birthday attack (cryptographic attack).",
        "html_url": "https://api.github.com/repos/kamils224/BirthdayAttack",
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": "C#",
        "forks_count": 0,
        "size": 5120,
        "open_issues": 0,
        "created_at": "2018-11-18T11:26:35+00:00",
        "updated_at": "2020-05-15T15:51:09+00:00",
    },
    {
        "id": 303857089,
        "name": "BooksManager",
        "description": None,
        "html_url": "https://api.github.com/repos/kamils224/BooksManager",
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": "Python",
        "forks_count": 0,
        "size": 50,
        "open_issues": 0,
        "created_at": "2020-10-14T00:02:55+00:00",
        "updated_at": "2020-10-22T16:06:55+00:00",
    },
]

client = TestClient(app)


async def override_get_user_repository_service():
    return UserRepositoryService(api=FakeGithubApi())


app.dependency_overrides[
    get_user_repository_service
] = override_get_user_repository_service


class FakeGithubApi(BaseRepositoryApi):
    async def get_user_repositories(
        self, username: str, page: int = 1, per_page: int = 10
    ) -> list[Repository]:
        return [Repository.parse_obj(item) for item in fake_data]


def test_get_user_repositories_returns_200():
    response = client.get("/users/name/repos")
    assert response.status_code == 200


def test_get_user_repositories_contains_data():
    response = client.get("/users/name/repos")
    data = response.json()
    assert len(data) == 2
    assert data[0]["id"] == 158076526
    assert data[1]["id"] == 303857089
