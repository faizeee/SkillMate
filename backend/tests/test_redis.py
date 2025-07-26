from fastapi_cache import FastAPICache
from core.redis import init_redis
import pytest


@pytest.mark.asyncio
async def test_redis_ping():
    await init_redis()
    redis = FastAPICache.get_backend().redis
    pong = await redis.ping()
    assert pong is True
