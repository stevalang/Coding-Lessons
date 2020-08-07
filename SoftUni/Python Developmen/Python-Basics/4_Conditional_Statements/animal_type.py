"""
Conditional Statements - Lab
Check: https://judge.softuni.bg/Contests/Practice/Index/1012#0
11. Animal Type
Condition:
Write a program that prints the class of the animal according to its name entered by the user.
-dog -> mammal
-crocodile, tortoise, snake -> reptile
-others -> unknown
Sample input and output
Input Output
dog mammal
snake reptile
cat unknown
"""


animal = input()

is_mammal = animal == 'dog'
is_reptile = animal == 'dog'

if is_mammal:
    print('mammal')
elif is_reptile:
    print('reptile')
else:
    print('unknown')
