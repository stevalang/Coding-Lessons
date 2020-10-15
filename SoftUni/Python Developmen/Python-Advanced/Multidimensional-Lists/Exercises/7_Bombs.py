def explode(row, )

n = int(input())

matrix = [list(map(int, input().split(' '))) for _ in range(n)]
print(matrix)

bomb_cells = input().split(' ')

print(bomb_cells)
bombs = []
for cell in bomb_cells:
    i, j = list(map(int, cell.split(',')))
    bomb = matrix[i][j]
    bombs.append(bomb)

    explode(i, j, n, matrix)
    matrix[i][j] = 0
# example = [
#         ['8', '3', '2', '5'],\
#         ['6', '4', '7', '9'],\
#         ['9', '9', '3', '6'],\
#         ['6', '8', '1', '2']
# ]