from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .declarative_base import Base
from .ulid import gen_ulid


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
