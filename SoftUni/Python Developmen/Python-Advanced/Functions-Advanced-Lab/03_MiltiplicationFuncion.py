from functools import reduce

# def multiply(*args):
#     res = 1
#     for a in args:
#         res *= a
#     return res
#
#
# result = multiply(1, 2, 3, 4)
# print(result)

multiply = lambda *args: reduce(lambda a, b: a * b, args)
