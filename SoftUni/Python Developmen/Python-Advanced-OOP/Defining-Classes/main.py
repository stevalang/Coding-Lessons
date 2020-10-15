class Person:
    max_age = 150

    def __init__(self, name):
        print(f'Init method for person {name}')
        self.name = name


p = Person('Gosho')

print(p.name)


Person.x = 5
print(Person.x)
print(str(Person))

