from fastapi import APIRouter, status, Query
from typing import Annotated
from bson import ObjectId

from schemas.news_schemas import News
from database.database import news_collection as db
from serializers.news_serializer import newsSerializer, newsListSerializer

    
router = APIRouter(prefix='/news')


@router.post('/create-news',  status_code=status.HTTP_201_CREATED)
async def createNews(payload: News):
    result = db.insert_one(payload.model_dump())
    new_news = newsSerializer(db.find_one({'_id': result.inserted_id}))
    return {'data': new_news}


@router.get('/get-news', status_code=status.HTTP_200_OK)
async def getNews():
    result = newsListSerializer(db.find())
    return {'data': result}


@router.get('/get-popular-news', status_code=status.HTTP_200_OK)
async def getPopularNews():
    result = newsListSerializer(db.find({"is_popular": True}))
    return {'data': result}


@router.get('/get-news-detail', status_code=status.HTTP_200_OK)
async def getNewsDetail(news_id: Annotated[str, Query()]):
    result = newsSerializer(db.find_one({"_id": ObjectId(news_id)}))
    return {'data': result}
