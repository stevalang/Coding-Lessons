cake_width = int(input())
cake_length = int(input())

cake_area = cake_length * cake_width
cake_eaten = input()
cake_eaten_count = 0
is_not_stop = True
while cake_area >= 0:
    if cake_eaten == "STOP":
        is_not_stop = False
        print(f'{cake_area} pieces are left.')
        break
    cake_eaten_count = int(cake_eaten)
    cake_area -= cake_eaten_count
    if cake_area <= 0:
        break
    cake_eaten = (input())
cake_needed = abs(cake_area)
if is_not_stop:
    print(f'No more cake left! You need {cake_needed} pieces more.')