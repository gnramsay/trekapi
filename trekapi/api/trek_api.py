"""All Routing for the API routes."""
import fastapi

router = fastapi.APIRouter()


@router.get("/api/trek/{series}")
def trek(series: str):
    """Placeholder for the api routes."""
    return {"message": "API Inititialized."}
