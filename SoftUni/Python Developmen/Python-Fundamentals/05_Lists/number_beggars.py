"""
Your task here is pretty simple: given a list of numbers and an amount of beggars, you are supposed to return a list with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.
For example: [1,2,3,4,5] for 2 beggars will return a result of 9 and 6, as the first one takes [1,3,5], the second collects [2,4].
The same list with 3 beggars would have in turn have produced a better outcome for the second beggar: 5, 7 and 3, as they will respectively take [1, 4], [2, 5] and [3].
Also note that not all beggars have to take the same amount of "offers", meaning that the length of the list is not necessarily a multiple of n; length can be even shorter, in which case the last beggars will of course take nothing (0).
"""
# money = input()
# m = money.split(", ")
# b = int(input())
#
# l = [0] * b
#
# for num in range(0, len(m), len(m) // b):
#     j = int(i % b)
#     if i % b == 0:
#         pass
#     else:
#         l[j] = l.append(int(m[i]))
#
#     j = m[i]
#     l.append(j)


nums_str = input().split(", ")
count = int(input())
nums = []

for num in nums_str:
    nums.append(int(num))

result_sum = [0] * count
for i in range(len(nums)):
    index = i % count
    result_sum[index] += nums[i]

print(result_sum)
