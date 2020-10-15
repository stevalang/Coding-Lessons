class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False
        self.current_water = 0

    def water(self, quantity):
        self.current_water += quantity
        self.is_happy = self.get_happy_status()

    def get_happy_status(self):
        return self.current_water >= self.water_requirements

    def status(self):
        if self.is_happy:
            return f'{self.name} is happy'
        else:
            return f'{self.name} is not happy'


#  If the water is greater than or equal of the requirements of the flower, it becomes happy

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())