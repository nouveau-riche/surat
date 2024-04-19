def newsSerializer(event) -> dict:
    return {
        "id": str(event['_id']),
        "title": event['title'],
        "news_date": event['news_date'],
        "description": event['description'],
        "is_popular": event['is_popular'],
        "image": event['image'],
        "created_by": event['created_by'],
        "created_at": event['created_at']
    }


def newsListSerializer(news) -> list:
    return [newsSerializer(item) for item in news]