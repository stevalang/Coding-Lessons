"""
Conditional Statements - Lab
Check: https://judge.softuni.bg/Contests/Practice/Index/1012#0
03. Even or Odd
Condition:
Write a program that reads an integer entered by the user and prints it to the console
whether the number is even or odd.
1. First create a Python file with an appropriate name in the existing project;
2. Read an integer from the console:
3. Check that the number is even by dividing it modularly by 2 and check that there is a remainder of the division.
If there is no residue, print an "even" output. Otherwise, print "odd":
"""


number = int(input())

if number % 2 == 0:
    print('even')
else:
    print('odd')
