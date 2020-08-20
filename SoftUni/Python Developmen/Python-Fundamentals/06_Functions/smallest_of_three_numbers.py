"""
Write a function which receives three integer numbers and returns the smallest. Use appropriate name for the function.

"""

# def smallest_of_three(a, b, c):
#
#     return min(a, b, c)
#
#
# print(smallest_of_three(int(input()), int(input()), int(input())))


def get_smallest_of_three_numbers(first_num, second_num, third_num):
    smallest = 0

    if first_num < second_num and first_num < third_num:
        smallest = first_num
    elif second_num < first_num and second_num < third_num:
        smallest = second_num

    return smallest


res = get_smallest_of_three_numbers(first_num=int(input()), second_num=int(input()), third_num=int(input()))
print(res)
