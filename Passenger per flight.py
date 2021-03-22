import sys
from math import floor

airlines = int(input())
most_passangers = -sys.maxsize
company_with_most_passengers = 0
average_passangers = 0

for company_name in range(airlines):
    name = input()
    total_flights = 0
    total_passangers = 0
    while name != "Finish":
        command = input()
        if command == "Finish":
            break
        else:
            passangers = int(command)
        total_passangers += passangers
        total_flights += 1
        average_passangers = total_passangers / total_flights
    if average_passangers > most_passangers:
        most_passangers = average_passangers
        company_with_most_passengers = name

    print(f'{name}: {floor(average_passangers)} passengers.')
print(f'{company_with_most_passengers} has most passengers per flight: {floor(most_passangers)}')
