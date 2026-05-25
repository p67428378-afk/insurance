
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    BASE_RATE: float = 500.0

    class Config:
        env_file = ".env"

settings = Settings()
