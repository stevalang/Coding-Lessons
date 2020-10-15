from collections import deque


def dispenser_management():
    water_in_dispenser = int(input())
    people = deque([])

    while True:
        command = input()
        if command == 'End':
            break
        if command == 'Start':
            pass
        if command.startswith('refill'):
            water_in_dispenser += int(command.split(' ')[-1])
        elif command.isalpha():
            name = command
            people.append(name)
        elif command.isdigit():
            if water_in_dispenser >= int(command):
                print(f'{people.popleft()} got water')
                water_in_dispenser -= int(command)
            else:
                print(f"{people.popleft()} must wait")

    print(f'{water_in_dispenser} liters left')


dispenser_management()
