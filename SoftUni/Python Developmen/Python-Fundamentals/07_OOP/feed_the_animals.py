class Animal:

    def __init__(self, name: str, food: int, area: str):
        self.name = name
        self.food = food
        self.area = area


class Area:

    def __init__(self, name:str, animals: list):

zoo = []

while True:
    command = input()
    if command == "Last Info":
        break
    add_feed, a_name, a_food, a_area = command.split(':')
    if add_feed == "Add":
        area_in_zoo = False
        for area in zoo:
            if area.name == a_area:
                animal_in_area = True
                for animal in area.animals:
                    
                animal.food += int(a_food)
                break

    def add(self, name, daily_food_limit, area):
        if name in self.animals:
            pass
        else:
            self.animals.append(name)
        self.daily_food_limit.append(daily_food_limit)
        self.area.append(area)

    def feed(self, name, food):
        if name in self.animals:
            self.daily_food_limit.remove(food)
            if
        else:
            self.animals.append(name)
        self.daily_food_limit.append(daily_food_limit)
        self.area.append(area)




Add:Maya:7600:WaterfallArea