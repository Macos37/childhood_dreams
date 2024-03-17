import asyncpg
import asyncio
import aiofiles
import os
from contextlib import asynccontextmanager


@asynccontextmanager
async def get_async_session():
    loop = asyncio.get_running_loop()
    pool = await asyncpg.create_pool(
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database=os.environ.get("DB_NAME"),
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        loop=loop
    )
    try:
        yield pool
    finally:
        await pool.close()


async def import_data() -> None:
    async with get_async_session() as pool:
        async with pool.acquire() as session:
            async with session.transaction():
                async with aiofiles.open("script.sql", "r") as f:
                    async for line in f:
                        await session.execute(line.strip())
            await session.close()


async def main():
    await import_data()

asyncio.run(main())
