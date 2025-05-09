# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/campground_db")
API_BASE_URL = os.getenv("API_BASE_URL", "https://thedyrt.com/api/v5/campgrounds/search")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
