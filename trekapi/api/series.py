"""Route definitions for the 'Series' Model."""

from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from trekapi import models, schemas
from trekapi.database import get_db

router = APIRouter(prefix="/series")


@router.get(
    "/{series_number}",
    response_model=schemas.Series,
    name="get_specific_series_data",
)
def get_one_series(series_number: str, db: Session = Depends(get_db)):
    """Return data for a specific series."""
    series_data = (
        db.query(models.Series)
        .filter(models.Series.series_number == series_number)
        .first()
    )
    if not series_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Series {series_number} is not in the database.",
        )
    return series_data


@router.get("/", response_model=List[schemas.Series])
def get_all_series(db: Session = Depends(get_db)):
    """Return a list of all Series in the database."""
    series = db.query(models.Series).all()
    return series


@router.post("/", response_model=schemas.Series)
def add_new_series(request: schemas.Series, db: Session = Depends(get_db)):
    """Add a new Series to the database.

    Note this is just the Series metadata, not season or episode data.
    """

    # make sure this series number is not alrady used.
    check_series = (
        db.query(models.Series)
        .filter(models.Series.series_number == request.series_number)
        .first()
    )

    if check_series:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                f"Series {request.series_number} "
                f"already exists ({request.name})."
            ),
        )

    # we're good so create the new one.
    new_series = models.Series(
        series_number=request.series_number,
        name=request.name,
        url=request.url,
        season_count=request.season_count,
        episode_count=request.episode_count,
        episodes_url=request.episodes_url,
        dates=request.dates,
        logo=request.logo,
    )
    db.add(new_series)
    db.commit()
    db.refresh(new_series)

    return new_series
