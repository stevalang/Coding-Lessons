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
