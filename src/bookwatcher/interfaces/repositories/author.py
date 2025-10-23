import abc

from bookwatcher.tables import Author


class IAuthorRepository(abc.ABC):

    @abc.abstractmethod
    def get_many(self) -> list[Author]:
        ...


    @abc.abstractmethod
    def get(self, author_id: str) -> Author:
        ...

    @abc.abstractmethod
    def save(self, author: Author) -> None:
        ...

    @abc.abstractmethod
    def delete(self, author_id: str) -> None:
        ...
