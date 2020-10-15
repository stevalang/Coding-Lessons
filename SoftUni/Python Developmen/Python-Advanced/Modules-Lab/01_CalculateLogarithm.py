from math import log

n = float(input())
base = input()
if base == 'natural':
    print(f'{log(n):.2f}')
else:
    base = float(base)
    print(f'{log(n, base):.2f}')
