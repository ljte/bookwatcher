from fastapi import APIRouter

from bookwatcher.database import DatabaseAdapter
from bookwatcher.repositories.author import AuthorRepository
from bookwatcher.services.author import AuthorService
from bookwatcher.tables import Author
from ..serializers import AuthorSerializer

author_router = APIRouter(prefix="/authors")


def db() -> DatabaseAdapter:
    return DatabaseAdapter(
        "postgresql",
        "psycopg2",
        "bookwatcher",
        "password",
        "localhost",
        5434,
        "bookwatcher",
    )


def author_service() -> AuthorService:
    return AuthorService(
        AuthorRepository(db())
    )


@author_router.get("", response_model=list[AuthorSerializer])
def list_authors() -> list[AuthorSerializer]:
    service = author_service()
    return [AuthorSerializer.model_validate(a) for a in service.get_authors()]


@author_router.get("/{author_id}", response_model=AuthorSerializer | None)
def list_authors(author_id: str) -> AuthorSerializer | None:
        service = author_service()
        return AuthorSerializer.model_validate(service.get_author(author_id))
