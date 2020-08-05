"""
Simple Operations and Calculations - Exercise
Check: https://judge.softuni.bg/Contests/Compete/Index/1160#0
05. Dance Hall
Condition:
A group of dancers are looking for a new hall. The hall they liked is rectangular and has dimensions:
L - length and W - width (in meters). The hall has a square wardrobe with a side - A
and a rectangular bench with an area 10 times smaller than the area of ​​the hall.
The place occupied by a dancer is 40 cm² and in addition he needs another 7000 cm² for free movement.
Write a program that calculates how many dancers can fit in the hall and move freely.
The result obtained should be rounded down to the nearest whole number.
Entrance
3 lines are read from the console:
1. L - length of the hall in meters - real number;
2. W - width of the hall in meters - real number;
3. A - side of the wardrobe in meters - a real number.
Exit
Print an integer on the console - the number of dancers that can fit in the free space
of the hall, rounded to the nearest whole number down.
"""


from math import pi
rad = float(input())
deg = rad * 180/ pi
print(round(deg))
