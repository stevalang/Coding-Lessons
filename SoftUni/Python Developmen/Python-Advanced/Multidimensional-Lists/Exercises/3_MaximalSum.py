def read_matrix():
    n, m = tuple(map(int, input().split(' ')))

    matrix = [list(map(int, input().split(' '))) for i in range(n)]

    return matrix, n, m


def get_squares(matrix, n_rows, m_cols):
    squares = []
    for i in range(n_rows - 2):
        for j in range(m_cols - 2):
            square = [matrix[i][j], matrix[i][j - m + 1], matrix[i][j - m + 2],
                      matrix[i + 1][j], matrix[i + 1][j - m + 1], matrix[i + 1][j - m + 2],
                      matrix[i + 2][j], matrix[i + 2][j - m + 1], matrix[i + 2][j - m + 2]]
            squares.append(square)
    return squares


def get_max_sum_square(squares):
    max_sum = 0
    max_square = []
    for square in squares:
        if max_sum < sum(square):
            max_sum = sum(square)
            if max_square:
                max_square.pop()
            max_square.append(square)

    return max_sum, max_square


solution, n, m = read_matrix()
squ = get_squares(solution, n, m)
maximum_sum, maximum_square = get_max_sum_square(squ)

print(f'Sum = {maximum_sum}')

for i in range(0, 9, 3):
    line = maximum_square[0][i:i + 3]
    print(' '.join(map(str, line)))
