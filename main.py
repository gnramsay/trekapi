"""Main API file."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from views import home

api = FastAPI(
    title="TrekAPI",
    description="An API to access Star Trek(tm) Episode data.",
    version="0.1.0",
)

api.mount("/static", StaticFiles(directory="static"), name="static")
api.include_router(home.router)
