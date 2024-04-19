def offerSerializer(offer) -> dict:
    return {
        "id": str(offer['_id']),
        "title": offer['title'],
        "offer_start_date": offer['offer_start_date'],
        "offer_end_date": offer['offer_end_date'],
        "description": offer['description'],
        "cuisine": offer['cuisine'],
        "lat_long": offer['lat_long'],
        "google_maps_url": offer['google_maps_url'],
        "image": offer['image'],
        "is_popular": offer['is_popular'],
        "created_by": offer['created_by'],
        "created_at": offer['created_at']
    }


def offerListSerializer(offers) -> list:
    return [offerSerializer(item) for item in offers]