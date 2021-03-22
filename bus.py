passengers = int(input())
stops = int(input())
total_passengers = passengers

for stop in range(1, stops + 1):
    if stop % 2 == 1:
        total_passengers += 2
    elif stop % 2 == 0:
        total_passengers -= 2
    go_out = int(input())
    total_passengers -= go_out
    income = int(input())
    total_passengers += income

print(f'The final number of passengers is : {total_passengers}')