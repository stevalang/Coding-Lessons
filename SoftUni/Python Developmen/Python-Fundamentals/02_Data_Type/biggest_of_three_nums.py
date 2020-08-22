import sys
biggest_num = - sys.maxsize
for num in range(3):
    num = int(input())
    if num > biggest_num:
        biggest_num = num
print(biggest_num)
