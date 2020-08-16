try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("There is a list of a strings that can't be multiply")
