from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):

    """Application settings loaded from environment variables."""

    APP_NAME: str = 'Event Analytics Platform'
    DEBUG: bool = True
    ENV: Literal['development', 'production'] = 'development'
    
    # Database settings
    DATABASE_URL: PostgresDsn

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'

# Create a singleton settings instance
settings = Settings()