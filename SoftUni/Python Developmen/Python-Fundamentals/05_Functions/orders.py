"""
Write a function that calculates the total price of an order and prints it on the console. The function should receive one of the following products: coffee, coke, water, snacks; and a quantity of the product. The prices for a single piece of each product are: 
"""

def find_price_per_unit(product, quantity):
    if product == 'coffee':
        return 1.5 * quantity
    if product == 'water':
        return 1 * quantity
    if product == 'coke':
        return 1.4 * quantity
    if product == 'snacks':
        return 2.0 * quantity


print(f'{find_price_per_unit(input(), int(input())):.2f}')
