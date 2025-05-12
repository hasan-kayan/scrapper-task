from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    """
    Settings configuration class for the application.

    Attributes:
        DATABASE_URL (str): The URL for the database connection, loaded from the environment.
        API_BASE_URL (str): The base URL for the API, loaded from the environment.
        LOG_LEVEL (str): The logging level for the application. Defaults to "INFO".

    Inner Class:
        Config:
            env_file (str): Specifies the environment file to load variables from. Defaults to ".env".
    """
    DATABASE_URL: str
    API_BASE_URL: str
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
