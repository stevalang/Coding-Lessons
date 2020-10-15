n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

while True:
    read_line = input()
    if read_line == 'END':
        break
    commands = read_line.split()
    action = commands[0]
    row, col, value = list(map(int, commands[1:]))
    if 0 <= row < n and 0 <= col < n:
        if action == 'Add':
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

for row in matrix:
    print(' '.join(map(str, row)))
