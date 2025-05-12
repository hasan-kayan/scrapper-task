from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scraper.campground_scraper import fetch_and_store

def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(fetch_and_store, 'cron', hour="*/6", args=[[-124.7, 24.4, -66.9, 49.4]])
    scheduler.start()
