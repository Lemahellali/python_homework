import csv
class Employee:
    def __init__(self, employee_id, first_name, last_name, email):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
def read_employees():
    employees= []
    with open("../csv/employees.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)   
        for row in reader:
            emp=Employee(row[0], row[1], row[2], row[3]) 
            employees.append(emp)
            return employees  
        emps =read_employees()
        for e in emps:
            print(e.first_name, e.last_name)

