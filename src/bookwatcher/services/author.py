from bookwatcher.interfaces import IAuthorRepository
from bookwatcher.tables import Author


class AuthorService:

    def __init__(self, author_repository: IAuthorRepository) -> None:
        self._author_repository = author_repository

    def get_authors(self) -> list[Author]:
        return self._author_repository.get_many()

    def get_author(self, author_id: str) -> Author:
        return self._author_repository.get(author_id)

    def save_author(self, author: Author) -> None:
        self._author_repository.save(author)

    def delete_author(self, author_id: str) -> None:
        self._author_repository.delete(author_id)