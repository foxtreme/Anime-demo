from pydantic import BaseModel, Field
from typing import Optional
from app.models.anime import Anime


class AnimeSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str
    status: str
    genre: Optional[str]
    author: Optional[str]
    platform: Optional[str]

    class Config:
        from_attributes = True

    @classmethod
    def from_model(cls, model: Anime) -> "AnimeSchema":
        return cls(
            id=model.id,
            name=model.name,
            status=model.status,
            genre=model.genre,
            author=model.author,
            platform=model.platform
        )


class UpdateAnimeSchema(BaseModel):
    name: Optional[str]
    status: Optional[str]
    genre: Optional[str]
    author: Optional[str]
    platform: Optional[str]

    class Config:
        from_attributes = True
