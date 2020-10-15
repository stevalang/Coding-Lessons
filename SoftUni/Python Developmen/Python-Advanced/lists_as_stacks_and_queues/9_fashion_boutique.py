from collections import deque

box = deque(map(int, input().split(" ")))
rack = int(input())

clothes_sum = 0
racks_count = 1

while box:
    clothe = box.pop()
    if clothes_sum + clothe <= rack:
        clothes_sum += clothe
    elif clothes_sum == rack:
        racks_count += 1
        clothes_sum = 0
        clothes_sum += clothe
    else:
        racks_count += 1
        clothes_sum = 0
        clothes_sum += clothe

print(racks_count)


