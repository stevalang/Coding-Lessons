field_row = int(input())
print()
fleets = [] # ['1 0 0 1', '2 0 0 0', '0 3 0 1']
for _ in range(field_row):
    ships = input()
    fleets.append(ships)
battle = input()
attacks = battle.split(' ') # ['0-0', '1-0', '2-1', '2-1', '2-1', '1-1', '2-1']
index = 0
for damage in attacks:
    x = damage.split('-')
    row = int(x[0])
    col = int(x[1])
    ship = int(fleets[row][col])
    if ship > 0:
        ship = 0
        index += 1
