'''
Write a program that receives a single string containing numbers separated by a single space. Print a list containing the opposite of each number
'''

string = input()
l = []
for _ in range(len(string), -1, -1):
    l.append(string)
print(l)
