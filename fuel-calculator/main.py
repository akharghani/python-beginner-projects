"""Fuel Trip Calculator: works out fuel consumption and cost for a road trip."""

from trip_calculations import (
    calculate_total_fuel,
    calculate_fuel_consumption_l_per_100km,
    calculate_total_cost,
)


def main():
    print("Trip Mileage / Fuel Efficiency Calculator")
    print("-----------------------------------------")

    # INPUT distance_km
    distance_km = float(input("Enter trip distance in kilometres: "))

    # IF distance_km <= 0 THEN
    if distance_km <= 0:
        print("ERROR: Distance must be greater than 0.")
        return

    # INPUT num_stops
    num_stops = int(input("Enter number of fuel stops: "))

    # Extra validation
    if num_stops <= 0:
        print("ERROR: Number of fuel stops must be at least 1.")
        return

    # LOOP to collect litres for each stop
    litres_list = []
    for stop_num in range(1, num_stops + 1):
        litres = float(input(f"Enter litres purchased at stop #{stop_num}: "))
        litres_list.append(litres)

    # Calculate total litres used
    total_litres = calculate_total_fuel(litres_list)

    # Edge case: total litres must be > 0
    if total_litres <= 0:
        print("ERROR: Total fuel must be greater than 0.")
        return

    # INPUT price per litre
    price_per_litre = float(
        input("Enter fuel price per litre: ")
    )

    # Calculate fuel consumption (L/100 km) using helper function
    fuel_consumption = calculate_fuel_consumption_l_per_100km(
        total_litres, distance_km
    )

    # Calculate total cost
    total_cost = calculate_total_cost(total_litres, price_per_litre)

    # Final output
    print("\nTrip Summary")
    print("-----------------------------------------")
    print(f"Total distance: {distance_km:.1f} km")
    print(f"Total fuel used: {total_litres:.2f} L")
    print(f"Fuel consumption: {fuel_consumption:.2f} L/100 km")
    print(f"Total fuel cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
