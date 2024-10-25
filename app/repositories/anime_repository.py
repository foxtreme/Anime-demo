from sqlmodel import Session
from fastapi import Depends
from app.config import get_db
from app.repositories.base_repository import BaseRepository
from app.models.anime import Anime


class AnimeRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(Anime, session=session)


def get_anime_repo(session: Session = Depends(get_db)):
    return AnimeRepository(session)
