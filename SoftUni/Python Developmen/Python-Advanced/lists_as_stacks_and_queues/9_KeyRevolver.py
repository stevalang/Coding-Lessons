from collections import deque

bullet_price = int(input())
size_barrel = int(input())

bullets_raw = deque(map(int, input().split(' ')))
bullets = deque(reversed(bullets_raw))
locks = deque(map(int, input().split(' ')))

intelligence = int(input())

cost = 0
index = 0
local_barrel = size_barrel

while len(bullets) > 0 and len(locks) > 0:
    index += 1


    bullet = bullets.popleft()
    lock = locks.popleft()
    cost += bullet_price
    can_unlock = lock <= bullet

    if can_unlock:
        print('Bang')
    else:
        print('Ping')
        locks.appendleft(lock)

        if local_barrel == 0:
            if bullets:
                print('Reloading!')
                local_barrel = min(size_barrel, len(bullets))

if len(locks) == 0:
    print(print(f'"{len(bullets)} bullets left. Earned ${intelligence - cost}"'))
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
