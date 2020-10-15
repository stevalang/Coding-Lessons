def read_matrix(num_lines):

    mat = [
        list(map(int, input().split(' '))) for _ in range(num_lines)

    ]
    return mat


def get_primary_diagonal(mat):  # [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    diagonal = [
        mat[i][i]
        for i in range(len(matrix))
    ]
    return sum(diagonal)


def get_secondary_diagonal(mat):
    diagonal = [
        mat[i][n - 1 - i]
        for i in range(len(matrix))
    ]
    return sum(diagonal)


def get_diff(primary, second):
    return abs(primary - second)


n = int(input())
matrix = read_matrix(n)
primary_diagonal = get_primary_diagonal(matrix)
second_diagonal = get_secondary_diagonal(matrix)
print(get_diff(primary_diagonal, second_diagonal))
