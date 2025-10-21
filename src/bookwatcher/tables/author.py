from datetime import datetime

from sqlalchemy import String, Text, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .declarative_base import Base
from .ulid import gen_ulid


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


