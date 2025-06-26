from sqlmodel import Field, SQLModel
from typing import Optional


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    year: int
    genre: Optional[str] = Field(default=None, max_length=50)
