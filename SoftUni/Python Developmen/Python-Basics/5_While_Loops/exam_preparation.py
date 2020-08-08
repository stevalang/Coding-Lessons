bad_marks_number = int(input())
task_name = input()
bad_marks_counter = 0
task_counter = 0
total_marks = 0
while True:
    if task_name != 'Enough':
        current_task_name = task_name
        mark = int(input())
        total_marks += mark
        if mark <= 4:
            bad_marks_counter += 1
        task_counter += 1
        if bad_marks_counter == bad_marks_number:
            print(f'You need a break, {bad_marks_counter} poor grades.')
            break
        task_name = input()
    else:
        break

avg_mark = total_marks / task_counter
if task_name == 'Enough':
    print(f'Average score: {avg_mark:.2f}')
    print(f'Number of problems: {task_counter}')
    print(f'Last problem: {current_task_name}')
