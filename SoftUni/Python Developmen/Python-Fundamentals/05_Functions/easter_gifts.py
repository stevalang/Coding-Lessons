gifts = [gift for gift in input().split(' ')]

while True:
    command = input()
    if command == "No Money":
        break
    command =[item for item in command.split()]
    if command[0] == 'OutOfStock':
        for gift in gifts:
            if gift == command[1]:
                index_to_change = gifts.index(gift)
                gifts.pop(index_to_change)
                gifts.insert(index_to_change, "None")
    elif command[0] == 'Required':
        if 0 <= int(command[2]) <= len(gifts) - 1:
            gifts.pop(int(command[2]))
            gifts.insert(int(command[2]), command[1])
    elif command[0] == 'JustInCase':
        gifts.pop(-1)
        gifts.append(command[1])

    print(" ".join([gift for gift in gifts if gift != "None"]))