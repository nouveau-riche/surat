def userSerializer(user) -> dict:
    return {
        "id": str(user['_id']),
        "firebase_uid": str(user['firebase_uid']),
        "name": user['name'],
        "phone": user['phone'],
        "email": user['email'],
        "deviceOS": user['deviceOS'],
        "image": user['image'],
        "created_at": user['created_at'],
        "created_by": user['created_by']
    }


