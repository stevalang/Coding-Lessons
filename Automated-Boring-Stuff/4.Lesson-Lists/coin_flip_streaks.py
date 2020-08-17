import random

flips = []
head = 0
head_strikes = 0
tail = 0
tail_strikes = 0
nums_of_streaks = 0
for _ in range(10000):
    head_or_tail = random.randint(0, 1)
    if head_or_tail == 0:
        flips.append('H')
    else:
        flips.append('T')

for item in flips:
    if item == 'H':
        is_six_in_row = False
        for i in range(5):
            if flips[i + 1] == 'H':
                head += 1
            else:
                head = 0
                break
        if head == 6:
            head_strikes += 1
            head = 0
    else:
        for i in range(5):
            if flips[i + 1] == 'T':
                continue
            else:
                break
        if tail == 6:
            tail_strikes += 1
            tail = 0

print(f'Chance of streak: {nums_of_streaks / 100}')

print(flips)
print(head_strikes)
print(tail_strikes)
