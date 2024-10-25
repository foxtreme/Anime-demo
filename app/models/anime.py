from sqlmodel import SQLModel, Field
from typing import Optional


class Anime(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field()
    status: str = Field()
    genre: Optional[str] = Field()
    author: Optional[str] = Field()
    platform: Optional[str] = Field()
