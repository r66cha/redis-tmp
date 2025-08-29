"""Redis"""

# -- Imports

import redis.asyncio as redis
from pydantic_settings import BaseSettings, SettingsConfigDict

# -- Exports

__all__ = ["rediska", "RedisManager"]

# --


class RedisManager(BaseSettings):

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    DIALECT: str = "redis"

    model_config = SettingsConfigDict(
        env_file=".env.dev",
        extra="ignore",
    )

    @property
    def _url(self):
        return f"{self.DIALECT}://{self.REDIS_HOST}:{self.REDIS_PORT}"

    def get_aioredis_client(self):
        return redis.from_url(
            url=self._url,
            db=0,
            decode_responses=True,
        )


rediska = RedisManager().get_aioredis_client()
