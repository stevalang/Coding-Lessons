"""
Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros and moves them to the back without messing up the other elements. Print the resulting integer list
"""

a = input()
a = a.split(", ")

count = 0
for i in range(len(a)):
    if int(a[i]) == 0:
        a.pop(i)
        count += 1
a = [int(i) for i in a]
print(a + count * [0])


# 1, 0, 1, 2, 0, 1, 3
