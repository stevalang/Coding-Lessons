"""
Simple Operations and Calculations - Exercise
Check: https://judge.softuni.bg/Contests/Compete/Index/1160#0
03. 2D Rectangle Area
Condition:
A rectangle is given by the coordinates of two of its opposite angles (x1, y1) - (x2, y2).
Calculate its area and perimeter.
The input is read from the console. The numbers x1, y1, x2 and y2 are given one per line.
The output is displayed on the console and must contain two rows with one number on each of them - the face and the perimeter.
Format the result to 2 characters after the comma.
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
