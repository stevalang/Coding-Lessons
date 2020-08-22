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



