n = int(input())

parking_lot = set()


def get_into_parking(plate_number):
    parking_lot.add(plate_number)


def get_out_parking(plate_number):
    if parking_lot:
        parking_lot.remove(plate_number)


for _ in range(n):
    action, plate_number = input().split(', ')
    operations = {
        'IN': get_into_parking,
        'OUT': get_out_parking,
    }
    operations[action](plate_number)

if parking_lot:
    print('\n'.join(parking_lot))
else:
    print('Parking Lot is Empty')
