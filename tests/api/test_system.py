import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_info_api(api_client: AsyncClient) -> None:
    response = await api_client.get("/api/info")
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == "0.1.0"
    assert data["status"] == "operational"
