from fastapi import APIRouter, Depends

from schemas import Pagination
from services import UserRepositoryService, get_user_repository_service

router = APIRouter(
    prefix='/users',
    tags=['user']
)


async def pagination_parameters(page: int = 1, per_page: int = 10):
    return Pagination(page=page, per_page=per_page)


@router.get("/{username}/repos")
async def get_user_repositories(username: str,
                                pagination: Pagination = Depends(pagination_parameters),
                                service: UserRepositoryService = Depends(get_user_repository_service)):
    return await service.get_user_repositories(username, page=pagination.page, per_page=pagination.per_page)
