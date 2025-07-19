from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    REDIS_HOST: str
    REDIS_PORT: int
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    OPENAI_API_KEY: str
    WEAVIATE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
