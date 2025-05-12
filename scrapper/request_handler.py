# scrapper/request_handler.py

import httpx
import asyncio
from typing import Optional
from app.config import (
    API_BASE_URL,
    DEFAULT_START_DATE,
    DEFAULT_END_DATE,
    DEFAULT_SORT,
    DEFAULT_PAGE_SIZE
)
from app.logger import logger
from app.config import API_BASE_URL
print("🎯 DEBUG API_BASE_URL:", API_BASE_URL)
import os
print("🌍 ENV VALUE OF API_BASE_URL:", os.getenv("API_BASE_URL"))

MAX_RETRIES = 3
TIMEOUT = 10

async def fetch_bounds_data(
    bbox: str,
    start_date: Optional[str] = DEFAULT_START_DATE,
    end_date: Optional[str] = DEFAULT_END_DATE,
    sort_by: str = DEFAULT_SORT,
    page: int = 1,
    page_size: int = DEFAULT_PAGE_SIZE
) -> dict:
    """
    Fetch campground data for a given bounding box with optional filters.
    """

    logger.debug(f"✅ ACTUAL API_BASE_URL USED: {API_BASE_URL}")

    params = {
        "filter[search][drive_time]": "any",
        "filter[search][air_quality]": "any",
        "filter[search][electric_amperage]": "any",
        "filter[search][max_vehicle_length]": "any",
        "filter[search][price]": "any",
        "filter[search][rating]": "any",
        "filter[search][bbox]": bbox,
        "sort": sort_by,
        "page[number]": page,
        "page[size]": page_size
    }

    if start_date:
        params["filter[search][start_date]"] = start_date
    if end_date:
        params["filter[search][end_date]"] = end_date

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with httpx.AsyncClient(timeout=TIMEOUT) as client:
                response = await client.get(API_BASE_URL, params=params)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            logger.warning(f"[Attempt {attempt}] HTTP error: {e}")
            await asyncio.sleep(2)
        except Exception as e:
            logger.error(f"Unexpected error on attempt {attempt}: {e}")
            break

    return {}
