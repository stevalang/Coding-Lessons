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


from math import floor

length_in_meters = float(input())
width_in_meter = float(input())
side_of_wardrobe = float(input())

room_area = length_in_meters * width_in_meter * 10000

wardrobe_area = side_of_wardrobe * side_of_wardrobe * 10000

bench_area = room_area / 10

dance_space = room_area - wardrobe_area - bench_area

dancer_space = 40
dancing_space = 7000

dancer_count = dance_space / (dancer_space + dancing_space)

print(floor(dancer_count))
