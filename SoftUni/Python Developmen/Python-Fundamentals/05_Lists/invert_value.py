string = input()
l = []
for _ in range(len(string), -1, -1):
    l.append(string)
print(l)
