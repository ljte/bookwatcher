from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import Session


class DatabaseAdapter:
    def __init__(
            self,
            driver: str,
            dialect: str,
            username: str,
            password: str,
            host: str,
            port: int,
            database: str,
    ):
        self._engine = create_engine(
            URL.create(
                drivername=f"{driver}+{dialect}",
                username=username,
                password=password,
                host=host,
                port=port,
                database=database,
            )

        )

    @contextmanager
    def make_session(self) -> Generator[Session, None, None]:
        with Session(self._engine) as session:
            session.begin()
            try:
                yield session
            except Exception:
                session.rollback()
                raise
            else:
                session.commit()
