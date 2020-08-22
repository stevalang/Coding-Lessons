from operator import index

inventory = input().split(", ")
line = input()
while line != 'Craft!':
    commands = line.split(" - ")
    command = commands[0]
    item = commands[1]
    if command == 'Craft':
        break
    if command == "Collect":
        if item in inventory:
            pass
        else:
            inventory.append(item)
    elif command == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif command == 'Combine Items':
        items = item.split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index + 1, new_item)
    elif command == 'Renew':
        if item in inventory:
            index_item = inventory.index(item)
            a = inventory.pop(index_item)
            inventory.append(a)
    line = input()

print(', '.join(inventory))
