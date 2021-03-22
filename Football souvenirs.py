team = input()
souvenirs = input()
number_of_souvenirs = int(input())
price=0

if team == "Argentina":
    if souvenirs == "flags":
        price = 3.25
    elif souvenirs == "caps":
        price = 7.20
    elif souvenirs == "posters":
        price = 5.10
    elif souvenirs == "stickers":
        price = 1.25
    else:
        print('Invalid stock!')
        exit()
elif team == "Brazil":
    if souvenirs == "flags":
        price = 4.20
    elif souvenirs == "caps":
        price = 8.50
    elif souvenirs == "posters":
        price = 5.35
    elif souvenirs == "stickers":
        price = 1.20
    else:
        print('Invalid stock!')
        exit()
elif team == "Croatia":
    if souvenirs == "flags":
        price = 2.75
    elif souvenirs == "caps":
        price = 6.90
    elif souvenirs == "posters":
        price = 4.95
    elif souvenirs == "stickers":
        price = 1.10
    else:
        print('Invalid stock!')
        exit()
elif team == "Denmark":
    if souvenirs == "flags":
        price = 3.10
    elif souvenirs == "caps":
        price = 6.50
    elif souvenirs == "posters":
        price = 4.80
    elif souvenirs == "stickers":
        price = 0.9
    else:
        print('Invalid stock!')
        exit()
else:
    print('Invalid country!')
    exit()

total = price * number_of_souvenirs

print(f'Pepi bought {number_of_souvenirs} {souvenirs} of {team} for {total:.2f} lv.')