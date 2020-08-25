"""
Write a program that keeps information about products and their prices. Each product has a name, a price and a quantity. If the product doesn't exist yet, add it with its starting quantity.
If you receive a product, which already exists, increase its quantity by the input quantity and if its price is different, replace the price as well.
You will receive products' names, prices and quantities on new lines. Until you receive the command "buy", keep adding items. When you do receive the command "buy", print the items with their names and total price of all the products with that name. 
Input
Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
The product data is always delimited by a single space.
Output
Print information about each product in the following format:  "{productName} -> {totalPrice}"
Format the average grade to the 2nd digit after the decimal separator.
"""


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
