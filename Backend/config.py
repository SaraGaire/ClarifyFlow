from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    database_url: str = "sqlite+aiosqlite:///./clarityflow.db"
    max_upload_size_mb: int = 25
    temp_audio_dir: str = "./temp"
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
