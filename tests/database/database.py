import pytest

from src.models.user import User, City, UserPhoto


@pytest.mark.asyncio
async def test_tables(database_session):
    assert database_session.query(User)
    # assert database_session.query(City)
    # assert database_session.query(UserPhoto)
