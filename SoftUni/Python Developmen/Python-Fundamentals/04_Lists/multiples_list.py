"""
Write a program that receives two numbers (factor and count) and creates a list with length of the given count and contains only elements that are multiples of the given factor

"""

factor = int(input())
count = int(input())
nums = []
for num in range(factor, factor * count + 1, factor):
    nums.append(num)
print(nums)
