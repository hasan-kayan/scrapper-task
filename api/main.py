from fastapi import FastAPI
from scraper.campground_scraper import fetch_and_store

app = FastAPI()

@app.post("/scrape")
async def trigger_scraper():
    """
    Trigger the campground data scraper for the entire USA.

    This endpoint initiates a scraping task that fetches campground data from 
    the external API within the bounding box covering the continental United States.

    - **Method:** POST
    - **Response:** JSON indicating that the scraping has started.

    Returns:
        dict: A status message indicating the scraper was triggered.
    """
    await fetch_and_store([-124.7, 24.4, -66.9, 49.4])
    return {"status": "started"}
