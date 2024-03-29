import pytest_asyncio

from src.models.user import User
from src.repositories.auth import AuthService
from src.schemas.auth import CreateAuthModel


@pytest_asyncio.fixture
async def user(database_session) -> User:
    user_service = AuthService(database_session)
    data = CreateAuthModel(
        name='test',
        surname='test',
        email='test',
        phone='+79012345678',
        password='test9999'
    )
    user = await user_service.create(data)
    return user
