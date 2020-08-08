n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    number = int(input())
    if 0 < number < 200:
        p1 += 1
    if 199 < number < 400:
        p2 += 1
    if 399 < number < 600:
        p3 += 1
    if 599 < number < 800:
        p4 += 1
    if number > 799:
        p5 += 1
print(f'{p1/n*100:.2f}%')
print(f'{p2/n*100:.2f}%')
print(f'{p3/n*100:.2f}%')
print(f'{p4/n*100:.2f}%')
print(f'{p5/n*100:.2f}%')

