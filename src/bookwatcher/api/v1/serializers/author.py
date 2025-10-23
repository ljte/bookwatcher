from datetime import datetime

from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel


class AuthorSerializer(BaseModel):
    id: str
    first_name: str = Field(serialization_alias="firstName")
    last_name: str = Field(serialization_alias="lastName")
    birthday: datetime

    class Config:
        from_attributes = True
        validate_by_name = True


# class AuthorDetailsSerializer(BaseModel):
#     id: str
#     first_name: str = Field(serialization_alias="firstName")
#     last_name: str = Field(serialization_alias="lastName")
#     birthday: datetime
#     description: str | None = None
#     books: list["BookSerializer"]
