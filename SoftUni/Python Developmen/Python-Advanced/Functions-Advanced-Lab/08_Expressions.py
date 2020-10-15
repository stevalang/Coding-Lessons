from itertools import product
from itertools import chain

nums = list(input().split(', '))
n = len(nums)

permutations = list(product('+-', repeat=n))

for permutation in permutations:
    expr = ''.join(list(chain(*zip(permutation, nums))))
    res = eval(expr)
    print(f"{expr}={res}")
