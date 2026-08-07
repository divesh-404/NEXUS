"""Application settings for the NEXUS API gateway.

All configuration is read through this typed Settings object (env + optional .env),
never via scattered os.environ calls in routers/services.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central config. Fields for later phases are stubbed with safe defaults now."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- Phase 1 ---
    app_name: str = "nexus-api-gateway"
    environment: str = "local"
    log_level: str = "INFO"
    host: str = "0.0.0.0"
    port: int = 8000

    # --- Phase 2 (LLM) — unused until then ---
    llm_provider: str = "ollama"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3"
    gemini_api_key: str = ""

    # --- Phase 3 (RAG / Postgres) ---
    database_url: str = ""

    # --- Phase 5 (Redis) ---
    redis_url: str = ""
    redis_url_secondary: str = ""

    # --- Phase 6 (Kafka) ---
    kafka_bootstrap_servers: str = ""
    kafka_events_topic: str = "nexus-events"
    kafka_dlq_topic: str = "dlq-failed"


@lru_cache
def get_settings() -> Settings:
    """Return a process-wide cached Settings instance."""
    return Settings()
