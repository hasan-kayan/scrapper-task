import httpx
from app.config import settings
from app.logger import logger
from models.campground_model import Campground
from services.campground_service import upsert_campground
from app.db import get_session
from tenacity import retry, wait_fixed, stop_after_attempt

@retry(wait=wait_fixed(3), stop=stop_after_attempt(3))
async def fetch_data(client, params):
    return await client.get(settings.API_BASE_URL, params=params, timeout=30.0)

async def fetch_and_store(bounds):
    params = {
        "filter[search][bbox]": ",".join(map(str, bounds)),
        "page[number]": 1,
        "page[size]": 500
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await fetch_data(client, params)
            res.raise_for_status()
            json_data = res.json()

            async for session in get_session():
                for item in json_data.get("data", []):
                    # 🔧 Eksik alanları boş/default değerlerle doldur
                    enriched = {
                        "id": item.get("id", ""),
                        "type": item.get("type", ""),
                        "links": item.get("links", {"self": "https://example.com"}),
                        "name": item.get("name", ""),
                        "latitude": item.get("latitude", 0.0),
                        "longitude": item.get("longitude", 0.0),
                        "region-name": item.get("region-name", ""),
                        "administrative-area": item.get("administrative-area"),
                        "nearest-city-name": item.get("nearest-city-name"),
                        "accommodation-type-names": item.get("accommodation-type-names", []),
                        "bookable": item.get("bookable", False),
                        "camper-types": item.get("camper-types", []),
                        "operator": item.get("operator"),
                        "photo-url": item.get("photo-url"),
                        "photo-urls": item.get("photo-urls", []),
                        "photos-count": item.get("photos-count", 0),
                        "rating": item.get("rating"),
                        "reviews-count": item.get("reviews-count", 0),
                        "slug": item.get("slug"),
                        "price-low": item.get("price-low"),
                        "price-high": item.get("price-high"),
                        "availability-updated-at": item.get("availability-updated-at"),
                    }

                    try:
                        cg = Campground.parse_obj(enriched)
                        await upsert_campground(session, cg)
                        logger.info(f"✅ Saved: {cg.name}")
                    except Exception as e:
                        logger.error(f"❌ Parse/store error [{item.get('id')}]: {e}")

    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e.response.status_code}")
    except httpx.ReadTimeout:
        logger.error("❌ Read timeout – API Not Responding.")
