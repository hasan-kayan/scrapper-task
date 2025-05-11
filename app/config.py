# app/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyUrl

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    database_url: AnyUrl
    api_base_url: AnyUrl
    log_level: str = "INFO"


settings = Settings()

# Opsiyonel: hızlı erişim için bu satırlar kalabilir
DATABASE_URL = settings.database_url
API_BASE_URL = settings.api_base_url
LOG_LEVEL = settings.log_level
