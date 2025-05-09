# scrapper/parser.py

from typing import List
from models.pydantic_models import Campground
from app.logger import logger

def parse_campgrounds(raw_data: dict) -> List[Campground]:
    campgrounds = []
    for item in raw_data.get("campgrounds", []):
        try:
            cg = Campground(**item)
            campgrounds.append(cg)
        except Exception as e:
            logger.warning(f"Validation failed: {e}")
    return campgrounds
