from sqlalchemy import delete

from bookwatcher.database import DatabaseAdapter
from bookwatcher.tables import Author
from bookwatcher.interfaces import IAuthorRepository


class AuthorRepository(IAuthorRepository):

    def __init__(self, db_adapter: DatabaseAdapter) -> None:
        self._db_adapter = db_adapter

    def get_many(self) -> list[Author]:
        with self._db_adapter.make_session() as session:
            return session.query(Author).all()

    def get(self, author_id: str) -> list[Author]:
        with self._db_adapter.make_session() as session:
            return session.get(Author, author_id)

    def save(self, author: Author) -> None:
        with self._db_adapter.make_session() as session:
            session.add(author)

    def delete(self, author_id: str) -> None:
        q = delete(Author).where(Author.id == author_id)
        with self._db_adapter.make_session() as session:
            session.execute(q)


