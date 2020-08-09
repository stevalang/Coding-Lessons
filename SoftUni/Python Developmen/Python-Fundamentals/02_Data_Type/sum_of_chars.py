lines = int(input())
total_sum = 0
for i in range(lines):
    letter = ord(input())
    total_sum += letter
print(f'The sum equals: {total_sum}')