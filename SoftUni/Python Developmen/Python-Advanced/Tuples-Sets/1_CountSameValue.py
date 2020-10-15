from collections import defaultdict

nums = map(float, input().split(' '))

number_occurrence = defaultdict(int)

for num in nums:
    number_occurrence[num] += 1

for num, count in number_occurrence.items():
    print(f'{num} - {count} times')
