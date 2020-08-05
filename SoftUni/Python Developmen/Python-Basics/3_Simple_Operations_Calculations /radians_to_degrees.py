"""
Simple Operations and Calculations - Exercise
02. Radians to Degrees
Check: https://judge.softuni.bg/Contests/Compete/Index/1160#0
Condition:
Write a program that reads an angle in radians (rad) and converts it to degrees (deg).
Round the result to the nearest whole number.
Use the formula: degree = radian * 180 / π.
The number π in Python can be accessed through the math module. To use its functionality,
you must first import the module.
"""


from math import pi
rad = float(input())
deg = rad * 180/ pi
print(round(deg))
