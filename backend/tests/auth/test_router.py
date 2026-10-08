def test_login_success(client):
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
        json={"username": "alice", "password": "supersecret123"},
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
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
        json={"username": "alice", "password": "wrongpassword"},
    )

    assert response.status_code == 401
    assert response.json() == {"code": "INVALID_CREDENTIALS"}


def test_login_unknown_user(client):
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "nobody", "password": "anypassword"},
    )

    assert response.status_code == 401
    assert response.json() == {"code": "INVALID_CREDENTIALS"}


def test_login_wrong_password_and_unknown_user_are_identical(client):
    client.post(
        "/api/v1/users",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "supersecret123",
        },
    )

    wrong_pass = client.post(
        "/api/v1/auth/login",
        json={"username": "alice", "password": "wrongpassword"},
    )

    unknown_user = client.post(
        "/api/v1/auth/login",
        json={"username": "nobody", "password": "anypassword"},
    )

    assert wrong_pass.status_code == unknown_user.status_code
    assert wrong_pass.json() == unknown_user.json()


def test_me_with_token(client, auth_token):
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {auth_token}"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"
    assert "password_hash" not in data


def test_me_without_token(client):
    response = client.get("/api/v1/users/me")

    assert response.status_code == 401
    assert response.json() == {"code": "INVALID_TOKEN"}


def test_me_with_invalid_token(client):
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": "Bearer garbage"},
    )

    assert response.status_code == 401
    assert response.json() == {"code": "INVALID_TOKEN"}


def test_me_with_expired_token(client, expired_token):
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {expired_token}"},
    )

    assert response.status_code == 401
    assert response.json() == {"code": "INVALID_TOKEN"}
