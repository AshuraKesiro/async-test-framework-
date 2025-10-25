import pytest
from core.api_client import APIClient

@pytest.fixture(scope="session")
async def api_client():
    client = APIClient()
    yield client
    await client.close()
