def find_in_matrix(matrix, search):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == search:
                return i, j
    return None


n = int(input())
matrix = [list(input()) for _ in range(n)]
search = input()

pos = find_in_matrix(matrix, search)
if pos:
    print(pos)
else:
    print(f'{search} does not occur in the matrix')