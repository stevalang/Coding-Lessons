from math import floor
record_sec = float(input())
distance_m = float(input())
time_sec_1m = float(input())
current_time = distance_m * time_sec_1m

resistance_m = floor(distance_m / 15)
add_seconds = resistance_m * 12.5

new_time = current_time + add_seconds
difference = abs(record_sec - new_time)

if new_time < record_sec:
    print(f'Yes, he succeeded! The new world record is {new_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')

