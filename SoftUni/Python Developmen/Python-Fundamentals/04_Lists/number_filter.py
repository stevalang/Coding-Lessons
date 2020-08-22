"""
Lists Basics - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1724#4
SUPyF2 Lists Basics Lab - 05. Numbers Filter
Problem:
You will receive a single number n. On the next n lines you will receive integers.
After that you will be given one of the following commands:
•	even
•	odd
•	negative
•	positive
Filter all the numbers that fit in the category (0 counts as a positive). Finally, print the result.
Example:
Input:
5
33
19
-2
18
998
even
Output:
[19, -2, 18, 998]
Input:
3
111
-4
0
negative
Output:
[-4]
"""

n = int(input())

numbers = []
filtered = []

for i in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()
if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered.append(number)
elif command == "positive":
    for number in numbers:
        if number >= 0:
            filtered.append(number)

print(filtered)
