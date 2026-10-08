def test_create_user(client):
    response = client.post(
        "/api/v1/users",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "supersecret123",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"
    assert "id" in data
    assert "password_hash" not in data


def test_create_user_duplicate_username(client):
    response = client.post(
        "/api/v1/users",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "supersecret123",
        },
    )

    assert response.status_code == 201

    response = client.post(
        "/api/v1/users",
        json={
            "username": "alice",
            "email": "alice2@example.com",
            "password": "supersecret123",
        },
    )

    assert response.status_code == 409
    assert response.json() == {"code": "USER_ALREADY_EXISTS", "field": "username"}


def test_create_user_duplicate_email(client):
    response = client.post(
        "/api/v1/users",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "supersecret123",
        },
    )

    assert response.status_code == 201

    response = client.post(
        "/api/v1/users",
        json={
            "username": "alice2",
            "email": "alice@example.com",
            "password": "supersecret123",
        },
    )

    assert response.status_code == 409
    assert response.json() == {"code": "USER_ALREADY_EXISTS", "field": "email"}


def test_get_user_not_found(client):
    response = client.get("/api/v1/users/9999")
    assert response.status_code == 404
    assert response.json() == {"code": "USER_NOT_FOUND", "user_id": 9999}


def test_create_user_short_username(client):
    response = client.post(
        "/api/v1/users",
        json={
            "username": "ab",  # < 3
            "email": "alice@example.com",
            "password": "supersecret123",
        },
    )
    assert response.status_code == 422


def test_user_password_is_hashed(client, session):
    from app.users.models import User
    from sqlalchemy import select

    client.post(
        "/api/v1/users",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "supersecret123",
        },
    )

    user = session.execute(select(User).where(User.username == "alice")).scalar_one()
    assert user.password_hash != "supersecret123"
    assert user.password_hash.startswith("$argon2")
