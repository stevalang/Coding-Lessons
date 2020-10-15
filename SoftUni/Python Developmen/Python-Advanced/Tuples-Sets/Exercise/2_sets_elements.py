n, m = (map(int, input().split(' ')))


set_one = set()
set_two = set()

for _ in range(n):
    number = input()
    set_one.add(number)

for _ in range(m):
    number = input()
    set_two.add(number)

set_intersection = set_one & set_two

print('\n'.join(set_intersection))

