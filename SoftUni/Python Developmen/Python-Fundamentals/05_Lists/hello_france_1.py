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