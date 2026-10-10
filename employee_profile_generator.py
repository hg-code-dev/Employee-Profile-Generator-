# Employee profile Generator 
first_name = 'John' # Employee first name 
last_name = 'Doe' # Employee last name 
full_name = first_name + ' ' + last_name # Employee's first + last name = full name 
address = '123 Main Street' # Employee's street name 
address += ', Apartment 4B' # Employee's building  
employee_age = 29 # Employee's age 
employee_info = full_name + ' is ' + str(employee_age) + ' years old' # Employee's full name + age = employees info 
print(employee_info) # Output: full name + is + age + years old  
experience_years = 7 # Employees years of experience 
experience_info = 'Experience: ' + str(experience_years) + ' years' # Employee's years of experience = employees experience info 
print(experience_info) # Output: Experience + experience years + years 
position = 'Data Analyst' # Employees position in the company 
salary = 75000 # Employee's yearly salary 
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}' #f-string: Employee's full name, age, position, salary($)
print(employee_card) #Output: Employee + full name + Age + employee age + Position + position + Salary + salary = employee card 
employee_code = 'DEV-2026-JD-001' # Employee company code 
department = employee_code[0:3] # slicing the string DEV-2026-JD-001 to get department 
print(department) #Output: sliced string = department 
year_code = employee_code[4:8] # slicing the string DEV-2026-JD-001 to get year
print(year_code) #Output: sliced string = year 
initials = employee_code[9:11] # slicing the string DEV-2026-JD-001 to get employee initials 
print(initials) #Output: sliced string = employee initials 
last_three = employee_code[-3:] # slicing the string DEV-2026-JD-001 to get last 3 digits 
print(last_three) #Output: sliced string = last 3 digits 