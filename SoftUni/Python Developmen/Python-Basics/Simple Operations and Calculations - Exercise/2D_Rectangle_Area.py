# 1. Reading cordinates
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

lenght = abs(x1 - x2)
width = abs(y1 - y2)

area = lenght * width
print(f'{area:.2f}')

perimeter = lenght * 2 + width * 2
print(f'{perimeter:.2f}')
