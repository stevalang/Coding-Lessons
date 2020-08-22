employees = input().split()
factor = int(input())
employee_happiness = list(map(lambda x: int(x) * factor, employees))
avg_happiness = sum(employee_happiness) / len(employee_happiness)

# above_avg_happy = [employee for employee in employee_happiness if employee >= avg_happiness]
above_avg_happy = list(filter(lambda employee: employee >= avg_happiness, employee_happiness))

if int(len(above_avg_happy)) >= len(employee_happiness) / 2:
    print(f'Score: {len(above_avg_happy)}/{len(employee_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(above_avg_happy)}/{len(employee_happiness)}. Employees are not happy!')
