command = input()

nums = list(map(lambda num: int(num), input().split()))

if command == 'Odd':
    sum_odd = sum(list(filter(lambda num: num % 2 != 0, nums)))
    print(sum_odd * len(nums))
else:
    sum_even = sum(list(filter(lambda num: num % 2 == 0, nums)))
    print(sum_even * len(nums))
