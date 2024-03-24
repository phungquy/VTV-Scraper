from http.client import HTTPException
from typing import Optional, List
from uuid import UUID
import pymongo.errors

# internal
from app.models.news_model import News


class NewsService:
    @staticmethod
    async def get_all_news() -> List[News]:
        all_news = await News.find().to_list()
        return all_news

    @staticmethod
    async def retrieve_single_news(original_id: str) -> News:
        single_news = await News.find_one(News.original_id == original_id)
        if single_news is None:
            raise pymongo.errors.OperationFailure("News not found")
        return single_news
