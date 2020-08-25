"""
Write a program that keeps information about companies and their employees. 
You will be receiving a company name and an employee's id, until you receive the command "End" command. Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
When you finish reading the data, order the companies by the name in ascending order. 
Print the company name and each employee's id in the following format:
{companyName}
-- {id1}
-- {id2}
-- {idN}
Input / Constraints
Until you receive the "End" command, you will be receiving input in the format: "{companyName} -> {employeeId}".
The input always will be valid.
"""

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
