import httpx
from core.config import settings

class APIClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or settings.base_url
        self.client = httpx.AsyncClient(base_url=self.base_url)

    async def get(self, endpoint: str):
        return await self.client.get(endpoint)

    async def post(self, endpoint: str, json: dict):
        return await self.client.post(endpoint, json=json)

    async def close(self):
        await self.client.aclose()
