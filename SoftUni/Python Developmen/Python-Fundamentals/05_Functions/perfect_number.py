"""
Write a function that receives an integer number and returns if this number is perfect or NOT.
A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
"""


def perfect_number(number):
    res = 0
    for i in range(1, number):
        if number % i == 0:
            res += i
    if res == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(int(input()))



