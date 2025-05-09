# services/revers_geocode.py

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="campground_scraper")

def get_address_from_coords(lat: float, lon: float) -> str:
    location = geolocator.reverse((lat, lon), exactly_one=True)
    return location.address if location else ""
