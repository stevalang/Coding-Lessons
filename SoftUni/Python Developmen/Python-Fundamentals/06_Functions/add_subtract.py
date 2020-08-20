# def sum_numbers(a, b, c):
#     return a + b - c
#
#
# print(sum_numbers(int(input()), int(input()), int(input())))


def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def solve(a, b, c):
    sum_n = sum_numbers(a, b)
    res_n = subtract(sum_n, c)
    return res_n


a = int(input())
b = int(input())
c = int(input())

res = solve(a, b, c)
print(res)


