import asyncio
import logging
import os

import pytest

from src.models.user import User

logger = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_auth(user: User, client):
    data = {
        'phone': '+79000000000',
        'password': 'test9999'
    }
    result = await client.post('/auth', json=data)
    result_json = result.json()
    assert result.status_code == 400
    assert result_json['detail'] == 'Пользователь с такими данными уже существует'
    #TODO


@pytest.mark.asyncio
async def test_register(user: User, client):
    data = {
        'phone': '+79000000000',
        'password': 'test9999'
    }
    #TODO