n = int(input())
elements_set = set()

for _ in range(n):
    elements = set(input().split(' '))
    elements_set = elements_set | elements

print('\n'.join(elements_set))