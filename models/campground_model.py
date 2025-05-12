# models/campground_model.py

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl
from sqlalchemy import Column, String, Float, Boolean, Integer, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy Base
Base = declarative_base()

class CampgroundDB(Base):
    """
    CampgroundDB is a SQLAlchemy model representing a campground entity in the database.

    Attributes:
        id (str): The unique identifier for the campground.
        type (str): The type of the campground.
        name (str): The name of the campground.
        latitude (float): The latitude coordinate of the campground.
        longitude (float): The longitude coordinate of the campground.
        region_name (str): The name of the region where the campground is located.
        administrative_area (str, optional): The administrative area of the campground (nullable).
        nearest_city_name (str, optional): The name of the nearest city to the campground (nullable).
        accommodation_type_names (JSON): A JSON object containing the types of accommodations available.
        bookable (bool): Indicates whether the campground is bookable.
        camper_types (JSON): A JSON object containing the types of campers allowed.
        operator (str, optional): The operator of the campground (nullable).
        photo_url (str, optional): The URL of the primary photo of the campground (nullable).
        photo_urls (JSON): A JSON object containing URLs of photos of the campground.
        photos_count (int): The total number of photos available for the campground.
        rating (float, optional): The average rating of the campground (nullable).
        reviews_count (int): The total number of reviews for the campground.
        slug (str, optional): A URL-friendly identifier for the campground (nullable).
        price_low (float, optional): The lowest price for the campground (nullable).
        price_high (float, optional): The highest price for the campground (nullable).
        availability_updated_at (datetime, optional): The timestamp of the last availability update (nullable).
    """
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
    """
    Campground model representing a camping site with various attributes.

    Attributes:
        id (str): Unique identifier for the campground.
        type (str): Type of the campground.
        links (CampgroundLinks): Links related to the campground.
        name (str): Name of the campground.
        latitude (float): Latitude coordinate of the campground.
        longitude (float): Longitude coordinate of the campground.
        region_name (str): Name of the region where the campground is located. 
            This field uses the alias "region-name".
        administrative_area (Optional[str]): Administrative area of the campground. 
            This field uses the alias "administrative-area".
        nearest_city_name (Optional[str]): Name of the nearest city to the campground. 
            This field uses the alias "nearest-city-name".
        accommodation_type_names (List[str]): List of accommodation types available at the campground. 
            This field uses the alias "accommodation-type-names".
        bookable (bool): Indicates whether the campground is bookable. Defaults to False.
        camper_types (List[str]): List of camper types supported by the campground. 
            This field uses the alias "camper-types".
        operator (Optional[str]): Operator or managing entity of the campground.
        photo_url (Optional[HttpUrl]): URL of the primary photo of the campground. 
            This field uses the alias "photo-url".
        photo_urls (List[HttpUrl]): List of URLs for photos of the campground. 
            This field uses the alias "photo-urls".
        photos_count (int): Number of photos available for the campground. 
            This field uses the alias "photos-count".
        rating (Optional[float]): Average rating of the campground.
        reviews_count (int): Number of reviews for the campground. 
            This field uses the alias "reviews-count".
        slug (Optional[str]): Slug for the campground, typically used in URLs.
        price_low (Optional[float]): Lowest price for the campground. 
            This field uses the alias "price-low".
        price_high (Optional[float]): Highest price for the campground. 
            This field uses the alias "price-high".
        availability_updated_at (Optional[datetime]): Timestamp of the last availability update. 
            This field uses the alias "availability-updated-at".
    """
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
