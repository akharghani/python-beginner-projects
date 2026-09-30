# Fuel Calculator

A beginner Python program from an intro course (Fall 2025). It asks about a road trip and works out fuel consumption and total fuel cost.

The main program (`main.py`) handles input and output, and the calculations live in a separate helper file (`trip_calculations.py`).

## How to run

```
python main.py
```

Then follow the prompts.

## Example

```
Enter trip distance in kilometres: 250
Enter number of fuel stops: 2
Enter litres purchased at stop #1: 10
Enter litres purchased at stop #2: 8.5
Enter fuel price per litre: 1.45

Trip Summary
-----------------------------------------
Total distance: 250.0 km
Total fuel used: 18.50 L
Fuel consumption: 7.40 L/100 km
Total fuel cost: $26.82
```

The program stops with an error message if the distance, number of stops, or total fuel is 0 or less.

## Planning

I wrote the pseudocode and drew a flowchart before coding.

[View the flowchart (PDF)](./Fuel%20Calculator%20Flowchart.pdf)

<details>
<summary>Show pseudocode</summary>

```text
BEGIN

PRINT "Trip Mileage / Fuel Efficiency Calculator"

INPUT distance_km

IF distance_km <= 0 THEN
    PRINT "ERROR: Distance must be greater than 0."
    STOP
END IF

INPUT num_stops

SET total_litres to 0

FOR stop_index FROM 1 TO num_stops DO
    INPUT litres_for_stop
    total_litres = total_litres + litres_for_stop
END FOR

IF total_litres <= 0 THEN
    PRINT "ERROR: Total fuel used must be greater than 0."
    STOP
END IF

INPUT price_per_litre

fuel_consumption = (total_litres / distance_km) * 100
total_cost = total_litres * price_per_litre

PRINT "Trip distance (km):", distance_km
PRINT "Total fuel used (L):", total_litres
PRINT "Fuel consumption (L/100 km):", fuel_consumption
PRINT "Total fuel cost ($):", total_cost

END
```

</details>
