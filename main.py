from fastapi import FastAPI
from app.routers import channel, giveaway, user, ticket
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

app.include_router(channel.router)
app.include_router(giveaway.router)
