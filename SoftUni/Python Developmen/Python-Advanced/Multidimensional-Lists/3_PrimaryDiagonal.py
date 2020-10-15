n = int(input())

matrix = [list(map(int, input().split(' '))) for _ in range(n)]
total = sum([matrix[i][i] for i in range(n)])
print(total)
