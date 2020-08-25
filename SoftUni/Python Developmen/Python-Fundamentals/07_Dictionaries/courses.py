"""
Write a program that keeps information about courses. Each course has a name and registered students.
You will be receiving a course name and a student name, until you receive the command "end". Check if such course already exists, and if not, add the course. Register the user into the course. When you receive the command "end", print the courses with their names and total registered users, ordered by the count of registered users in descending order. For each contest print the registered users ordered by name in ascending order.
Input
Until the "end" command is received, you will be receiving input in the format: "{courseName} : {studentName}".
The product data is always delimited by " : ".
Output
Print the information about each course in the following the format:  "{courseName}: {registeredStudents}"
Print the information about each student, in the following the format: "-- {studentName}"
"""


courses = {}

while True:
    data = input()
    if data == 'end':
        break

    args = data.split(" : ")
    course = args[0]
    name = args[1]

    if course not in courses:
        courses[course] = [name]
    else:
        courses[course].append(name)

sorted_courses = dict(sorted(courses.items(),key=lambda el: len(el[1]), reverse=True))
for name_course, username in sorted_courses.items():
    print(f'{name_course}: {len(username)}')
    for student_name in sorted(username):
        print(f'-- {str(student_name)}')



