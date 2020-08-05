import math

runner_1 = int(input())
runner_2 = int(input())
runner_3 = int(input())

total_time = runner_1 + runner_2 + runner_3

minutes = total_time // 60

seconds = total_time % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
