def func():
    return 1


print(func())
print(func)


def hello():
    return 'Hello!'


print(hello())
print(hello)
greet = hello
print(greet)

print(greet())

del hello
print(greet())











