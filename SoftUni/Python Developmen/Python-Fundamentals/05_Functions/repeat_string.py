"""
Write a function that receives a string and a repeat count n. The function should return a new string (the old one repeated n times).
"""

def string_repeat(text, count):
    result = text * count
    return result


print(string_repeat(input(), int(input())))
