from collections import deque

print()
def solve():
    dispenser = int(input())
    people = deque()
    while True:
        person = input()
        if person == 'Start':
            break
        people.append(person)

    while people:
        command = input()
        if command.startswith('refill'):
            dispenser += int(command.split()[1])
            continue

        if command == 'End':
            break

        litres = int(command)
        if dispenser >= litres:
            print(f'{people.popleft()} got water')
            dispenser -= litres
        else:
            print(f'{people.popleft()} must wait')
    print(f'{dispenser} liters left')


solve()
