# app/scheduller.py  → önerilen: app/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from scrapper.processor import scrape_all_bounds

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_all_bounds, "interval", hours=12)
    scheduler.start()
