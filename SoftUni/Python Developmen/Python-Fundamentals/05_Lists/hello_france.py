"""

The budget was enough to get them to Frankfurt and they have some money left, but their final aim is to go to France, which means that they will need more finances. They’ve decided to make profit by buying items on discount from the Thrift Shop and selling them for a higher price. You must help them.
Create a program that calculates the profit after buying some items and selling them on a higher price. In order to fulfil that, you are going to need certain data - you will receive a collection of items and a budget in the following format:
{type->price|type->price|type->price……|type->price}
{budget}
The prices for each of the types cannot exceed a certain price, which is given bellow:

If a price for a certain item is higher than the maximum price, don’t buy it. Every time you buy an item, you have to reduce the budget with the value of its price. If you don’t have enough money for it, you can’t buy it. Buy as much items as you can.
You have to increase the price of each of the items you have successfully bought with 40%. Print the list with the new prices and the profit you will gain from selling the items. They need exactly 150$ for tickets for the train, so if their budget after selling the products is enough – print – "Hello, France!" and if not – "Time to go."
Input / Constraints
On the 1st line you are going to receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]
On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
Output
Print the list with the bought item’s new prices, rounded 2 digits after the decimal separator in the following format:
"{price1} {price2} {price3} {price5}………{priceN}"
Print the profit, rounded 2 digits after the decimal separator in the following format:
"Profit: {profit}"
If the money for tickets are enough, print: "Hello, France!" and if not – "Time to go."

"""


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
