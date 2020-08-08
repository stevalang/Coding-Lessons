n = int(input())

combinations_count = 0

for n1 in range(0, n + 1):
    for n2 in range(0, n + 1):
        for n3 in range(0, n + 1):
            if n1 + n2 + n3 == n:
                combinations_count += 1
print(combinations_count)