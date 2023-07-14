from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgres://postgres:postgres@postgres:5432/postgres"  # noqa 501


settings = Settings()
