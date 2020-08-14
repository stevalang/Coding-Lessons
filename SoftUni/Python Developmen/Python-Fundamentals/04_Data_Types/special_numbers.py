'''
A number is special when its sum of digits is 5, 7 or 11.
Write a program to read an integer n and for all numbers, in the range 1…n, print the number and if it is special or not (True / False).
'''

n = int(input())

for i in range(1, n + 1):
    digits_sum = 0
    for digit in str(i):
        digits_sum += int(digit)

    is_special = digits_sum in [5, 7, 11]
    print(f'{i} -> {is_special}')
