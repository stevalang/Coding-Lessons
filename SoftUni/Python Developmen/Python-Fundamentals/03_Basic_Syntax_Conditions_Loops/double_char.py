'''
Given a string, you have to print a string in which each character (case-sensitive) is repeated.
'''
text = input()

for letter in text:
    print(2 * letter, end="")
