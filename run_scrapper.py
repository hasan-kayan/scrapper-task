# run_scrapper.py

import asyncio
from scrapper.processor import scrape_all_bounds
from app.logger import logger

if __name__ == "__main__":
    logger.info("Running scraper manually...")
    asyncio.run(scrape_all_bounds())
