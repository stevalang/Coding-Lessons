import math

companions = int(input())
days = int(input())
coins = 0
companions_count = companions
for i in range(1, days + 1):

    if i % 15 == 0:
        companions_count += 5
    if i % 10 == 0:
        companions_count -= 2
    if i % 3 == 0 and i % 5 == 0:
        coins -= 2 * companions_count
    if i % 5 == 0:
        coins += 20 * companions_count
    if i % 3 == 0:
        coins -= companions_count * 3
    coins += (50 - (companions_count * 2))

print(f'{companions_count} companions received {math.floor(coins / companions_count)} coins each.')
