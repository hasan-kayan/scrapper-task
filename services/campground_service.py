from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.campground_model import CampgroundDB
from models.campground_model import Campground

def pydantic_to_db_data(cg: Campground) -> dict:
    return cg.dict(
        by_alias=False,  # 👈 Python adları kullanılır
        exclude={"links", "photo_urls", "camper_types", "accommodation_type_names"}
    )
async def upsert_campground(session: AsyncSession, cg: Campground):
    data = pydantic_to_db_data(cg)
    existing = await session.get(CampgroundDB, cg.id)

    if existing:
        for key, value in data.items():
            setattr(existing, key, value)
    else:
        new_cg = CampgroundDB(**data)
        session.add(new_cg)

    await session.commit()


