# scrapper/processor.py

from typing import List
from sqlalchemy.orm import Session
from app.database import SessionLocal
from models.sqlalchemy_models import Campground as DBCampground
from models.pydantic_models import Campground as PydanticCampground
from app.logger import logger
from scrapper.bound_generator import generate_bounds
from scrapper.request_handler import fetch_bounds_data
from scrapper.parser import parse_campgrounds
import asyncio


def save_to_db(campgrounds: List[PydanticCampground]):
    session: Session = SessionLocal()
    for cg in campgrounds:
        try:
            existing = session.query(DBCampground).filter_by(id=cg.id).first()
            data = cg.dict()
            data["accommodation_type_names"] = ",".join(cg.accommodation_type_names)
            data["camper_types"] = ",".join(cg.camper_types)
            data["photo_urls"] = ",".join([str(url) for url in cg.photo_urls])

            if existing:
                for key, value in data.items():
                    setattr(existing, key, value)
                logger.info(f"Updated campground: {cg.name}")
            else:
                new_entry = DBCampground(**data)
                session.add(new_entry)
                logger.info(f"Inserted new campground: {cg.name}")
            session.commit()
        except Exception as e:
            logger.error(f"Database error for {cg.name}: {e}")
            session.rollback()
    session.close()


async def scrape_all_bounds(
    country: str = "usa",
    start_date: str = None,
    end_date: str = None,
    **kwargs
):
    """
    Scrape campgrounds for all bounds in the specified country.
    """
    logger.info(f"Starting scrape for country: {country}")
    bounds_list = generate_bounds(country=country)

    for bounds in bounds_list:
        logger.debug(f"Fetching data for bounds: {bounds}")
        raw_data = await fetch_bounds_data(
            bbox=bounds,
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

        if raw_data.get("data"):
            campgrounds = parse_campgrounds(raw_data)
            save_to_db(campgrounds)
        else:
            logger.warning(f"No data received for bounds: {bounds}")
