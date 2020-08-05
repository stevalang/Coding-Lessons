hour = int(input())
minutes = int(input())

minutes_sum = hour * 60 + minutes
new_time = minutes_sum + 15

hour_new = new_time // 60
minutes_new = new_time % 60

if hour_new >= 24:
    hour_new -= 24

if minutes_new < 10:
    print(f'{hour_new}:0{minutes_new}')
else:
    print(f'{hour_new}:{minutes_new}')
