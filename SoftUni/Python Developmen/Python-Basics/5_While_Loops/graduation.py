name = input()
grade = 1
average_score = 0
while grade <= 12:
    score = float(input())
    if score >= 4:
        average_score += score
        grade += 1
print(f'{name} graduated. Average grade: {average_score / 12:.2f}')
