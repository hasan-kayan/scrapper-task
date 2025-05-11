from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.routes import router as api_router
from app.database import Base, engine
from app.logger import logger
from app.scheduller import start_scheduler


# Yeni lifespan yapısı
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application started.")
    start_scheduler()
    yield
    logger.info("Application shutting down...")


app = FastAPI(
    title="Campground Scraper",
    description="Scrapes campground data from The Dyrt",
    version="1.0.0",
    lifespan=lifespan
)

# Veritabanı tabloları oluşturuluyor
Base.metadata.create_all(bind=engine)

# API router ekle
app.include_router(api_router)
