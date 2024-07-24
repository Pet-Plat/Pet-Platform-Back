import os
import sys

import pytest

from httpx import AsyncClient, ASGITransport

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.main import app


@pytest.fixture(scope='function', autouse=True)
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac