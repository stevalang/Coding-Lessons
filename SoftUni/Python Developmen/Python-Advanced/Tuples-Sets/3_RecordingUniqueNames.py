number_lines = int(input())

names = set()

for _ in range(number_lines):
    name = input()
    if name not in names:
        print(name)
        names.add(name)
