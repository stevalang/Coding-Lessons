"""
A palindrome is a number which reads the same backward as forward, such as 323 or 1001. Write a function which receives a list of positive integers and checks if each integer is a palindrome or not. Print the results on the console
The input will be a single string containing the numbers separated by comma and space ", "
"""

# def pal_int(string):
#     for each_string in [word for word in string.split(", ")]:
#         if each_string == each_string[::-1]:
#             print('True')
#         else:
#             print('False')
#
#
# pal_int(input())
#
#


def is_palindrome(text):
    counter = len(text) // 2
    is_palindrome = True

    for i in range(counter):
        second_index = len(text) - 1 - i
        if text[i] != text[second_index]:
            is_palindrome = False
            break
    return is_palindrome


def solve(items: str):
    for item in items:
        print(is_palindrome(item))


items = input().split(', ')
solve(items)
