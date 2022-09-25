"""Define Schemas used in the API."""

from pydantic import BaseModel, Field, HttpUrl


class Series(BaseModel):
    """Define the Series Schema."""

    series_number: int = Field(
        description="Number of this Series, starting at 1 for TOS."
    )
    name: str = Field(description="Standard name of this Series.")
    url: HttpUrl = Field(
        description="URL for the main Wikipedia page of this Series."
    )
    season_count: int = Field(
        description="Number of full seasons in this Series."
    )
    episode_count: int = Field(
        description="Total Number of episodes in this Series (all Seasons)."
    )
    episodes_url: HttpUrl = Field(
        description="URL for the Episode data on Wikipedia of this Series."
    )
    dates: str = Field(
        description="Start and end dates of this Series, Text format."
    )
    logo: HttpUrl = Field(description="URL for the Logo of this Series.")

    class Config:
        """Set this as ORM compatible and add example data."""

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


class Season(BaseModel):
    """Define the Season schema."""

    season_number: int = Field(
        title="Season Number",
        description="Number of Season within it's parent Season.",
    )
    total_episodes: int
    season_start: str
    season_end: str

    class Config:
        """Set this as ORM compatible and add example data."""

        orm_mode = True
        schema_extra = {
            "example": {
                "total_episodes": 20,
                "season_start": "January 3, 1993",
                "season_end": "June 20, 1993",
            }
        }
