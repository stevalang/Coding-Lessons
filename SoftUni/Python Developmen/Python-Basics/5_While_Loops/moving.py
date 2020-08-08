free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())
total_free_area = free_space_height * free_space_length * free_space_width
boxes_space = input()
boxes_count = 0

while boxes_space != 'Done':
    boxes_space = int(boxes_space)
    boxes_count += boxes_space
    diff = abs(total_free_area - boxes_count)
    if total_free_area <= boxes_count:
        print(f'No more free space! You need {diff} Cubic meters more.')
        break
    boxes_space = input()
if total_free_area > boxes_count:
    print(f'{diff} Cubic meters left.')
