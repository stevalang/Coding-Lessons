"""
You've done all the work and the last thing left to accomplish is to own a legendary item. However, it's a tedious process and it requires quite a bit of farming. Anyway, you are not too pretentious – any legendary item will do. The possible items are:
Shadowmourne – requires 250 Shards;
Valanyr – requires 250 Fragments;
Dragonwrath – requires 250 Motes;
Shards, Fragments and Motes are the key materials and everything else is junk. You will be given lines of input, in the format: 
2 motes 3 ores 15 stones
Keep track of the key materials - the first one that reaches the 250 mark, wins the race. At that point you have to print that the corresponding legendary item is obtained. Then, print the remaining shards, fragments, motes, ordered by quantity in descending order, then by name in ascending order, each on a new line. Finally, print the collected junk items in alphabetical order.
Input
Each line comes in the following format: {quantity} {material} {quantity} {material} … {quantity} {material}
Output
On the first line, print the obtained item in the format: {Legendary item} obtained!
On the next three lines, print the remaining key materials in descending order by quantity
If two key materials have the same quantity, print them in alphabetical order
On the final several lines, print the junk items in alphabetical order
All materials are printed in format {material}: {quantity}
The output should be lowercase, except for the first letter of the legendary
"""


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
