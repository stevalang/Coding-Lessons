"""
Conditional Statements - Lab
Check: https://judge.softuni.bg/Contests/Practice/Index/1012#0
09. Area of ​​Figures
Condition:
Write a program in which the user enters the type and dimensions of a geometric figure and calculates its face.
The figures are of four types: square, rectangle, circle and triangle.
The first line of the input reads the type of figure (square, rectangle, circle or triangle):
-If the figure is a square, the next line reads a number - the length of its side;
-If the figure is a rectangle, the next two lines read two numbers - the lengths of its sides;
-If the figure is a circle, on the next line read a number - the radius of the circle;
-If the figure is a triangle, the next two lines read two numbers - the length of its side and
the length of the height to it.
Round the result to 3 digits after the decimal point.
"""

import math

figure_shape = (input())
s = 0
is_valid = True

if figure_shape == 'square':
    a = float(input())
    s = a * a

elif figure_shape == 'rectangle':
    a = float(input())
    b = float(input())
    s = a * b
elif figure_shape == 'circle':
    r = float(input())
    s = math.pi * r * r
elif figure_shape == 'triangle':
    a = float(input())
    h = float(input())
    s = a * h / 2
else:
    print('not a shape')
    is_valid = False

if is_valid:
    print(f'{s:.3f}')
