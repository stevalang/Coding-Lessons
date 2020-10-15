f = open('baba.txt', 'rb')

while (c := input()) != 'END':
    print(c)

with open('my_first_file.txt') as f:
    print(f.readlines())