class Parking:
    def __init__(self):
        self.__cars = set()

    def process_car(self, direction, plate):
        if direction == 'IN':
            self.__cars.add(plate)
        elif direction == 'OUT' and plate in self.__cars:
            self.__cars.remove(plate)

    def print_status(self):
        if self.__cars:
            print('\n'.join([plate for plate in self.__cars]))
        else:
            print('Parking Lot is Empty')


parking = Parking()

n = int(input())

for _ in range(n):
    direction, plate = input().split(', ')
    parking.process_car(direction, plate)

parking.print_status()
