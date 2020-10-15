def myfunc(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def recursive_func():
    recursive_func()
