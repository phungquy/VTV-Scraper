import pymongo.errors
from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException, status, Depends

# internal
from app.models.news_model import News
from app.schemas.news_schema import ListNewsOut, SingleNewsOut
from app.services.news_service import NewsService

news_router = APIRouter()


@news_router.get("/", summary="Get all news", response_model=List[ListNewsOut])
async def get_all_news():
    all_news = await NewsService.get_all_news()

    if all_news:
        get_all_news_resp: List[ListNewsOut] = []
        for item in all_news:
            news_out_item = ListNewsOut(
                **item.dict(),
                news_id=item.original_id
            )
            get_all_news_resp.append(news_out_item)

        return get_all_news_resp
    return []


@news_router.get("/{news_id}", summary="Get single news by news_id", response_model=SingleNewsOut)
async def get_single_news(news_id: str):
    single_news = await NewsService.retrieve_single_news(news_id)
    news_out_item = SingleNewsOut(
        **single_news.dict(),
        news_id=single_news.original_id
    )
    return news_out_item
