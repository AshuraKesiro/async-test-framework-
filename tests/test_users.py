import pytest
from utils.data_generators import user_payload
from utils.validators import validate_user_schema

@pytest.mark.asyncio
async def test_get_users(api_client):
    response = await api_client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    validate_user_schema(users[0])

@pytest.mark.asyncio
async def test_create_user(api_client):
    payload = user_payload()
    response = await api_client.post("/users", json=payload)
    assert response.status_code in (201, 200)
    data = response.json()
    for key in payload.keys():
        assert key in data
