import pytest
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings
from models.campground_model import CampgroundDB
from scraper.campground_scraper import fetch_and_store

DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
engine = create_async_engine(DATABASE_URL, echo=False)
TestSession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@pytest.mark.asyncio
async def test_fetch_and_store():
    """
    Test the `fetch_and_store` function to ensure it retrieves and stores campground data correctly.
    This test uses a small geographic bounding box to limit the scope of the data fetched.
    It then verifies that at least one campground record is successfully saved in the database.
    Steps:
    1. Define a small bounding box (`test_bounds`) for testing purposes.
    2. Call the `fetch_and_store` function with the test bounds.
    3. Query the database to check if at least one campground record exists.
    4. Assert that a campground record is present in the database.
    Raises:
        AssertionError: If no campground record is found in the database.
    """
    test_bounds = [-77.0, 38.8, -76.9, 38.9]
    
    await fetch_and_store(test_bounds)

    async with TestSession() as session:
        result = await session.execute(
            CampgroundDB.__table__.select().limit(1)
        )
        campground = result.fetchone()
        assert campground is not None, "Kamp alanı kaydedilmedi!"
