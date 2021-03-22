toy = 5
pullover = 15
command = " "
number_of_adults = 0
number_of_kids = 0

while command != "Christmas":
    command = input()
    if command == "Christmas":
        break
    else:
        age = int(command)
    if age <= 16:
        number_of_kids += 1
    else:
        number_of_adults += 1
money_for_toys = number_of_kids * toy
money_for_pullover = number_of_adults * pullover

print(f'Number of adults: {number_of_adults}')
print(f'Number of kids: {number_of_kids}')
print(f'Money for toys: {money_for_toys}')
print(f'Money for sweaters: {money_for_pullover}')
