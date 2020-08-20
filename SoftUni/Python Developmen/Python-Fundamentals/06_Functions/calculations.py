"""

Create a function that receives three parameters and calculates a result depending on operator. The operator can be  'multiply', 'divide', 'add', 'subtract' . The input comes as three parameters – two integers and an operator as a string.

"""


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def execute(a, b, operation):
    mapping = {
        'multiply': multiply,
        'add': add,
        'divide': divide,
        'subtract': subtract,
    }
    fn = mapping[operation]
    return fn(a, b)


a = int(input())
b = int(input())
operation = input()
print(execute(a, b, operation))





# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
# def execute(a, b, operation):
#     if operation == 'multiply':
#         return multiply(a, b)
#     if operation == 'add':
#         return add(a, b)
#     if operation == 'divide':
#         return divide(a, b)
#     if operation == 'subtract':
#         return subtract(a, b)

# a = int(input())
# b = int(input())
# operation = input()
# print(execute(a, b, operation))


# def execute(a, b, operation):
#     if operation == 'multiply':
#         return a * b
#     if operation == 'divide':
#         return a / b
#     if operation == 'add':
#         return a + b
#     if operation == 'subtract':
#         return a - b
#
#
# a = int(input())
# b = int(input())
# operation = input()
# print(execute(a, b, operation))


#     [multiply
#      divide
#      add
#      subtract]
#
#     ]
#
#
# a, b, = int(input())
# result = 0
# print(result)
