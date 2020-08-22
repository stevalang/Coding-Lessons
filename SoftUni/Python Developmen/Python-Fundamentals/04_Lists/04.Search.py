"""
Lists Basics - Lab
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1724#3
SUPyF2 Lists Basics Lab - 04. Search
Problem:
You will receive a number n and a word. On the next n lines you will be given some strings.
You have to add them in a list and print them.
After that you have to filter out only the strings that include the given word and print that list also.
Examples:
Input:
3
SoftUni
I study at SoftUni
I walk to work
I learn Python at SoftUni
Output:
['I study at SoftUni', 'I walk to work', 'I learn Python at SoftUni']
['I study at SoftUni', 'I learn Python at SoftUni']
Input:
4
tomatoes
I love tomatoes
I can eat tomatoes forever
I don't like apples
Yesterday I ate two tomatoes
Output:
['I love tomatoes', 'I can eat tomatoes forever', "I don't like apples", 'Yesterday I ate two tomatoes']
['I love tomatoes', 'I can eat tomatoes forever', 'Yesterday I ate two tomatoes']
"""

lines = int(input())
special_word = input()
my_list = []
special_list = []
for _ in range(lines):
    word = input()
    if special_word in word:
        special_list.append(word)
    my_list.append(word)
print(my_list)
print(special_list)
