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

items = input().split("|")
budget = float(input())
initial_budget = budget

bought_items = []

for item in items:
    name, price = item.split("->")
    price = float(price)
    if budget - price >= 0:
        if (name == "Clothes" and (price <= 50.00)) or \
                (name == "Shoes" and (price <= 35.00)) or \
                (name == "Accessories" and (price <= 20.50)):
            budget -= price
            bought_items += [price * 1.4]

total = (budget + sum(bought_items))
profit = (total - initial_budget)

for item in bought_items:
    print(f"{item:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if total >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
