x = [1, 2, 3, 4, 5, 6]

filtered = [num for num in x if num % 2 == 0]

print(x)

# --------------------------------------

items = [word[0] for word in ['this', 'is', 'a', 'list']]
print(items)

# --------------------------------------

x = [num for num in range(5)]

# -------------------------------

nums = [1, 2, 3, 4, 5, 6]

filtered1 = [
    True if x % 2 == 0 else False
    for x in nums
    if x % 2 == 0
]
print(filtered1)

# -------------------------------------------

l = [('Peter', 22), ('Amy', 18)]
print(l)
print(dict(l))

# ------------------------------

numbers = [1, 2, 3, 4, 4, 5, 6, 2, 1]

unique = {num for num in nums}

print(unique)


def test():
    print(test)
    return 42


print([test() for i in range(10) if i % 2 == 0])
