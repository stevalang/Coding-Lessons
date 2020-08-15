lines = int(input())
my_list = []
filtered = []
for _ in range(lines):
    number = int(input())
    my_list.append(number)
command = input()
if command == 'positive':
    for number in my_list:
        if number >= 0:
            filtered.append(number)
elif command == 'negative':
    for number in my_list:
        if number < 0:
            filtered.append(number)
elif command == 'even':
    for number in my_list:
        if number % 2 == 0:
            filtered.append(number)
elif command == 'odd':
    for number in my_list:
        if number % 2 != 0:
            filtered.append(number)

print(filtered)
