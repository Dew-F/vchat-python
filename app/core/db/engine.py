from sqlalchemy import create_engine

from app.core.config import settings
from app.core.db.base import Base

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},  # для SQLite
    echo=settings.debug,
)
