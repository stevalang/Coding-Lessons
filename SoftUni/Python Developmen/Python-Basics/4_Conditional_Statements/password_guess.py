"""
Conditional Statements - Lab
Check: https://judge.softuni.bg/Contests/Practice/Index/1012#0
07. Password Guess
Condition:
Write a program that reads a password (one line of random text) entered by the user and checks if
the entry matches the phrase "s3cr3t! P @ ssw0rd". In case of coincidence, display "Welcome".
In case of discrepancy, display "Wrong password!".
Sample input and output
entrance exit entrance exit entrance exit
qwerty Wrong password! s3cr3t! P @ ssw0rd Welcome s3cr3t! p @ ss Wrong password!
"""

password = (input())

if password == "s3cr3t!P@ssw0rd":
    print('Welcome')
else:
    print("Wrong password!")
