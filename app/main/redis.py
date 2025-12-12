import redis.asyncio as redis
from .config import RedisConfig

redis_config = RedisConfig()
redis_client = redis.Redis(host=redis_config.host, port=redis_config.port)
