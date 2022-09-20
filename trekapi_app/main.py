"""Main API file."""
from fastapi import FastAPI

api = FastAPI(
    title="TrekAPI",
    description="An API to access Star Trek(tm) Episode data.",
    version="0.1.0",
)


@api.get("/", name="root_path")
def root():
    """Define the Root path."""
    return {"message": "FastAPI initialized."}
