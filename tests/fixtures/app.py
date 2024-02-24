import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from async_asgi_testclient import TestClient
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import async_session_maker
from src.services.main import create_app


@pytest_asyncio.fixture
async def app():
    instance = create_app()
    async with LifespanManager(instance):
        yield instance


@pytest_asyncio.fixture
async def client(app):
    return TestClient(app)


@pytest.fixture(scope="module")
async def database_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
