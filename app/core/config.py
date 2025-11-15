from pydantic_settings import BaseSettings
from pydantic import Field
import os


class Settings(BaseSettings):
    # === APP CONFIG ===
    APP_NAME: str = "FASTAPI FULL ASYNC PROJECT"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"

    # === DATABASE CONFIG ===
    # Test uchun SQLite
    DATABASE_URL: str = Field(
        default="sqlite+aiosqlite:///./test.db",
        description="Async SQLite URL",
    )

    # Agar keyin PostgreSQLga o'tmoqchi bo'lsangiz:
    # DATABASE_URL: str = "postgresql+asyncpg://postgres:1234@localhost:5432/my_db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
