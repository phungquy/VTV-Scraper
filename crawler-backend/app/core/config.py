import os
from typing import List, Union
from pydantic import BaseSettings, Field
from pathlib import Path


class Base(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Crawler backend - Base Mode"
    # Database
    MONGO_CONNECTION_STRING: str = Field("MONGO_CONNECTION_STRING", cast=str)
    MONGO_DB: str = Field("MONGO_DB", cast=str)

    class Config:
        case_sensitive = True
        env_file = ".env"

class Dev(Base):
    PROJECT_NAME: str = "Crawler backend - Dev mode"
    BACKEND_CORS_ORIGINS: List[str] = [
        "*",
    ]

    class Config:
        env_file = Path(__file__).parents[2] / 'res/.env.dev'


class Staging(Base):
    PROJECT_NAME: str = "Crawler backend - Staging mode"
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://bongda12h.test",
    ]

    class Config:
        env_file = Path(__file__).parents[2] / 'res/.env.staging'


class Prod(Base):
    PROJECT_NAME: str = "Crawler backend - Prod mode"
    BACKEND_CORS_ORIGINS: List[str] = [
        "https://bongda12h.net",
    ]

    class Config:
        env_file = Path(__file__).parents[2] / 'res/.env.prod'


config = dict(
    dev=Dev,
    staging=Staging,
    prod=Prod
)

settings: Union[Dev, Staging, Prod] = config[os.environ.get('FASTAPI_MODE', 'dev').lower()]()
