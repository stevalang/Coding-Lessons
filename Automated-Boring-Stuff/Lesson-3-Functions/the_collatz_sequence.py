import sys


def collatz(number):
    if number / 2 == 0:
        res = number // 2
    elif number % 2 == 0:
        res = 3 * number + 1

    while res == 1:
        print(res)
        sys.exit()

    while res != 1:
        print(res)
        number = res
        return collatz(number)


print("Enter a number:")
try:
    number = int(input())
    collatz(number)
except ValueError:
    print('Please enter a valid INTEGER.')
