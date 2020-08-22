class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


person_one = Person("Peter")
print(person_one.get_name())

person_two = Person("Slavi")
print(person_two.get_name())