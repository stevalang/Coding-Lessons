budget = int(input())
season = input()
fishermen_count = int(input())

price = 0
ship_spring = 3000
ship_summer_autumn = 4200
ship_winter = 2600

if fishermen_count <= 6:
    if season == 'Spring':
        price = ship_spring * 0.9
    elif season == 'Autumn' or season == 'Summer':
        price = ship_summer_autumn * 0.9
    else:
        price = ship_winter * 0.9
elif fishermen_count <= 11:
    if season == 'Spring':
        price = ship_spring * 0.85
    elif season == 'Autumn' or season == 'Summer':
        price = ship_summer_autumn * 0.85
    else:
        price = ship_winter * 0.85
else:
    if season == 'Spring':
        price = ship_spring * 0.75
    elif season == 'Autumn' or season == 'Summer':
        price = ship_summer_autumn * 0.75
    else:
        price = ship_winter * 0.75

if fishermen_count % 2 == 0 and season != 'Autumn':
    price *= 0.95
else:
    price = price

difference = abs(budget - price)

if budget >= price:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')
