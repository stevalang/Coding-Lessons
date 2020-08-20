# def odd_even_sum(numbers=input()):
#     sum_even = []
#     for num in numbers:
#         if num % 2 == 0:
#             sum_even.append(num)
#         return sum_even
#     odd_sum = []
#     for num in numbers:
#         if num % 2 != 0:
#             odd_sum.append(num)
#         return odd_sum
#     return [odd_sum, even_sum()]
#
#
# print(f'Odd sum = {sum(odd_even_sum[0])}, Even sum = {sum(odd_even_sum[1])}')


def even_odd_sum(number):
    odd_digits_list = [int(digit) for digit in number if digit % 2 != 0]
    even_digits_list = [int(digit) for digit in number if digit % 2 == 0]
    return f"Odd sum = {sum(odd_digits_list)}, Even sum = {sum(even_digits_list)}"


print(even_odd_sum([int(digit) for digit in input()]))
