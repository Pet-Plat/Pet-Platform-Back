import os
from typing import Literal

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict, BaseSettings


if os.getcwd().endswith("src"):
    DOTENV = os.path.join(os.path.pardir, ".env")
else:
    DOTENV = ".env"


class PGConfig(BaseModel):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    DATABASE: str
    TEST_DATABASE_URL: str

    @property
    def pg_dns(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"

    @property
    def pg_test_dns(self):
        return self.TEST_DATABASE_URL


class AppRunConfig(BaseModel):
    HOST: str
    PORT: int
    MODE: Literal["DEV", "TEST", "PROD"]
    CORS_ORIGINS: str | list[str]

    @property
    def cors_as_list(self):
        return self.CORS_ORIGINS.split(", ")


class APIConfig(BaseModel):
    CURRENT_VERSION: str


class SecurityConfig(BaseModel):
    SECRET_KEY: str
    ENCRYPT_KEY: str
    HASH_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


class RabbitMQConfig(BaseModel):
    ...

    @property
    def broker_dns(self):
        raise NotImplementedError()


class S3Config(BaseModel):
    ...

    @property
    def s3_dns(self):
        raise NotImplementedError()


class AuthServiceConfig(BaseModel):
    ...

    @property
    def auth_service_dns(self):
        raise NotImplementedError()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=DOTENV, env_prefix="BACKEND__",
                                      env_nested_delimiter="__", case_sensitive=False)

    db: PGConfig
    run: AppRunConfig
    api: APIConfig
    security: SecurityConfig


settings = Settings()
