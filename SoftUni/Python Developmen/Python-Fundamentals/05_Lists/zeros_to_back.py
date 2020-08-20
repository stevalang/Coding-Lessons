"""
Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros and moves them to the back without messing up the other elements. Print the resulting integer list
"""

# index = 0
# for i in range(len(num_str)):
#     if len(num_str) > 1:
#         if num_str[i] == 0:
#             num_str.pop(i)
# print(num_str)

# 1, 0, 1, 2, 0, 1, 3,


def push_zeros_to_the_end(num_str, n):
    count = 0
    for i in range(n):
        if num_str[i] != 0:
            num_str[count] = num_str[i]
            count += 1
    while count < n:
        num_str[count] = 0
        count += 1
    return num_str


string = input().split(", ")
num_str = []
for num in string:
    num_str.append(int(num))
n = len(num_str)

print(push_zeros_to_the_end(num_str,n))
