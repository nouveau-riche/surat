def eventSerializer(event) -> dict:
    return {
        "id": str(event['_id']),
        "name": event['name'],
        "event_date": event['event_date'],
        "description": event['description'],
        "is_popular": event['is_popular'],
        "image": event['image'],
        "video": event['video'],
        "created_by": event['created_by'],
        "created_at": event['created_at']
    }


def eventListSerializer(events) -> list:
    return [eventSerializer(item) for item in events]