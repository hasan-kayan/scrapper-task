import httpx
from app.config import settings
from app.logger import logger
from models.campground_model import Campground
from services.campground_service import upsert_campground
from app.db import get_session
from tenacity import retry, wait_fixed, stop_after_attempt

@retry(wait=wait_fixed(3), stop=stop_after_attempt(3))
async def fetch_data(client, params):
    """
    Fetch data asynchronously from the API.

    This function sends a GET request to the API endpoint specified in the settings
    with the provided query parameters and a timeout.

    Args:
        client (httpx.AsyncClient): The HTTP client used to make the request.
        params (dict): A dictionary of query parameters to include in the request.

    Returns:
        httpx.Response: The response object returned by the API.

    Raises:
        httpx.RequestError: If an error occurs while making the request.
        httpx.HTTPStatusError: If the response contains an HTTP error status.
    """
    return await client.get(settings.API_BASE_URL, params=params, timeout=30.0)

async def fetch_and_store(bounds):
    """
    Fetches data from an API within the specified geographical bounds and stores it in the database.

    This function sends an asynchronous HTTP request to fetch data based on the provided bounding box
    coordinates. The data is then enriched with default values for missing fields, parsed into a 
    `Campground` object, and upserted into the database.

    Args:
        bounds (list): A list of four float values representing the bounding box coordinates 
                       [min_longitude, min_latitude, max_longitude, max_latitude].

    Raises:
        httpx.HTTPStatusError: If the HTTP request returns a non-successful status code.
        httpx.ReadTimeout: If the HTTP request times out.

    Logs:
        - Logs successful storage of campground data.
        - Logs errors during parsing or storing of individual items.
        - Logs HTTP errors or timeouts during the API request.
    """
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
