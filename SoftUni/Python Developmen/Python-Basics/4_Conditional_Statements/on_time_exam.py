hour_exam = int(input())
minute_exam = int(input())
hour_arriving = int(input())
minutes_arriving = int(input())

hour_to_minutes_exam = hour_exam * 60
hour_to_minutes_arriving = hour_arriving * 60

sum_minutes_exam = hour_to_minutes_exam + minute_exam
sum_minutes_arriving = hour_to_minutes_arriving + minutes_arriving
diff = abs(sum_minutes_arriving - sum_minutes_exam)
if sum_minutes_exam < sum_minutes_arriving:
    print('Late')
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        h = diff // 60
        m = diff % 60
        if m < 10:
            print(f"{h}:0{m} hours after the start")
        else:
            print(f"{h}:{m} hours after the start")
elif sum_minutes_exam > sum_minutes_arriving + 30:
    if diff < 60:
        print('Early')
        print(f'{diff} minutes before the start')
    else:
        h = diff // 60
        m = diff % 60
        if m < 10:
            print('Early')
            print(f"{h}:0{m} hours before the start")
        else:
            print('Early')
            print(f"{h}:{m} hours before the start")
elif sum_minutes_exam == sum_minutes_arriving:
    print('On time')
else:
    print('On time')
    print(f'{diff} minutes before the start')
