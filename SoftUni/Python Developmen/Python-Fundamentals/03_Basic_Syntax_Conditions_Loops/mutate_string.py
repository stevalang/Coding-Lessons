'''
You will be given two strings. Transform the first string into the second one, one letter at a time and print it. Print only the unique strings
Note: the strings will have the same lengths
'''

str_one = input()
str_two = input()

for i in range(len(str_one)):
    if str_two[i] != str_one[i]:
        for str_two_index in range(0, i + 1):
            print(str_two[str_two_index], end="")
        for str_one_index in range(i + 1, len(str_two)):
            print(str_one[str_one_index], end='')
        print()
