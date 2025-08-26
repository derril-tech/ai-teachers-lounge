from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/teachers_lounge"
    
    # NATS
    NATS_URL: str = "nats://localhost:4222"
    
    # S3/MinIO
    S3_ENDPOINT_URL: str = "http://localhost:9000"
    S3_ACCESS_KEY_ID: str = "minioadmin"
    S3_SECRET_ACCESS_KEY: str = "minioadmin"
    S3_BUCKET_NAME: str = "teachers-lounge"
    
    # OpenAI
    OPENAI_API_KEY: str = "your-openai-api-key"
    
    class Config:
        env_file = ".env"


settings = Settings()
