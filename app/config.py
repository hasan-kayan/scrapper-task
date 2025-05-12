# app/config.py

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

# 🔁 .env dosyasını yükle
load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    # Environment variables
    database_url: str = Field(..., env="DATABASE_URL")
    api_base_url: str = Field(..., env="API_BASE_URL")
    log_level: str = Field("INFO", env="LOG_LEVEL")

    # Optional internal config defaults
    default_sort: str = "recommended"
    default_page_size: int = 500
    default_start_date: str = "2025-06-19"
    default_end_date: str = "2025-07-02"

# ✅ Create settings instance
settings = Settings()

# Optional short aliases
DATABASE_URL = settings.database_url
API_BASE_URL = settings.api_base_url
LOG_LEVEL = settings.log_level
DEFAULT_SORT = settings.default_sort
DEFAULT_PAGE_SIZE = settings.default_page_size
DEFAULT_START_DATE = settings.default_start_date
DEFAULT_END_DATE = settings.default_end_date

# Debug output
if __name__ == "__main__":
    print("✅ Loaded API_BASE_URL:", API_BASE_URL)
    print("✅ Loaded DATABASE_URL:", DATABASE_URL)
