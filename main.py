import asyncio
from scraper.campground_scraper import fetch_and_store

async def main():
    bounds_list = [
        [-124.7, 24.4, -66.9, 49.4],  # USA bounding box
        # Parçalara ayırabilirsin grid'e
    ]
    await asyncio.gather(*(fetch_and_store(bounds) for bounds in bounds_list))

if __name__ == "__main__":
    asyncio.run(main())
