employees = {}

while True:
    line = input()
    if line == "End":
        break
    args = line.split(" -> ")
    company_name = args[0]
    employee_id = args[1]

    if company_name not in employees:
        employees[company_name] = []
    if employee_id not in employees[company_name]:
        employees[company_name].append(employee_id)

for corp, emp_id in sorted(employees.items()):
    print(f'{corp}')
    for ids in emp_id:
        print(f'-- {ids}')
