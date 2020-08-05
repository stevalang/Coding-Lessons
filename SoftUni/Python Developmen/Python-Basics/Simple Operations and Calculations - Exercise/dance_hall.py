from math import floor

length_in_meters = float(input())
width_in_meter = float(input())
side_of_wardrobe = float(input())

room_area = length_in_meters * width_in_meter * 10000

wardrobe_area = side_of_wardrobe * side_of_wardrobe * 10000

bench_area = room_area / 10

dance_space = room_area - wardrobe_area - bench_area

dancer_space = 40
dancing_space = 7000

dancer_count = dance_space / (dancer_space + dancing_space)

print(floor(dancer_count))
