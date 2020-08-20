# def hello(name='Jose'):
#     print('The hello() function has been executed!')
#
#     def greet():
#         return "\t This is the greet() func inside hello!"
#
#     def welcome():
#         return '\t This is welcome() inside hello'
#
#     print('I am going to return a function')
#
#     if name == 'Jose':
#         return greet
#     else:
#         return welcome
#
#
# my_new_func = hello("Jose")
# print(my_new_func)
# print(my_new_func())
#
#
# def cool():
#
#     def super_cool():
#         return 'I am very cool!'
#     return super_cool
#
#
# some_func = cool()
#
# print(some_func)
# print(some_func())
#

def hello():
    return 'Hi Jose!'


def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())


other(hello)

