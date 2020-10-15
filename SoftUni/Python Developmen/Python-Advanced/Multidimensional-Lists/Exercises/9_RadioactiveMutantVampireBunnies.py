def find_player(matrix):
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if value == 'P':
                return x, y


def find_bunnies(matrix):
    bunnies = []
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if value == 'B':
                bunnies.append((x, y))
                return bunnies


rows, cols = tuple(map(int, input().split()))
lair = [list(input()) for _ in range(rows)]
commands = list(input())
player_x, player_y = find_player(lair)

bunny_multiplication_direction = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

last_player_x, last_player_y = None, None

won = False
lost = False

for command in commands:

    lair[player_x][player_y] = '.'
    last_player_x = player_x
    last_player_y = player_y

    if command == 'U':
        player_x -= 1
    elif command == 'D':
        player_x += 1
    elif command == 'L':
        player_y -= 1
    elif command == 'R':
        player_y += 1

    if rows > player_x >= 0 and cols > player_y >= 0:
        won = True
        break
    else:
        at_position = lair[player_x][player_y]
        if at_position == 'B':
            lost = True
            last_player_x = player_x
            last_player_y = player_y
        else:
            lair[last_player_x][last_player_y] = 'P'

    for bunny_x, bunny_y in find_bunnies(lair):
        for delta_x, delta_y in bunny_multiplication_direction:
            new_bunny_x = bunny_x + delta_x
            new_bunny_y = bunny_y + delta_y

            if rows > new_bunny_x >= 0 and cols > new_bunny_y >= 0:
                at_position = lair[new_bunny_x][new_bunny_y]
                lair[new_bunny_x][new_bunny_y] = 'B'
                print()
                for row in lair:
                    print(''.join(row))
                if lost:
                    break
                if at_position == 'P':
                    lost = True
                    break
    if won:
        break

for row in lair:
    print(''.join(row))

if won:
    print(f"won: {last_player_x} {last_player_y}")
else:
    print(f"dead: {last_player_x} {last_player_y}")
