"""
Conditional Statements - Lab
Check: https://judge.softuni.bg/Contests/Practice/Index/1012#0
04. Number 1 ... 9 to Text
Condition:
Write a program that reads an integer in the range [1… 9],
entered by the user and writes it in English words.
If the number is out of range, the program displays "number too big".
Sample input and output
5 five 1 one 9 nine 10 number too big
"""


num = int(input())
if num < 1:
    print('zero')
if num < 2:
    print('one')
elif num < 3:
    print('two')
elif num < 4:
    print('three')
elif num < 5:
    print('four')
elif num < 6:
    print('five')
elif num < 7:
    print('six')
elif num < 8:
    print('seven')
elif num < 9:
    print('eight')
elif num < 10:
    print('nine')
else:
    print('number too big')
