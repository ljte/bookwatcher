from pydantic import BaseModel


class BookSerializer(BaseModel):
    id: str
    title: str
    isbn: int
    author_id: str