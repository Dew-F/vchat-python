from collections.abc import Generator

import pytest

from app.core.config import settings


@pytest.fixture
def auth_token(client) -> str:
    client.post(
        "/api/v1/users",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "supersecret123",
        },
    )
    response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "alice",
            "password": "supersecret123",
        },
    )
    return response.json()["access_token"]


@pytest.fixture
def expired_token() -> str:
    import jwt
    from datetime import datetime, timedelta, timezone

    payload = {
        "sub": "1",
        "exp": datetime.now(timezone.utc) - timedelta(minutes=1),
    }
    return jwt.encode(
        payload,
        key=settings.secret_key,
        algorithm=settings.jwt_algorithm,
    )
