'''
Cruise Game
'''
import math
name = input()
games = int(input())
points_total = 0
volleyball = 0
tennis = 0
badminton = 0
volleyball_counter = 0
tennis_counter = 0
badminton_counter = 0
for i in range(1, games+1):
    game_name = input()
    points = int(input())
    if game_name == "volleyball":
        points *= 1.07
        volleyball += points
        volleyball_counter += 1
    elif game_name == "tennis":
        points *= 1.05
        tennis += points
        tennis_counter += 1
    elif game_name == "badminton":
        points *= 1.02
        badminton += points
        badminton_counter += 1
    points_total += points

avg_volleyball = volleyball / volleyball_counter
avg_tennis = tennis / tennis_counter
avg_badminton = badminton / badminton_counter
if avg_volleyball >= 75 and avg_tennis >= 75 and avg_badminton >= 75:
    print(f"Congratulations, {name}! You won the cruise games with {math.floor(points_total)} points.")
else:
    print(f"Sorry, {name}, you lost. Your points are only {math.floor(points_total)}.")



