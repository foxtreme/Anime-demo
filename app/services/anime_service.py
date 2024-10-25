from fastapi import Depends
from app.models.anime import Anime
from app.repositories.anime_repository import get_anime_repo, AnimeRepository
from app.schemas.anime_schema import AnimeSchema, UpdateAnimeSchema
from typing import Optional


class AnimeService:
    def __init__(self, anime_repository: AnimeRepository):
        self.anime_repository = anime_repository

    def create_anime(self, anime_data: AnimeSchema) -> AnimeSchema:
        anime_model = Anime(**anime_data.dict(exclude_unset=True))
        new_anime = self.anime_repository.create(anime_model)
        return AnimeSchema.from_orm(new_anime)

    def get_anime_list(self):
        anime_list = self.anime_repository.get_all()
        return [AnimeSchema.from_orm(anime) for anime in anime_list]

    def get_anime_by_id(self, anime_id: int) -> AnimeSchema:
        anime = self.anime_repository.get_by_id(anime_id)
        return AnimeSchema.from_orm(anime)

    def update_anime(self, anime_id: int, anime_data: UpdateAnimeSchema) -> Optional[AnimeSchema]:
        updated_anime = self.anime_repository.update(anime_data.dict(exclude_unset=True), anime_id)
        if updated_anime:
            return AnimeSchema.from_orm(updated_anime)
        return None

    def delete_anime(self, anime_id: int) -> Optional[int]:
        deleted_id = self.anime_repository.delete(anime_id)
        return deleted_id if deleted_id else None


def get_anime_service(anime_repository: AnimeRepository = Depends(get_anime_repo)):
    return AnimeService(anime_repository=anime_repository)
