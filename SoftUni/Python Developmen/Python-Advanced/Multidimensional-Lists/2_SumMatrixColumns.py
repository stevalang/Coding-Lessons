rows, cols = [int(n) for n in input().split(', ')]

matrix = [
    [int(n) for n in input().split(' ')]
    for _ in range(rows)
]

for col in zip(*matrix):
    print(sum(col))

# for j in range(cols):
#     total = sum(row[j] for row in matrix)
#     print(total)
