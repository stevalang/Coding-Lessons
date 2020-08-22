"""
You will be given a number n representing the number of rows of the field. On the next n lines you will receive each row of the field as a string with numbers separated by a space. Each number greater than zero represents a ship with a health equal to the number value. After that you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}". Each time a square is being attacked, if there is a ship there (number greater than 0) you should reduce its value. After the attacks have ended, print how many ships were destroyed (if its value has reached zero)
"""


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
