line1 = int(input())
line2 = int(input())

result = ''
for i in range(line1, line2 + 1):
    result += chr(i) + ' '
print(result)
    # print(chr(i), end=' ')
