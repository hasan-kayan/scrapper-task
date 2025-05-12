import json
from typing import List
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "bounds_config.json"

def load_bounds_config() -> dict:
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def generate_bounds(country: str = "usa") -> List[str]:
    """
    Generate bounding boxes for a given country using config JSON.
    """
    config = load_bounds_config()

    if country not in config:
        raise ValueError(f"Unknown country: {country}")

    sw_lng, sw_lat = config[country]["sw"]
    ne_lng, ne_lat = config[country]["ne"]
    step = config[country].get("step", 1.0)

    bounds = []
    lat = sw_lat
    while lat < ne_lat:
        lng = sw_lng
        while lng < ne_lng:
            bounds.append(f"{lng},{lat},{lng + step},{lat + step}")
            lng += step
        lat += step

    return bounds
