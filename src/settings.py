from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore" 
    )

    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5434/ads_db"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_topic_ads: str = "ads"
    auth_service_url: str = "http://localhost:8000"

    POSTGRES_CONNECTION_STRING: str | None = None
    POSTGRES_DATABASE_NAME: str | None = None
    POSTGRES_HOST: str | None = None
    POSTGRES_PORT: int | None = None
    POSTGRES_USERNAME: str | None = None
    POSTGRES_PASSWORD: str | None = None
    
    KAFKA_BROKERS: str | None = None
    KAFKA_TOPIC_MARKETPLACE_ADS: str | None = None

    @model_validator(mode="after")
    def apply_platform_env_vars(self):
        if self.POSTGRES_CONNECTION_STRING:
            url = self.POSTGRES_CONNECTION_STRING
            if url.startswith("postgres://"):
                url = url.replace("postgres://", "postgresql+asyncpg://", 1)
            self.database_url = url
            
        elif self.POSTGRES_HOST and self.POSTGRES_USERNAME:
            self.database_url = (
                f"postgresql+asyncpg://{self.POSTGRES_USERNAME}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT or 5432}/{self.POSTGRES_DATABASE_NAME}"
            )

        if self.KAFKA_BROKERS:
            self.kafka_bootstrap_servers = self.KAFKA_BROKERS
            
        if self.KAFKA_TOPIC_MARKETPLACE_ADS:
            self.kafka_topic_ads = self.KAFKA_TOPIC_MARKETPLACE_ADS

        return self