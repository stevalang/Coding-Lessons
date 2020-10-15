from mathops import executor, parser

expr = input()

res = executor.executor(*parser.parse_expr(expr))
print(f'{res:.2f}')
