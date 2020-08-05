
'''
Conditional Statements - Lab
Check: https://judge.softuni.bg/Contests/Practice/Index/1012#0
12. Toy Shop
Condition:
Petya has a toy store. She receives a large order that she must fulfill. With the money he will earn,
wants to go on a trip. Write a program that calculates the profit from the order.
Toy prices:
-Puzzle - BGN 2.60.
-Speaking doll - BGN 3.
- Teddy bear - BGN 4.10.
-Mignon - BGN 8.20.
-Truck - BGN 2
If the ordered toys are 50 or more, the store makes a 25% discount on the total price.
Petya has to give 10% of the earned money for the rent of the store.
To calculate whether the money will be enough for her to go on a trip.
Entrance
6 lines are read from the console:
1. Price of the trip - real number;
2. Number of puzzles - integer;
3. Number of talking dolls - integer;
4. Number of teddy bears - an integer;
5. Number of minions - an integer;
6. Number of trucks - an integer.
Exit
The following is printed on the console:
-If the money is enough it is printed:
- "Yes! {Remaining money} lv left."
-If the money is NOT enough, print:
- "Not enough money! {Lv needed} lv needed."
The result must be formatted to the second decimal place.
'''


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
