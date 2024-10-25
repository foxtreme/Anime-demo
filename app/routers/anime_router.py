from fastapi import APIRouter, status, HTTPException, Depends
from app.schemas.anime_schema import AnimeSchema, UpdateAnimeSchema
from app.services.anime_service import AnimeService, get_anime_service
from typing import List


router = APIRouter(
    prefix="/anime",
    tags=["anime"],
    responses={404: {"Error": "Not found"}}
)


@router.get("", response_model=List[AnimeSchema], status_code=status.HTTP_200_OK)
def get_anime_list(anime_service: AnimeService = Depends(get_anime_service)):
    return anime_service.get_anime_list()


@router.get("/{anime_id}", response_model=AnimeSchema, status_code=status.HTTP_200_OK)
def get_anime_by_id(anime_id,
                    anime_service: AnimeService = Depends(get_anime_service)):
    anime = anime_service.get_anime_by_id(anime_id)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return anime


@router.post("", response_model=AnimeSchema, status_code=status.HTTP_201_CREATED)
def create_anime(anime: AnimeSchema,
                 anime_service: AnimeService = Depends(get_anime_service)):
    return anime_service.create_anime(anime)


@router.put("/{anime_id}", response_model=AnimeSchema, status_code=status.HTTP_200_OK)
def update_anime(anime_id: int, anime: UpdateAnimeSchema,
                 anime_service: AnimeService = Depends(get_anime_service)):
    updated_anime = anime_service.update_anime(anime_id, anime)
    if not updated_anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return updated_anime


@router.delete("/{anime_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_anime(anime_id: int,
                 anime_service: AnimeService = Depends(get_anime_service)):
    deleted_id = anime_service.delete_anime(anime_id)
    if not deleted_id:
        raise HTTPException(status_code=404, detail="Anime not found")
    return {"message": "Anime deleted successfully"}
