

n = int(input())

diary = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in diary:
        diary[name] = []
    diary[name].append(grade)

# for student, grades in diary.items():
#     average = sum(grades)/len(grades)
#     if average >= 4.50:
#         student_average_grades[student] = average
get_average = lambda x: sum(x)/len(x)
student_average_grades = {student: get_average(grades) for student, grades in diary.items() if get_average(grades) >= 4.50}


sorted_diary = dict(sorted(student_average_grades.items(), key=lambda x: x[1], reverse=True))

for key, value in sorted_diary.items():
    print(f'{key} -> {value:.2f}')