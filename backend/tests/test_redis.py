from fastapi_cache import FastAPICache
import pytest


@pytest.mark.asyncio
async def test_redis_ping():
    # await init_redis()
    redis = FastAPICache.get_backend().redis
    pong = await redis.ping()
    assert pong is True


@pytest.mark.asyncio
async def test_set_and_get_from_redis():
    redis = FastAPICache.get_backend().redis
    await redis.set("foo", "bar")
    val = await redis.get("foo")
    assert val == "bar"
