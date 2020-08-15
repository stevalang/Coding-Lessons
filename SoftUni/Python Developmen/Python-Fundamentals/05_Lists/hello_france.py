# {type->price|type-> price|type->price……|type->price}
# {budget}
import math
items = input().split('|')
initial_budget = int(input())
budget = initial_budget
new_list = []
profit_total = 0

for item in items:
    # name, price = item.split("->")
    args = item.split("->")
    item_type = args[0]
    item_price = float(args[1])
    if budget - item_price >= 0:
        if item_type == 'Clothes' and item_price <= 50:
            budget -= item_price
            profit = item_price * 0.4
            profit_total += profit
            new_item_price = item_price + profit
            new_list.append(new_item_price)
        if item_type == 'Shoes' and item_price <= 35:
            budget -= item_price
            profit = item_price * 0.4
            profit_total += profit
            new_item_price = item_price + profit
            new_list.append(new_item_price)
        if item_type == 'Accessories' and item_price <= 20.50:
            budget -= item_price
            profit = item_price * 0.4
            profit_total += profit
            new_item_price = item_price + profit
            new_list.append(new_item_price)

total = (budget + sum(new_list))
profit = (total - initial_budget)
for item in new_list:
    print(f"{item:.2f}", end=" ")
print()
print(f'Profit: {profit:.2f}')

if total >= 150:
    print(f'Hello, France!')
else:
    print("Time to go.")

# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120