from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import event_router, news_router, offer_router, user_router

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(event_router.router)
app.include_router(news_router.router)
app.include_router(offer_router.router)
app.include_router(user_router.router)


@app.get('/')
async def root():
    return {"Server is running": "yes"}
