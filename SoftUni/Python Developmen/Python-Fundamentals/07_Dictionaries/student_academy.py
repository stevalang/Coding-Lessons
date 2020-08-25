"""
Write a program that keeps information about students and their grades. 
You will receive n pair of rows. First you will receive the student's name, after that you will receive his grade. Check if the student already exists and if not, add him. Keep track of all grades for each student.
When you finish reading the data, keep the students with average grade higher than or equal to 4.50. Order the filtered students by average grade in descending order.
Print the students and their average grade in the following format:
{name} –> {averageGrade}
Format the average grade to the 2nd decimal place.
"""

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
