"""
Lists Basics - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1724#2
SUPyF2 Lists Basics Lab - 03. Lists Statistics
Problem:
You will be given a number n. On the next n lines you will receive integers. You have to create and print two lists:
•	One with all the positives (including 0)
•	One with all the negatives
Finally print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"
Example:
Input:
5
10
3
2
-15
-4
Output:
[10, 3, 2]
[-15, -4]
Count of positives: 3. Sum of negatives: -19
"""


notes = []
while True:
    string = input()
    if string == 'End':
        break
    tokens = string.split('-')
    importance = int(tokens[0])
    task = tokens[1]
    notes.append((importance, task))
result = [task_name for importance, task_name in sorted(notes) if importance != 0]

print(result)
