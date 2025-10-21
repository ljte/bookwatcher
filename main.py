from datetime import datetime

from sqlalchemy import create_engine, String, DateTime, func, Text, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, Session
from sqlalchemy.testing.schema import mapped_column
from ulid import ULID

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)


def gen_ulid() -> str:
    return str(ULID())

class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = 'author'

    id: Mapped[int] = mapped_column(
        String(26),
        primary_key=True,
        default=gen_ulid,
        index=True,
    )
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    birthdate: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    description: Mapped[str] = mapped_column(Text, nullable=True, index=False)

    books: Mapped[list["Book"]] = relationship(
        back_populates="author", cascade="all,delete-orphan"
    )

    def __repr__(self):
        return f"{type(self).__name__}({self.first_name} {self.last_name})"


class Book(Base):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(
        String(26),
        primary_key=True,
        default=gen_ulid,
        index=True,
    )
    title: Mapped[str] = mapped_column(String(255))
    isbn: Mapped[int] = mapped_column(Integer(), unique=True, index=True, nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    description: Mapped[str] = mapped_column(Text, nullable=True, index=False)
    completed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    author: Mapped["Author"] = relationship(back_populates="books")

    def __repr__(self):
        return f"{type(self).__name__}({self.title})"

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
