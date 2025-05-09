# main.py

from fastapi import FastAPI
from api.routes import router as api_router
from app.database import Base, engine
from app.logger import logger
from app.scheduller import start_scheduler

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Campground Scraper",
    description="Scrapes campground data from The Dyrt",
    version="1.0.0"
)

# API route'larını bağla
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    logger.info("Application started.")
    start_scheduler()
