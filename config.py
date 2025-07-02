import os
from typing import Optional

class Settings:
    # Server settings
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    
    # API settings
    API_TITLE: str = "Simple FastAPI"
    API_DESCRIPTION: str = "A super simple FastAPI project"
    API_VERSION: str = "1.0.0"
    
    # CORS settings
    ALLOWED_ORIGINS: list = ["*"]  # In production, specify actual origins
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100

# Create global settings instance
settings = Settings()