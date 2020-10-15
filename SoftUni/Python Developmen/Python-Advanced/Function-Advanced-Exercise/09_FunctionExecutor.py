def func_executor(*args):
    res = []
    for function_definition in args:
        func, func_args = function_definition
        # res.append(func(*func_args))
        return list(map(lambda x: func(*func_args), func_args))


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))


