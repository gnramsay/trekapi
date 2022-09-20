"""Main API file."""
from fastapi import FastAPI

from views import home

api = FastAPI(
    title="TrekAPI",
    description="An API to access Star Trek(tm) Episode data.",
    version="0.1.0",
)

api.include_router(home.router)
