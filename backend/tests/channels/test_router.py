def test_create_channel(client):
    response = client.post(
        "/api/v1/channels",
        json={
            "name": "test",
            "is_voice": True,
            "is_private": False,
            "is_direct": False,
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "test"
    assert data["is_voice"] is True
    assert data["is_private"] is False
    assert data["is_direct"] is False
    assert "id" in data


def test_create_channel_duplicate_name(client):
    response = client.post(
        "/api/v1/channels",
        json={
            "name": "test",
        },
    )

    assert response.status_code == 201

    response = client.post(
        "/api/v1/channels",
        json={
            "name": "test",
        },
    )

    assert response.status_code == 409
    assert response.json() == {"code": "CHANNEL_ALREADY_EXISTS", "field": "name"}


def test_get_channel_not_found(client):
    response = client.get("/api/v1/channels/9999")
    assert response.status_code == 404
    assert response.json() == {"code": "CHANNEL_NOT_FOUND", "channel_id": 9999}
