"""
Conditional Statements - Lab
Check: https://judge.softuni.bg/Contests/Practice/Index/1012#0
06. Number 100 ... 200
Condition:
Write a program that reads an integer entered by the user and checks if it is below 100,
between 100 and 200 or over 200. Print messages accordingly, as in the examples below:
Sample input and output
entrance exit entrance exit entrance exit
95 Less than 100 120 Between 100 and 200 210 Greater than 200
"""



num = int(input())
if num < 100:
    print('Less than 100')
elif num <= 200:
    print('Between 100 and 200')
else:
    print('Greater than 200')
