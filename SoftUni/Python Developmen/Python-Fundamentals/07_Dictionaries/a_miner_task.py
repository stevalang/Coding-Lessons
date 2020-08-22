resource = input()

mine = {}

while resource != 'stop':
    quantity = int(input())
    if resource not in mine:
        mine[resource] = 0
    mine[resource] += int(quantity)

    resource = input()

for (resource, quantity) in mine.items():
    print(f'{resource} -> {mine[resource]}')