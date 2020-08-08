student_name = input()
grade = 1
average_score = 0
times_failed = 0
excluded = False
while grade <= 12:
    score = float(input())
    if score >= 4:
        average_score += score
        grade += 1
    else:
        times_failed += 1
        if times_failed == 2:
            excluded = True
            break

if excluded:
    print(f'{student_name} has been excluded at {grade} grade')
else:
    print(f'{student_name} graduated. Average grade: {average_score / 12:.2f}')
