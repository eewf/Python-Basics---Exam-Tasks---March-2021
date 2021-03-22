from math import ceil
distance = 384400
time_to_stay = 3
speed = float(input())
needed_fuel_per_100km = float(input())

trip_km = distance * 2
trip_time = trip_km / speed + time_to_stay
trip_fuel = needed_fuel_per_100km * trip_km / 100

print(f'{ceil(trip_time)}')
print(f'{ceil(trip_fuel)}')
