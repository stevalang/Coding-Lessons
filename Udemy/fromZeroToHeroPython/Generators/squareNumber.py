def generator_square(n):
    for i in range(n):
        yield i ** 2


for x in generator_square(10):
    print(x)
