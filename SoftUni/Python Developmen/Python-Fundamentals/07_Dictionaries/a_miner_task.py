"""
You will be given a sequence of strings, each on a new line. Every odd line on the console is representing a resource (e.g. Gold, Silver, Copper, and so on) and every even – quantity. Your task is to collect the resources and print them each on a new line.
Print the resources and their quantities in the following format:
{resource} –> {quantity}
The quantities will be in the range [1 … 2 000 000 000]
"""

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
