"""Correlation ID middleware and JSON request logging.

A correlation ID tags one inbound request across logs (and later Kafka, DB, traces).
Clients may send `X-Correlation-ID`; otherwise we generate a UUID4.
"""

from __future__ import annotations

import json
import logging
import time
import uuid
from collections.abc import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger("nexus.access")


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    """Attach correlation_id to request.state, response header, and a JSON access log."""

    header_name = "X-Correlation-ID"

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        incoming = request.headers.get(self.header_name)
        correlation_id = incoming.strip() if incoming else str(uuid.uuid4())
        request.state.correlation_id = correlation_id

        started = time.perf_counter()
        status_code = 500
        try:
            response = await call_next(request)
            status_code = response.status_code
        except Exception:
            duration_ms = (time.perf_counter() - started) * 1000
            logger.error(
                json.dumps(
                    {
                        "event": "request_failed",
                        "correlation_id": correlation_id,
                        "method": request.method,
                        "path": request.url.path,
                        "status_code": status_code,
                        "duration_ms": round(duration_ms, 2),
                    }
                )
            )
            raise

        duration_ms = (time.perf_counter() - started) * 1000
        response.headers[self.header_name] = correlation_id
        logger.info(
            json.dumps(
                {
                    "event": "request",
                    "correlation_id": correlation_id,
                    "method": request.method,
                    "path": request.url.path,
                    "status_code": status_code,
                    "duration_ms": round(duration_ms, 2),
                }
            )
        )
        return response
