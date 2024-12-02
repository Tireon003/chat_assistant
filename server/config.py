from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    BOT_API_KEY: str
    OPENAI_API_KEY: str
    OPENAI_MODEL_NAME: str
    OPENAI_BASE_URL: str
    LOG_LEVEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
    )


settings = Settings()
