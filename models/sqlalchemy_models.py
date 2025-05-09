# models/sqlalchemy_models.py

from sqlalchemy import Column, String, Float, Integer, DateTime, Boolean
from app.database import Base

class Campground(Base):
    __tablename__ = "campgrounds"

    id = Column(String, primary_key=True, index=True)
    type = Column(String)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    region_name = Column(String)
    administrative_area = Column(String)
    nearest_city_name = Column(String)
    accommodation_type_names = Column(String)  # comma-separated list
    bookable = Column(Boolean)
    camper_types = Column(String)  # comma-separated list
    operator = Column(String)
    photo_url = Column(String)
    photo_urls = Column(String)  # comma-separated list
    photos_count = Column(Integer)
    rating = Column(Float)
    reviews_count = Column(Integer)
    slug = Column(String)
    price_low = Column(Float)
    price_high = Column(Float)
    availability_updated_at = Column(DateTime)
