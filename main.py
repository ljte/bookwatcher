from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from bookwatcher.api.database import DatabaseAdapter
from bookwatcher.tables.author import Author
from bookwatcher.tables.book import Book

engine = create_engine("postgresql+psycopg2://bookwatcher:password@localhost:5434/bookwatcher", echo=True)

if __name__ == '__main__':
    database_adapter = DatabaseAdapter(
        "postgresql",
        "psycopg2",
        "bookwatcher",
        "password",
        "localhost",
        5434,
        "bookwatcher",
    )

    with database_adapter.make_session() as session:
        author = Author(
            first_name="John",
            last_name="Doe",
            books=[
                Book(title="Harry Potter", isbn=9876543210987),
            ]
        )

        session.add(author)
        session.commit()

        print(author.books)
