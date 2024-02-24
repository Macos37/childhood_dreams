import pytest_asyncio

from src.models.user import User
from src.repositories.auth import AuthService
from src.schemas.user import CreateUserModel


@pytest_asyncio.fixture
async def user(database_session) -> User:
    user_service = AuthService(database_session)
    data = CreateUserModel(
        name='test',
        surname='test',
        email='test',
        phone='+79012345678',
        password='test9999'
    )
    user = await user_service.create(data)
    return user
