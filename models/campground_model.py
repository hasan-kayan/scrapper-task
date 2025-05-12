# models/campground_model.py

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl
from sqlalchemy import Column, String, Float, Boolean, Integer, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy Base
Base = declarative_base()

class CampgroundDB(Base):
    __tablename__ = "campgrounds"

    id = Column(String, primary_key=True)
    type = Column(String)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    region_name = Column(String)
    administrative_area = Column(String, nullable=True)
    nearest_city_name = Column(String, nullable=True)
    accommodation_type_names = Column(JSON)
    bookable = Column(Boolean)
    camper_types = Column(JSON)
    operator = Column(String, nullable=True)
    photo_url = Column(String, nullable=True)
    photo_urls = Column(JSON)
    photos_count = Column(Integer)
    rating = Column(Float, nullable=True)
    reviews_count = Column(Integer)
    slug = Column(String, nullable=True)
    price_low = Column(Float, nullable=True)
    price_high = Column(Float, nullable=True)
    availability_updated_at = Column(DateTime, nullable=True)


# ✅ Pydantic modeli
class CampgroundLinks(BaseModel):
    self: HttpUrl

class Campground(BaseModel):
    id: str
    type: str
    links: CampgroundLinks
    name: str
    latitude: float
    longitude: float
    region_name: str = Field(..., alias="region-name")
    administrative_area: Optional[str] = Field(None, alias="administrative-area")
    nearest_city_name: Optional[str] = Field(None, alias="nearest-city-name")
    accommodation_type_names: List[str] = Field([], alias="accommodation-type-names")
    bookable: bool = False
    camper_types: List[str] = Field([], alias="camper-types")
    operator: Optional[str] = None
    photo_url: Optional[HttpUrl] = Field(None, alias="photo-url")
    photo_urls: List[HttpUrl] = Field([], alias="photo-urls")
    photos_count: int = Field(0, alias="photos-count")
    rating: Optional[float] = None
    reviews_count: int = Field(0, alias="reviews-count")
    slug: Optional[str] = None
    price_low: Optional[float] = Field(None, alias="price-low")
    price_high: Optional[float] = Field(None, alias="price-high")
    availability_updated_at: Optional[datetime] = Field(None, alias="availability-updated-at")
