from fastapi import APIRouter, status, Query
from typing import Annotated
from bson import ObjectId

from schemas.event_schemas import Event
from database.database import events_collection as db
from serializers.event_serializer import eventSerializer, eventListSerializer


router = APIRouter(prefix='/event')


@router.post('/create-event',  status_code=status.HTTP_201_CREATED)
async def createEvent(payload: Event):
    result = db.insert_one(payload.model_dump())
    new_event = eventSerializer(db.find_one({'_id': result.inserted_id}))
    return {'data': new_event}


@router.get('/get-events', status_code=status.HTTP_200_OK)
async def getEvents():
    result = eventListSerializer(db.find())
    return {'data': result}


@router.get('/get-popular-events', status_code=status.HTTP_200_OK)
async def getPopularEvents():
    result = eventListSerializer(db.find({"is_popular": True}))
    return {'data': result}


@router.get('/get-event-detail', status_code=status.HTTP_200_OK)
async def getEventDetail(event_id: Annotated[str, Query()]):
    result = eventSerializer(db.find_one({"_id": ObjectId(event_id)}))
    return {'data': result}
