def get_item_cost(hero, item):
    return items_cost[hero][item]


def get_inventory_cost(hero, inventory):
    return sum([get_item_cost(hero, item) for item in inventory])


heroes = input().split(', ')


heroes_inventory = \
    {hero_name: set() for hero_name in heroes}
items_cost = {hero_name: {} for hero_name in heroes}

while True:
    command = input()
    if command == 'End':
        break

    hero, item, cost = command.split('-')
    cost = int(cost)

    heroes_inventory[hero].add(item)
    if item not in items_cost[hero].keys():
        items_cost[hero][item] = cost

[print(f"{hero_name} -> Items: {len(hero_inventory)}, Cost: {get_inventory_cost(hero_name, hero_inventory)}")
 for hero_name, hero_inventory in heroes_inventory.items()]
