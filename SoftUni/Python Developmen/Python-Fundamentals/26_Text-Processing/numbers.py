numbers = input().split()

res = []

int_nums = []
for num in numbers:
    int_nums.append(int(num))

nums_to_add = len(int_nums)//2
avg = sum(int_nums) / len(int_nums)

