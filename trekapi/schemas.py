"""Define Schemas used in the API."""
from pydantic import BaseModel


class Series(BaseModel):
    """Define the Series Schema."""

    series_number: int
    name: str
    url: str
    season_count: int
    episode_count: int
    episodes_url: str
    dates: str
    logo: str

    class Config:
        """Set this as ORM compatible."""

        orm_mode = True
