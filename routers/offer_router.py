from fastapi import APIRouter, status, Query
from typing import Annotated 
from bson import  ObjectId

from schemas.offer_schemas import Offer
from database.database import offer_collection as db
from serializers.offer_serializer import offerSerializer, offerListSerializer

router = APIRouter(prefix='/offer')

@router.post('/create-offer',  status_code=status.HTTP_201_CREATED)
async def createOffer(payload: Offer):
    result = db.insert_one(payload.model_dump())
    new_offer = offerSerializer(db.find_one({'_id': result.inserted_id}))
    return {'data': new_offer}


@router.get('/get-offers', status_code=status.HTTP_200_OK)
async def getOffers():
    result = offerListSerializer(db.find())
    return {'data': result}


@router.get('/get-popular-offers', status_code=status.HTTP_200_OK)
async def getPopularNews():
    result = offerListSerializer(db.find({"is_popular": True}))
    return {'data': result}


@router.get('/get-offer-detail', status_code=status.HTTP_200_OK)
async def getNewsDetail(offer_id: Annotated[str, Query()]):
    result = offerSerializer(db.find_one({"_id": ObjectId(offer_id)}))
    return {'data': result}