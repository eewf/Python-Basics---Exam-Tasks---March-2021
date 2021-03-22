from math import floor

width = float(input())
length = float(input())
height = float(input())
average_high_of_astronauts = float(input())
needed_space_for_one = 2 * 2 * (average_high_of_astronauts + 0.4)
spacecraft = width * length * height
spacecraft_value = spacecraft // needed_space_for_one

if 3 <= spacecraft_value <= 10:
    print(f'The spacecraft holds {floor(spacecraft_value)} astronauts.')
elif spacecraft_value < 3:
    print(f'The spacecraft is too small.')
elif spacecraft_value > 10:
    print(f'The spacecraft is too big.')
