class Animal:

    def __init__(self, command, name, food_limit, location):
        self.name = name
        self.food_limit = food_limit
        self.location = location
        self.command = command

    def feed(self):
        pass

    animals = []
# Add:Bonie:3490:RiverArea

print(animal.name)
print(animal.location)
print(animal.food_limit)

while True:
    line = input()
    if line == "Last Info":
        break
    animals = []
    command, name, daily_limit, location = input().split(':')
    if command == 'Add':
        animals.append(name)
        Animal(name).food_limit += daily_limit

    else:
        pass


    animal = Animal(command, name, food_limit, location)
