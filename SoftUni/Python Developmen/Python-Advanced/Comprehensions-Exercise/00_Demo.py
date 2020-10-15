mylist = [1, 2, 3, 4]

mylist_fom_comprehension = [str(x) for x in range(1, 5)]

odd_numbers = [x for x in range(5) if x % 2 != 0]

new_list = [x + 1 if x % 2 == 0 else x for x in range(5)]

print({str(i): i for i in [1, 2, 3, 4]})

print({str(i) for i in range(5)})


def generate_col():
    return [j for j in range(5)]


print([generate_col() for i in range(5)])


matrix = [
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
]
flatten = [col for row in matrix for col in row]