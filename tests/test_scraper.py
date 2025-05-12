import pytest
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings
from models.campground import CampgroundDB
from scraper.campground_scraper import fetch_and_store

DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
engine = create_async_engine(DATABASE_URL, echo=False)
TestSession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@pytest.mark.asyncio
async def test_fetch_and_store():
    # Küçük bir alan kullanarak test edelim
    test_bounds = [-77.0, 38.8, -76.9, 38.9]
    
    await fetch_and_store(test_bounds)

    async with TestSession() as session:
        result = await session.execute(
            CampgroundDB.__table__.select().limit(1)
        )
        campground = result.fetchone()
        assert campground is not None, "Kamp alanı kaydedilmedi!"
