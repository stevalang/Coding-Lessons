def print_triangle(size):
    for row in range(size):
        print(*[i for i in range(1, row+1)])
    for row in range(size, 0, -1):
        print(*[i for i in range(1, row+1)])
