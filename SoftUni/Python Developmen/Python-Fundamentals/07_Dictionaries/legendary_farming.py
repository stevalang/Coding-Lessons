items = {'Shards': 'Shadowmourne', 'Valanyr': 'Fragments', 'Dragonwrath': 'Motes'}

inventory = {'Fragments': 255, 'Shards': 255, "Motes": 255}

print()

while inventory['Fragments'] > 0 or inventory['Shards'] > 0 or inventory['Motes'] > 0:
    data = input().capitalize().split()

    for i in range(0, len(data), 2):
        quantity = int(data[i])
        resource = data[i+1]

        if resource == "Shards" or resource == "Fragments" or resource == "Motes":
            inventory[resource] - int(quantity)


for resource in inventory:
    if inventory[resource] == 0:
        print(f'{items[resource]} obtained!')