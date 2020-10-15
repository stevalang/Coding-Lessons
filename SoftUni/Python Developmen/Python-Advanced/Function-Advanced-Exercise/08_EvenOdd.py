def even_odd(*args):
    nums = args[:-1]
    command = args[-1]
    if command == 'even':
        return list(filter(lambda num: num % 2 == 0, nums))
    else:
        return list(filter(lambda num: num % 2 != 0, nums))


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))