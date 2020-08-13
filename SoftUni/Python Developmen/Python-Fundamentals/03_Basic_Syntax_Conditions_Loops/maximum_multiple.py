'''
Given a Divisor and a Bound, find the largest integer N, such that:
N is divisible by divisor
N is less than or equal to bound
N is greater than 0.
Notes: The divisor and bound are only positive values. It's guaranteed that a divisor is found
'''


divisor = int(input())
bound = int(input())
max_num = 0
for i in range(1, bound+1):
    if i % divisor == 0:
        max_num = i
print(max_num)
