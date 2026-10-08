from collections.abc import Generator

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

from app.main import app
from app.core.db.session import get_session
from app.core.db.base import Base

from app.users import models as _users_models  # noqa: F401
from app.channels import models as _channels_models  # noqa: F401


@pytest.fixture
def engine() -> Generator[Engine, None, None]:
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture
def session(engine) -> Generator[Session, None, None]:
    with Session(engine, expire_on_commit=False) as session:
        yield session


@pytest.fixture
def client(session) -> Generator[TestClient, None, None]:
    app.dependency_overrides[get_session] = lambda: session
    yield TestClient(app)
    app.dependency_overrides.clear()
