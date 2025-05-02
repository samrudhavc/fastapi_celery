from pydantic_settings import BaseSettings  # Correct import for Pydantic v2

class Settings(BaseSettings):
    APP_NAME: str
    
    # Database Configuration
    DATABASE_URL: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str

    # Celery Configuration
    CELERY_BROKER_URL: str
    CELERY_BACKEND_URL: str

    # SMTP Configuration (For Email)
    SMTP_SERVER: str
    SMTP_PORT: int
    SENDER_EMAIL: str
    SENDER_PASSWORD: str

    class Config:
        env_file = ".env"  # Load environment variables from the .env file

settings = Settings()