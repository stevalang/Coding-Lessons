from collections import defaultdict

stocks = defaultdict(int)

print()
while True:
    command = input()
    if command == "statistics":
        break
    product, quantity = command.split(": ")
    if product in stocks:
        stocks[product] += int(quantity)
    else:
        stocks[product] = int(quantity)

print(f"Products in stock:")
for product, quantity in stocks.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(stocks.keys())}")
print(f'Total Quantity: {sum(stocks.values())}')
