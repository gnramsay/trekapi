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
    series_number = Column(Integer, unique=True)
    name = Column(String)
    url = Column(String)
    season_count = Column(Integer)
    episode_count = Column(Integer)
    episodes_url = Column(String)
    dates = Column(String)
    logo = Column(String)

    seasons = relationship("Season", back_populates="series")


class Season(Base):
    """Define the Season Model."""

    __tablename__ = "season"
    id = Column(Integer, primary_key=True, index=True)
    season_number = Column(Integer)
    total_episodes = Column(Integer)
    season_start = Column(String)
    season_end = Column(String)

    series_id = Column(Integer, ForeignKey("series.id"))
    series = relationship("Series", back_populates="seasons")
