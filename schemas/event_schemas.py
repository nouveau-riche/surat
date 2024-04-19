from pydantic import BaseModel
from datetime import datetime as date
import datetime


# we don't need ids in schemas as these are param which we need to hit api request
class Event(BaseModel):
    """
    Schema for event
    """

    name: str
    event_date: date
    description: str
    image: str | None = None
    video: str | None = None
    is_popular: bool | None = bool(False)
    created_at: datetime.datetime = datetime.datetime.now()
    created_by: str | None = None
