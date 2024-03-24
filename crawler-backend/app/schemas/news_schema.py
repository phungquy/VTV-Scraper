from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class ListNewsOut(BaseModel):
    news_id: str
    title: str
    author: str
    avatar: Optional[str]
    avatar_desc: Optional[str]
    sapo: str
    scraped_time: datetime


class SingleNewsOut(BaseModel):
    news_id: str
    title: str
    author: str
    avatar: Optional[str]
    avatar_desc: Optional[str]
    sapo: str
    content: str
    scraped_time: datetime
