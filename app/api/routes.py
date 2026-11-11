"""API routes for service status and initial ingestion workflow."""

from typing import TypedDict

from fastapi import APIRouter
from fastapi.responses import Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

router = APIRouter()


class HealthResponse(TypedDict):
    status: str


@router.get("/health", tags=["health"], response_model=None)
async def health() -> HealthResponse:
    """Report that the API process is running."""
    return {"status": "ok"}


@router.get("/ready", tags=["health"], response_model=None)
async def readiness() -> HealthResponse:
    """Report API readiness (dependency checks will be added with integrations)."""
    return {"status": "ready"}


@router.get("/metrics", tags=["operations"], include_in_schema=False)
async def metrics() -> Response:
    """Expose Prometheus metrics in the standard text format."""
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
