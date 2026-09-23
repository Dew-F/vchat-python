from fastapi import FastAPI

from app.core.exception_handlers import register_exception_handlers
from app.users.router import router as users_router

app = FastAPI(title="VChat API")

register_exception_handlers(app)

app.include_router(users_router)
