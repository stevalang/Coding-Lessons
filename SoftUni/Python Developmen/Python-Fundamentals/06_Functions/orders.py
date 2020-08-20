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
