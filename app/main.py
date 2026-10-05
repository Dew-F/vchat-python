from fastapi import FastAPI

from app.users.router import router as users_router
from app.channels.router import router as channel_router
from app.core.exception.handlers import register_exception_handlers

app = FastAPI()
register_exception_handlers(app)

app.include_router(users_router)
app.include_router(channel_router)
