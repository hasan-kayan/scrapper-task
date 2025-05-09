# scrapper/bound_generator.py

def generate_bounds():
    bounds = []
    for lat in range(24, 50):      # 24 to 49
        for lon in range(-125, -66):  # -125 to -67
            bounds_str = f"{lat},{lon},{lat+1},{lon+1}"
            bounds.append(bounds_str)
    return bounds
