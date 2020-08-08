n1_max = int(input())
n2_max = int(input())
n3_max = int(input())
is_odd = False
for n1 in range(2, n1_max + 1, 2):
    for n2 in range(2, n2_max + 1):
        for n3 in range(2, n3_max + 1, 2):
            if n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7:
                print(f'{n1} {n2} {n3}')
