from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017"
    mongodb_database: str = "gamedev_ai"
    frontend_url: str = "http://localhost:5173"
    ai_provider: str = "mock"
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

@lru_cache
def get_settings(): return Settings()
