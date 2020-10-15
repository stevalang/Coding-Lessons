rows, cols = tuple(map(int, input().split()))

matrix = []
player_position = []

for i in range(rows):
    row = [x for x in list(input())]
    matrix.append(row)
    for c in row:
        if 'P' == c:
            player_position = [i, row.index('P')]

commands = list(input())

for command in commands:
    next_player_position = []
    temp_position = []
    if command == 'U':
        next_player_position = [player_position[0] - 1, player_position[1]]
        next_position = matrix[[next_player_position[0]][next_player_position[1]]]
        current_position = matrix[player_position[0]][player_position[1]]
        if next_position == ".":
            next_player_position = 'P'
            current_position = '.'

    elif command == 'D':
        next_player_position = [player_position[0] + 1, player_position[1]]
    elif command == 'L':
        next_player_position = [player_position[0], [player_position[1]-1]]
    elif command == 'R':
        next_player_position = [player_position[0], [player_position[1]+1]]

for row in matrix:
    commands
    for element in row:
        if element == '.':

print(matrix)
print(commands)
print(player_position)
