# scrapper/bound_generator.py

from typing import List

def generate_bounds(country: str = "usa") -> List[str]:
    """
    Generate bounding boxes for a given country. Returns a list of bbox strings.
    """
    country_bounds = {
        "usa": (-125, 24, -66, 49),       # (sw_lng, sw_lat, ne_lng, ne_lat)
        "turkey": (25, 35.8, 45, 42.1)
        # Diğer ülkeleri buraya ekleyebilirsin
    }

    if country not in country_bounds:
        raise ValueError(f"Unknown country: {country}")

    sw_lng, sw_lat, ne_lng, ne_lat = country_bounds[country]

    # Örnek grid mantığı: 1x1 derece böl
    step = 1.0
    bounds = []

    lat = sw_lat
    while lat < ne_lat:
        lng = sw_lng
        while lng < ne_lng:
            bounds.append(f"{lng},{lat},{lng + step},{lat + step}")
            lng += step
        lat += step

    return bounds
