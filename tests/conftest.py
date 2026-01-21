from typing import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient

from src.main_api import app


@pytest.fixture
async def api_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
