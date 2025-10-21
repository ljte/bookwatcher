from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from bookwatcher.tables.author import Author
from bookwatcher.tables.book import Book
from bookwatcher.tables.declarative_base import Base

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        author = Author(
            first_name="John",
            last_name="Doe",
            books=[
                Book(title="The Lord of the Rings", isbn=1234567890123),
                Book(title="Harry Potter", isbn=9876543210987),
            ]
        )

        session.add(author)
        session.commit()

        print(author.books)
