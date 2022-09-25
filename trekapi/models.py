"""Define the database Models."""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Series(Base):
    """Define the Series Model.

    This contains the individual `Series` Metadata.
    """

    __tablename__ = "series"
    id = Column(Integer, primary_key=True, index=True)
    series_number = Column(Integer)
    name = Column(String)
    url = Column(String)
    season_count = Column(Integer)
    episode_count = Column(Integer)
    episodes_url = Column(String)
    dates = Column(String)
    logo = Column(String)
