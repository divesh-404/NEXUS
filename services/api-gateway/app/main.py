"""NEXUS API gateway — FastAPI application entrypoint.

Wires: settings → logging → correlation middleware → routers.
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings
from app.middleware.correlation import CorrelationIdMiddleware
from app.routers import health


def _configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup/shutdown hook — reserved for Redis/Kafka clients in later phases."""
    settings = get_settings()
    _configure_logging(settings.log_level)
    logging.getLogger(__name__).info(
        "starting %s env=%s", settings.app_name, settings.environment
    )
    yield
    logging.getLogger(__name__).info("shutting down %s", settings.app_name)


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, lifespan=lifespan)
    # Last added = outermost in Starlette; add correlation so it wraps all routes.
    app.add_middleware(CorrelationIdMiddleware)
    app.include_router(health.router)
    return app


app = create_app()
