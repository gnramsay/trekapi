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
        schema_extra = {
            "example": {
                "series_number": 4,
                "name": "Deep Space Nine",
                "url": (
                    "https://en.wikipedia.org/wiki/Star_Trek"
                    ":_Deep_Space_Nine"
                ),
                "season_count": "7",
                "episode_count": "176",
                "episodes_url": (
                    "https://en.wikipedia.org/wiki/List_of_Star_Trek"
                    ":_Deep_Space_Nine_episodes"
                ),
                "dates": "January 4, 1993 - May 31, 1999",
                "logo": (
                    "https://upload.wikimedia.org/wikipedia/commons/thumb"
                    "/e/e7/Star_Trek_DS9_logo.svg/"
                    "220px-Star_Trek_DS9_logo.svg.png"
                ),
            }
        }
