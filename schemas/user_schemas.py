from pydantic import BaseModel, Field, EmailStr
import datetime



# we don't need ids in schemas as these are param which we need to hit api request
class User(BaseModel):
    """
    Schema for User
    """

    firebase_uid: str
    name: str
    phone: str = Field(max_length= 10, min_length= 10)
    email: EmailStr | None = None
    image: str | None = None
    deviceOS: str | None = None
    created_at: datetime.datetime = datetime.datetime.now()
    created_by: str | None = None


