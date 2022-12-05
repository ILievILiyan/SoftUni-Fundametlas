command = input().split(" -> ")
companies_staff = {}

while command[0] != "End":
    company_name, employee_id = command[0], command[1]

    if company_name not in companies_staff.keys():
        companies_staff[company_name] = []
    if employee_id not in companies_staff[company_name]:
        companies_staff[company_name].append(employee_id)

    command = input().split(" -> ")

for company in companies_staff.keys():
    print(company)
    for employees in companies_staff[company]:
        print(f"-- {employees}")
