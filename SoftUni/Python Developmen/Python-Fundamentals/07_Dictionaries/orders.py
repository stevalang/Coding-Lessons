from collections import defaultdict


def print_orders(dictionary1, dictionary2, template):
    for k,v in dictionary1.items():
        res = dictionary1[k] * dictionary2[k]
        print(template.format(k,res))


products_prices = defaultdict(float)
products_quantities = defaultdict(int)
while True:
    args = input().split(" ")
    if args[0] =='buy':
        break

    product = args[0]
    price = float(args[1])
    quantities = int(args[2])

    products_prices[product] = price
    products_quantities[product] += quantities

print_orders(products_prices, products_quantities, "{} -> {:.2f}")
