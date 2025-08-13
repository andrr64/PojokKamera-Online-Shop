# app/core/config.py
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = Field(..., description="Database connection string")

    # App
    DEBUG: bool = False

    # JWT
    SECRET_KEY: str = Field(..., description="Secret key for JWT")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True  # penting: DATABASE_URL ≠ database_url


# Inisialisasi settings
settings = Settings()