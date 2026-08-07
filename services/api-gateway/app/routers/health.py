"""Health check router — liveness for local, Docker, and Render."""

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
async def health() -> dict[str, str]:
    """Return a simple OK payload so orchestrators know the process is up."""
    return {"status": "ok"}
