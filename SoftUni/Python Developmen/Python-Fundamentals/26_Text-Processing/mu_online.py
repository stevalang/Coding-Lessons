rooms = input().split("|")

health = 100
bitcoins = 0
is_alive = True
for i in range(rooms):
    room = rooms[i]
    args = room.split()
    command = args[0]
    number = int(args[1])

    if command == "potion":
        temp = health
        health += number
        healed = number

        if health > 100:
            health = 100
            healed = 100 - temp

        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}")
            is_alive = False
            break

if is_alive:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")





# line = input()
# initial_health = 100
# initial_bitcoins = 0
# rooms_count = 0
# is_alive = True
#
#
# rooms = line.split('|')
#
# for room in rooms:
#     rooms_count += 1
#     command_num = room.split(" ")
#     command = command_num[0]
#     number = int(command_num[1])
#
#     if command == 'potion':
#         if initial_health + number > 100:
#             print(f"You healed for {100 - initial_health} hp.")
#             initial_health = 100
#             print(f"Current health: {initial_health} hp.")
#         else:
#             print(f"You healed for {number} hp.")
#             initial_health += number
#             print(f"Current health: {initial_health} hp.")
#
#     elif command == "chest":
#         print(f"You found {number} bitcoins.")
#         initial_bitcoins += number
#     else:
#         initial_health -= number
#         if initial_health > 0:
#             print(f"You slayed {command}.")
#         else:
#             print(f'You died! Killed by {command}.')
#             print(f'Best room: {rooms_count}')
#             is_alive = False
#             break
#
# if is_alive:
#     print(f"You've made it!")
#     print(f"Bitcoins: {initial_bitcoins}")
#     print(f"Health: {initial_health}")
