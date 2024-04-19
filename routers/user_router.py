from fastapi import APIRouter, Query
from typing import Annotated

from schemas.user_schemas import User
from serializers.user_serializer import userSerializer
from database.database import user_collection as db

router = APIRouter(prefix='/auth')

@router.post('/create-user')
async def createUser(payload: User):
    result = db.insert_one(payload.model_dump())
    new_user = userSerializer(db.find_one({'_id': result.inserted_id}))
    return {'data': new_user}   

@router.get('/get-user')
async def getUser(firebase_uid: Annotated[str, Query()]):
    result = userSerializer( db.find_one({'firebase_uid': firebase_uid}))
    return {'data': result}



