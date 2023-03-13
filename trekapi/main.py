"""Main API file."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from trekapi import models
from trekapi.api import trek_api
from trekapi.database import engine
from trekapi.views import home

api = FastAPI(
    title="TrekAPI",
    description="An API to access Star Trek(tm) Episode data.",
    version="0.1.0",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    redoc_url=None,
    contact={
        "Developer name": "Grant Ramsay",
        "website": "https://www.gnramsay.com",
        "email": "grant@gnramsay.com",
    },
)

api.mount("/static", StaticFiles(directory="static"), name="static")
api.include_router(home.router)
api.include_router(trek_api.router)

models.Base.metadata.create_all(engine)
