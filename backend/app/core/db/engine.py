from sqlalchemy import create_engine

from app.core.config import settings

engine = create_engine(
    settings.database_url,
    echo=settings.debug,
    pool_size=20,
    max_overflow=40,
    pool_timeout=60,
    pool_recycle=3600,
    pool_pre_ping=True,
)
