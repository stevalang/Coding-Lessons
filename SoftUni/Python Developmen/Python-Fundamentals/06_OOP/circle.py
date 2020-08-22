class Circle:

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter/2

    __pi = 3.14

    def calculate_circumference(self):
        return Circle.__pi*self.diameter

    def calculate_area(self, ):
        return self.__pi * self.radius**2

    def calculate_area_of_sector(self, angle):
        return (angle/360) * self.__pi * self.radius ** 2


circle = Circle(int(input()))
angle = int(input())

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
