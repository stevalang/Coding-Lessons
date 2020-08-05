"""
Simple Operations and Calculations - Exercise
Проверка: https://judge.softuni.bg/Contests/Compete/Index/1160#0
03. 2D Rectangle Area
Условие:
Правоъгълник е зададен с координатите на два от своите срещуположни ъгъла (x1, y1) – (x2, y2).
Да се пресметнат площта и периметъра му.
Входът се чете от конзолата. Числата x1, y1, x2 и y2 са дадени по едно на ред.
Изходът се извежда на конзолата и трябва да съдържа два реда с по една число на всеки от тях – лицето и периметъра.
Резултатът да се форматира до 2 знака след запетаята.
"""

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
