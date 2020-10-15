def find_diagonals(n):
    firs_diagonal = [matrix[i][j] for i in range(n) for j in range(n) if i == j]
    second_diagonal = [matrix[i][j] for i in range(n) for j in range(n) if n - 1 - i == j]
    return firs_diagonal, second_diagonal


def create_row():
    return [int(j) for j in input().split(', ')]


def create_matrix(n):
    matrix = [create_row() for row in range(n)]
    return matrix


n = int(input())

matrix = create_matrix(n)

f, s = find_diagonals(n)

print(f"First diagonal: {', '.join(map(str, f))}. Sum: {sum(f)}")
print(f"Second diagonal: {', '.join(map(str,s))}. Sum: {sum(s)}")
