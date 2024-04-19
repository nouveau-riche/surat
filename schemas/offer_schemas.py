from pydantic import BaseModel
from datetime import datetime as date
import datetime


# we don't need ids in schemas as these are param which we need to hit api request
class Offer(BaseModel):
    """
    Schema for offer
    """

    title: str
    offer_start_date: date
    offer_end_date: date
    description: str
    cuisine: str
    lat_long: list[int]
    google_maps_url: str
    image: str | None = None
    is_popular: bool | None = bool(False)
    created_at: datetime.datetime = datetime.datetime.now()
    created_by: str | None = None
