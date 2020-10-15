print([
    [
        n for n in map(int, input().split(', '))
        if n % 2 == 0
     ]
    for _ in range(int(input()))
])

