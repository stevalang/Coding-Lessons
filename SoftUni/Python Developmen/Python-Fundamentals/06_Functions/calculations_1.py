def solve(operator, a, b):
    if operator == 'multiply':
        operator = '*'
    elif operator == 'divide':
        operator = '/'
    elif operator == 'add':
        operator = '+'
    elif operator == 'subtract':
        operator = '-'
    return eval(f'{a}{operator}{b}')


print(int(solve(input(), input(), input())))
