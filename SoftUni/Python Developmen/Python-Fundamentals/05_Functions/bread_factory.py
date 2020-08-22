events = input().split('|')
energy = 100
coins = 100
is_closed = False
for event in events:
    args = event.split('-')
    event_ingredient = args[0]
    number = int(args[1])

    if event_ingredient == 'rest':
        temp = 0
        if energy + number <= 100:
            temp = number
            energy += number
        else:
            temp = int(100 - energy)
            energy = 100
        print(f'You gained {temp} energy.')
        print(f'Current energy: {energy}.')

    elif event_ingredient == 'order':
        if energy >= 30:
            energy -= 30
            coins += number
            print(f'You earned {number} coins.')
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins-number <= 0:
            is_closed = True
            break
        else:
            coins -= number
            print(f'You bought {event_ingredient}.')


if is_closed:
    print(f'Closed! Cannot afford {event_ingredient}.')
else:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')