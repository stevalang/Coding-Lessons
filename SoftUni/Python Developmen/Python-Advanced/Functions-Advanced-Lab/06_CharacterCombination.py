def generate(k: int, a: list):
    if k == 1:
        permutations.add(''.join(a))
    else:

        generate(k - 1, a)

        for i in range(k):
            if k % 2 == 0:
                a[i], a[k - 1] = a[k - 1], a[i]
            else:
                a[0], a[k - 1] = a[k - 1], a[0]

            generate(k - 1, a)


permutations = set()
s = list(input())
generate(len(s), s)
print('\n'.join(list(permutations)))
