"""All Routing for the API routes."""
from fastapi import APIRouter

from trekapi.api import series

router = APIRouter(tags=["Trekpedia API"], prefix="/api/v1")
router.include_router(series.router)
