import sys
n = int(input())
i = 0
num = sys.maxsize

while i < n:
    current_num = int(input())
    if current_num < num:
        num = current_num
    i += 1
print(num)
