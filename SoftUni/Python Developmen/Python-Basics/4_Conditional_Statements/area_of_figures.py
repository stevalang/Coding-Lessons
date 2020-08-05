import math

figure_shape = (input())
s = 0
is_valid = True

if figure_shape == 'square':
    a = float(input())
    s = a * a

elif figure_shape == 'rectangle':
    a = float(input())
    b = float(input())
    s = a * b
elif figure_shape == 'circle':
    r = float(input())
    s = math.pi * r * r
elif figure_shape == 'triangle':
    a = float(input())
    h = float(input())
    s = a * h / 2
else:
    print('not a shape')
    is_valid = False

if is_valid:
    print(f'{s:.3f}')
