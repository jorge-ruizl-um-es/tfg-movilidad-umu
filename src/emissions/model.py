def estimate_emissions(mode, distance_km):
    emissions_factors = {
        'coche': 0.12,       # kg CO₂/km
        'bus': 0.06,
        'bici': 0.0,
        'a pie': 0.0
    }
    if mode not in emissions_factors or distance_km is None:
        return None
    return round(emissions_factors[mode] * distance_km, 3)
