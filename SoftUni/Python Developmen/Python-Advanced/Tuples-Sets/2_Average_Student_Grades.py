from collections import defaultdict

students = defaultdict(list)

n = int(input())

for _ in range(n):
    tokens = input().split(' ')
    name = tokens[0]
    mark = float(tokens[1])
    students[name].append(mark)

for name, grades in students.items():
    grades_str = ' '.join(map(lambda f: format(f, '.2f'), grades))
    print(f'{name} -> {grades_str} (avg: {sum(grades)/ len(grades):.2f})')