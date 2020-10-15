from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split(' ')))
print(f'{max(orders)}')

while orders:
    current_order = orders.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        orders.append(current_order)
        break

if orders:
    orders_left = ''.join(list(map(str, orders)))
    print(f"Orders left: {orders_left}")
else:
    print("Orders complete")
