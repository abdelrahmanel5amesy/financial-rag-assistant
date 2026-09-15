from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CHROMA_DB_PATH: str = "../data/chroma_db"
    COLLECTION_NAME: str = "financial_filings"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    OLLAMA_MODEL: str = "llama3.2"
    OLLAMA_HOST: str = "http://localhost:11434"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()