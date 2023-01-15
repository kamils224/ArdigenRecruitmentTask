from datetime import datetime

from pydantic import BaseModel, Field


class Pagination(BaseModel):
    page: int
    per_page: int


class Repository(BaseModel):
    id_: int = Field(alias="id")
    name: str
    description: str | None
    html_url: str
    stargazers_count: int
    watchers_count: int
    language: str
    forks_count: int
    size: int
    open_issues: int
    created_at: datetime
    updated_at: datetime
