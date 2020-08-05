"""
Conditional Statements - Lab
Check: https://judge.softuni.bg/Contests/Practice/Index/1012#0
01. Excellent Result
Condition:
The first task on this topic is to write a console program that reads a score (decimal number),
entered by the user and prints "Excellent!" if the rating is 5.50 or higher.
"""
mark = float(input())

if mark >= 5.50:
    print('Excellent!')
