# nums = list(map(lambda x: int(x), input().split(', ')))
# print(nums)
# even_indices = [index for index in range(len(nums)) if nums[index] % 2 == 0]
# print(even_indices)

nums = list(map(int, input().split(", ")))
print([index for index, num in enumerate(nums) if num % 2 == 0])
