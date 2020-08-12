quantity = int(input())
days = int(input())

price_ornament_set = 2
price_tree_skirt = 5
price_tree_garlands = 3
price_tree_lights = 15

total_spirit = 0
total_cost = 0
for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_spirit += 5
        total_cost += quantity * price_ornament_set
    if i % 3 == 0:
        if quantity % 2 == 0:
            total_cost += quantity * price_tree_skirt + quantity * price_tree_garlands
            total_spirit += 43
        else:
            total_cost += quantity * price_tree_skirt + quantity * price_tree_garlands
        total_spirit += 13
    if i % 5 == 0:
        total_cost += quantity * price_tree_lights
        total_spirit += 17
    if i % 10 == 0:
        total_cost += quantity * price_tree_lights + quantity * price_tree_garlands + quantity * price_tree_skirt
        total_spirit -= 20

    if i % 10 == 0:
        total_spirit -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')
