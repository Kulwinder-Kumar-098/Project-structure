from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str = "Task Manager"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./tasks.db"


settings = Settings()
