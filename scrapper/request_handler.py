# scrapper/request_handler.py

import httpx
import asyncio
from app.config import API_BASE_URL
from app.logger import logger

MAX_RETRIES = 3
TIMEOUT = 10

async def fetch_bounds_data(bounds: str) -> dict:
    url = f"{API_BASE_URL}?bounds={bounds}"
    for attempt in range(MAX_RETRIES):
        try:
            async with httpx.AsyncClient(timeout=TIMEOUT) as client:
                response = await client.get(url)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            logger.warning(f"[Attempt {attempt+1}] HTTP error: {e}")
            await asyncio.sleep(2)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            break
    return {}
