from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "FastAPI Starter"
    DEBUG: bool = True

    # Database settings
    DATABASE_URL: str = "sqlite:///./dev.db"  # SQLite for development
    DB_ECHO: bool = False  # Set to True to see SQL queries in logs

    # Security settings
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()