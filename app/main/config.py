from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict
from pydantic_settings import BaseSettings as _BaseSettings


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8",
    )


class RedisConfig(BaseSettings, env_prefix="REDIS_"):
    host: str
    port: int
    password: str


class ApplicationConfig(BaseSettings, env_prefix="APPLICATION_"):
    title: str
    debug: bool = False


class Config(BaseModel):
    app: ApplicationConfig
    redis: RedisConfig


def create_config() -> Config:
    return Config(
        app=ApplicationConfig(),
        redis=RedisConfig(),
    )
