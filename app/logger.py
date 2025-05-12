import logging
from app.config import settings
"""
Logger configuration for the campground scraper application.
This module sets up the logging configuration for the application.
It uses the standard logging library to log messages to the console.
"""
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("campground_scraper")
