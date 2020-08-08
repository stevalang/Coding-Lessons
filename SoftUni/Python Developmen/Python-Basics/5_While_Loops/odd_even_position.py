import sys
n = int(input())

sum_odd = 0
odd_max_number = -sys.maxsize
odd_min_number = sys.maxsize
sum_even = 0
even_max_number = -sys.maxsize
even_min_number = sys.maxsize
for i in range(1, n + 1):
    current_number = float(input())
    if i % 2 == 0:
        sum_even += current_number
        if current_number > even_max_number:
            even_max_number = current_number
        if current_number < even_min_number:
            even_min_number = current_number
    else:
        sum_odd += current_number
        if current_number > odd_max_number:
            odd_max_number = current_number
        if current_number < odd_min_number:
            odd_min_number = current_number

print(f'OddSum={sum_odd:.2f},')
if odd_min_number == sys.maxsize:
    print(f'OddMin=No,')
else:
    print(f'OddMin={odd_min_number:.2f},')
if odd_max_number == -sys.maxsize:
    print(f'OddMax=No,')
else:
    print(f'OddMax={odd_max_number:.2f},')
print(f'EvenSum={sum_even:.2f},')
if even_min_number == sys.maxsize:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={even_min_number:.2f},')
if even_max_number == -sys.maxsize:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={even_max_number:.2f}')
