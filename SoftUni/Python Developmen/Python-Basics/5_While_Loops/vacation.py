trip_cost = float(input())
money_owned = float(input())
day_count = 0
days_money_spent = 0
while True:
    action = input()
    money = float(input())
    if action == 'save':
        money_owned += money
        days_money_spent = 0
    else:
        days_money_spent += 1
        money_owned -= money
        if money_owned < 0:
            money_owned = 0
    day_count += 1

    if days_money_spent == 5:
        print(f"You can't save the money.")
        print(f"{day_count}")
        break
    if money_owned >= trip_cost:
        print(f'You saved the money for {day_count} days.')
        break
