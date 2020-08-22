import sys

# COMPREHENSION
# ---------------------------------------------------------------
# numbers = list(map(int, input().split()))
# remover = [numbers.remove(min(numbers)) for _ in range(int(input()))]
# print(numbers)


# FOR LOOP

nums_str = input().split()
numbers = []

for num in nums_str:
    numbers.append(int(num))

removal = int(input())

for _ in range(removal):
    numbers.remove(min(numbers))
print(numbers)

# nums_string = input().split(' ')
# n = int(input())
#
# for i in range(n):
#     min_num = min(nums_string)
#     nums_string.remove(min_num)
# print(nums_string)


# new_list = []
# a = -sys.maxsize
# for num in nums_string:
#     new_list.append(int(num))
#
# for i in range(n):
#     count = 0
#     for i in new_list:
#         if i > a:
#             a == i
#             count += 1
# print(new_list)
