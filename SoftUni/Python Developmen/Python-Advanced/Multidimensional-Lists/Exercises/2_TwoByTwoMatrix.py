def read_matrix():

    rows, cols = list(map(int, input().split(' ')))

    mat = [
        list(input().split(' ')) for _ in range(rows)
    ]
    return mat, cols


def get_square(mat):
    count_squares = 0
    for i in range(len(matrix)-1):
        row = matrix[i]
        for j in range(len(row)-1):
            if matrix[i][j] == matrix[i + 1][j] and \
                    matrix[i][j] == matrix[i][j+1] and \
                    matrix[i + 1][j] == matrix[i + 1][j + 1]:
                count_squares += 1
    return count_squares


matrix, col = read_matrix()
squares = get_square(matrix)
print(squares)

