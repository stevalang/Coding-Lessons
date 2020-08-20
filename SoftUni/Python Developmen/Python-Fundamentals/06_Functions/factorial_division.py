"""

Write a function that receives two integer numbers. Calculate factorial of each number. Divide the first result by the second and print the division formatted to the second decimal point.

"""


def get_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


def factorial_division(a, b):
    return print(f"{(get_factorial(a) / get_factorial(b)):.2f}")


factorial_division(int(input()), int(input()))
