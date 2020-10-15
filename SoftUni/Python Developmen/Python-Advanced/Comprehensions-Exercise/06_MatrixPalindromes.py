from string import ascii_lowercase


def create_cell(i,  j):
    first_char = ascii_lowercase[i]
    middle_char = ascii_lowercase[(i + j)]

    return f"{first_char}{middle_char}{first_char}"


i, j = map(int, input().split())

matrix = [[create_cell(row, col) for col in range(j)] for row in range(i)]

for row in matrix:
    print(' '.join(row))

