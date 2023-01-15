from external.repository_api import BaseRepositoryApi, GithubApi


class UserRepositoryService:

    def __init__(self, api: BaseRepositoryApi):
        self.api = api

    async def get_user_repositories(self,
                                    username: str,
                                    page: int = 1,
                                    per_page: int = 10):

        return await self.api.get_user_repositories(username, page=page, per_page=per_page)


def get_user_repository_service() -> UserRepositoryService:
    return UserRepositoryService(api=GithubApi())
