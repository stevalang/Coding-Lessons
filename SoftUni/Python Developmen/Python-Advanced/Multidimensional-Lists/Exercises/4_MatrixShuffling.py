def is_valid(matrix, cmd):

    if cmd and cmd[0] != 'swap':
        return False
    if len(cmd[1:]) != 4:
        return False

    x1, y1, x2, y2 = tuple(map(int, cmd[1:]))

    if x1 < 0 or x1 >= n:
        return False
    if x2 < 0 or x2 >= n:
        return False
    if y1 < 0 or y1 >= m:
        return False
    if y2 < 0 or y2 >= m:
        return False
    return True


n, m = tuple(map(int, input().split(' ')))

matrix = []


while True:
    temp_command = input()
    if temp_command == 'END':
        break
    command = temp_command.split(' ')

    if len(command) == m:
        matrix.append(command)

    elif is_valid(matrix, command):
        x1, y1, x2, y2 = tuple(map(int, command[1:]))
        temp = matrix[x1][y1]
        matrix[x1][y1] = matrix[x2][y2]
        matrix[x2][y2] = temp
        for line in matrix:
            print(' '.join(line))
    else:
        print('Invalid input!')
