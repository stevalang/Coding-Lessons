import math
year = input()
p = int(input())
h = int(input())

times_played_volleyball = 0
weekends = 48
additional_play_time = 0
weekends_Sofia = weekends - h
saturdays_play = 3 / 4 * weekends_Sofia
vacation_play = 2/3 * p
play_home_town = h
times_played_volleyball = saturdays_play + vacation_play + play_home_town

if year == "leap":
    additional_play_time = times_played_volleyball * 0.15
    times_played_volleyball += additional_play_time
    print(f'{math.floor(times_played_volleyball)}')
else:
    print(f'{math.floor(times_played_volleyball)}')
