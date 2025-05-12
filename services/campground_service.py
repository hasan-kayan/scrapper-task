from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.campground_model import CampgroundDB
from models.campground_model import Campground

def pydantic_to_db_data(cg: Campground) -> dict:
    """
    Converts a Pydantic Campground model instance to a dictionary suitable for database storage.

    Args:
        cg (Campground): An instance of the Campground Pydantic model.

    Returns:
        dict: A dictionary representation of the Campground instance with specific fields excluded 
              and using Python attribute names instead of aliases.

    Notes:
        - The following fields are excluded from the resulting dictionary:
          "links", "photo_urls", "camper_types", "accommodation_type_names".
        - The `by_alias` parameter is set to False, ensuring that Python attribute names are used 
          instead of any defined aliases.
    """
    return cg.dict(
        by_alias=False,  
        exclude={"links", "photo_urls", "camper_types", "accommodation_type_names"}
    )
async def upsert_campground(session: AsyncSession, cg: Campground):
    """
    Inserts or updates a campground record in the database.

    If a campground with the given ID exists in the database, its fields are updated
    with the provided data. Otherwise, a new campground record is created and added
    to the database.

    Args:
        session (AsyncSession): The SQLAlchemy asynchronous session used for database operations.
        cg (Campground): The Pydantic model containing campground data to be inserted or updated.

    Returns:
        None
    """
    data = pydantic_to_db_data(cg)
    existing = await session.get(CampgroundDB, cg.id)

    if existing:
        for key, value in data.items():
            setattr(existing, key, value)
    else:
        new_cg = CampgroundDB(**data)
        session.add(new_cg)

    await session.commit()


