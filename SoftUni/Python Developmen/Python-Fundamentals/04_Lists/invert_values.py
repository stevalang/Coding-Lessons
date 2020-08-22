'''
Write a program that receives a single string containing numbers separated by a single space. Print a list containing the opposite of each number
'''

string_number = input().split()
opposite = []
for num in string_number:
    opposite.append(- int(num))
print(opposite)

