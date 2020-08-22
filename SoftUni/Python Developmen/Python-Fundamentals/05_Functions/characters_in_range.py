"""
Write a function that receives two characters and returns a single string with all the characters in between them according to the ASCII code.
"""

def string(a=input(), b=input()):
    new_string = []
    start = ord(a)
    finish = ord(b)
    for i in range(start+1, finish):
        new_string += [chr(i)]
    return ' '.join(new_string)


print(string())
