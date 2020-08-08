import sys
num = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for i in range(num):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number


sum_numbers = sum_numbers - max_number
difference_between_sum_and_max = abs(max_number - sum_numbers)
if sum_numbers == max_number:
    print(f'Yes\nSum = {sum_numbers}')
else:
    print(f'No\nDiff = {difference_between_sum_and_max}')
