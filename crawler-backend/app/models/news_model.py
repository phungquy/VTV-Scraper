from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, before_event, Replace, Insert
from pydantic import Field


class News(Document):
    original_id: str
    original_url: str
    title: str
    author: str
    avatar: Optional[str] = None
    avatar_desc: Optional[str] = None
    sapo: str
    content: str
    scraped_time: datetime = Field(default_factory=datetime.utcnow)


    def __repr__(self):
        return f"<News {self.title}>"

    def __str__(self):
        return self.title

    def __hash__(self):
        return hash(self.original_url)

    def __eq__(self, other):
        if isinstance(other, News):
            return self.graph_model == other.graph_model
        return False

    class Settings:
        name = "thegioi_news"
