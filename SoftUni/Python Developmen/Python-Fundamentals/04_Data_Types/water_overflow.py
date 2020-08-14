buckets = int(input())

CAPACITY = 255
total_liters = 0
for i in range(buckets):
    water = int(input())
    total_liters += water
    if total_liters > CAPACITY:
        print(f'Insufficient capacity!')
        total_liters -= water
print(total_liters)
