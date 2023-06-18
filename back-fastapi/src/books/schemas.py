from typing import Optional

from pydantic import BaseModel


class FoundBook(BaseModel):

    livelib_id: int
    title: str
    author: Optional[str]


class FoundBooks(BaseModel):

    count: int
    books: Optional[list[FoundBook]]


class FullBook(BaseModel):

    id: int
    title: str
    author: Optional[str]
    cover_url: Optional[str]


class FullBooks(BaseModel):

    count: int
    books: Optional[list[FullBook]]
