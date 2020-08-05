trip = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.1
minion_price = 8.2
truck_price = 2

puzzle_money = puzzle_count * puzzle_price
doll_money = doll_count * doll_price
teddy_bear_money = teddy_bear_count * teddy_bear_price
minion_money = minion_count * minion_price
truck_money = truck_count * truck_price

total_money = puzzle_money + doll_money + teddy_bear_money + minion_money + truck_money
total_toys = puzzle_count + doll_count + teddy_bear_count + minion_count + truck_count

if total_toys < 50:
    total_money = total_money
else:
    total_money = total_money * 0.75

rent = total_money/10
profit = total_money - rent

if profit >= trip:
    print(f'Yes! {(profit - trip):.2f} lv left.')
else:
    print(f'Not enough money! {trip - profit:.2f} lv needed.')
