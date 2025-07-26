from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from core.config import config


async def init_redis():
    """Initialize the redis."""
    redis = aioredis.from_url(config.redis_url, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="skillmate-cache")


# TODO: write test for below code when uncommented
# async def clear_a_single_redis_key(key:str):
#     """Clear a single key cache."""
#     await FastAPICache.get_backend().delete(key)

# async def clear_whole_namespace(name_space:str="skillmate-cache"):
#     """Delete full redis namespace."""
#     await FastAPICache.clear(namespace=name_space)
