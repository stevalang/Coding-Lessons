import sys
n = int(input())
i = 0
number = -sys.maxsize
while i < n:
    current_number = int(input())
    if current_number > number:
        number = current_number
    i += 1
print(number)