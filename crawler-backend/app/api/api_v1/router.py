from fastapi import APIRouter
from app.api.api_v1.handlers import news

router = APIRouter()

router.include_router(news.news_router, prefix='/news', tags=['news'])
