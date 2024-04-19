from fastapi import FastAPI

from routers import event_router, news_router, offer_router, user_router

app = FastAPI()

app.include_router(event_router.router)
app.include_router(news_router.router)
app.include_router(offer_router.router)
app.include_router(user_router.router)


# // work on adding user image while integrating s3


@app.get('/')
async def root():
    return {"Server is running": "yes"}
