# api/routes.py

from fastapi import APIRouter
from scrapper.processor import scrape_all_bounds

router = APIRouter()

@router.post("/start-scraper")
async def start_scraper():
    await scrape_all_bounds()
    return {"message": "Scraper started successfully"}
