from fastapi import FastAPI
from scraper.campground_scraper import fetch_and_store

app = FastAPI()

@app.post("/scrape")
async def trigger_scraper():
    await fetch_and_store([-124.7, 24.4, -66.9, 49.4])
    return {"status": "started"}
