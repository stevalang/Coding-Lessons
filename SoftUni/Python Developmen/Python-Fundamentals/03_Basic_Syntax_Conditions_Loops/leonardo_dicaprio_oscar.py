'''
Write a program that receives a single integer number and prints different messages depending on the number:
If Oscar is 88 - "Leo finally won the Oscar! Leo is happy".
If Oscar is 86 - "Not even for Wolf of Wall Street?!"
If Oscar is not 88 nor 86 (and below 88) - "When will you give Leo an Oscar?"
If Oscar is over 88 - "Leo got one already!"
'''


line = int(input())
if line == 88:
    print("Leo finally won the Oscar! Leo is happy")
elif line == 86:
    print("Not even for Wolf of Wall Street?!")
elif line != 86 and line < 88:
    print("When will you give Leo an Oscar?")
elif line > 88:
    print("Leo got one already!")
