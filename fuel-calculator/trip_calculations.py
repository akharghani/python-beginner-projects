"""
Helper functions for the Fuel Trip Calculator.
"""

def calculate_total_fuel(litres_list):
    """
    Accepts a list of fuel amounts in litres
    and returns the total litres used.
    """
    return sum(litres_list)

def calculate_fuel_consumption_l_per_100km(total_litres, distance_km):
    """
    Calculates fuel consumption in litres per 100 km.
    Formula: (total_litres / distance_km) * 100
    """
    return (total_litres / distance_km) * 100

def calculate_total_cost(total_litres, price_per_litre):
    """
    Calculates total fuel cost.
    """
    return total_litres * price_per_litre
