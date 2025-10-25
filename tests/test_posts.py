import pytest

@pytest.mark.asyncio
async def test_get_posts(api_client):
    response = await api_client.get("/posts")
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert "title" in posts[0]
