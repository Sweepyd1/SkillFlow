from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from pathlib import Path

class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    # DB_URL: SecretStr
    HOME_PATH:Path = Path.cwd().parent
    # ADMIN_ID: int
    model_config = SettingsConfigDict(
        env_file = f"{HOME_PATH}/.env"
    )


settings = Settings()