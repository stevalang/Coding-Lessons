"""
Simple Operations and Calculations - Lab
05. Creation Projects
Check: https://judge.softuni.bg/Contests/Compete/Index/1011#2
Write a program that calculates how many hours it will take an architect to design several
construction sites. The preparation of a project takes approximately three hours.
Entrance
2 lines are read from the console:
1. The name of the architect - text;
2. Number of projects - integer.
Exit
The following is printed on the console:
"The architect {architect's name} will need {hours needed} hours to complete {number of projects} project / s."
"""


name = input()
projects_count = int(input())
time_needed = int(projects_count*3)
print(f"The architect {name} will need {time_needed} hours to complete {projects_count} project/s.")
