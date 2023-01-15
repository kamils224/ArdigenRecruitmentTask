from fastapi import APIRouter, Depends, HTTPException

from schemas import Pagination, Repository
from services import UserRepositoryService, get_user_repository_service

router = APIRouter(
    prefix='/users',
    tags=['users']
)


async def pagination_parameters(page: int = 1, per_page: int = 10):
    return Pagination(page=page, per_page=per_page)


@router.get("/{username}/repos", response_model=list[Repository])
async def get_user_repositories(username: str,
                                pagination: Pagination = Depends(pagination_parameters),
                                service: UserRepositoryService = Depends(get_user_repository_service)):
    # currently we skip details about pagination like total pages etc.,
    # it is not provided by GitHub api by default and needs to be calculated
    return await service.get_user_repositories(username, page=pagination.page, per_page=pagination.per_page)
