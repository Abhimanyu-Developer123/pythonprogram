class Employee:
    def __init__(self, emp_id, name, position, salary):  # Constructor
        self.emp_id = emp_id  # Employee ID
        self.name = name  # Employee name
        self.position = position  # Employee position
        self.salary = salary  # Employee salary

    def show_details(self):  # Display employee details
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ₹{self.salary}")

    def update_salary(self, new_salary):  # Update employee salary
        if new_salary > 0:
            self.salary = new_salary
            print(f"Salary updated to ₹{self.salary}")
        else:
            print("Invalid salary amount. It must be positive.")

class EmployeeManagementSystem:
    def __init__(self):  # Constructor
        self.employees = {}  # Dictionary to store employees by ID

    def add_employee(self, emp_id, name, position, salary):  # Add a new employee
        if emp_id in self.employees:
            print(f"Employee with ID {emp_id} already exists.")
        else:
            self.employees[emp_id] = Employee(emp_id, name, position, salary)
            print(f"Employee '{name}' added successfully.")

    def remove_employee(self, emp_id):  # Remove an employee
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee with ID {emp_id} has been removed.")
        else:
            print(f"Employee with ID {emp_id} does not exist.")

    def display_all_employees(self):  # Display all employee details
        if not self.employees:
            print("No employees in the system.")
        else:
            print("\n--- All Employees ---")
            print("---------------------")
            for emp in self.employees.values():
                emp.show_details()
                print("---------------------")

# Example Usage
ems = EmployeeManagementSystem()

# Adding employees
ems.add_employee(101, "John Doe", "Software Engineer", 60000)
ems.add_employee(102, "Jane Smith", "Project Manager", 80000)
ems.add_employee(103, "Mike Jhonson", "Superviser", 150000)

# Display all employees
ems.display_all_employees()

# Update salary of an employee
ems.employees[101].update_salary(65000)
ems.employees[103].update_salary(152500)

# Remove an employee
ems.remove_employee(102)

# Display all employees after update and removal
ems.display_all_employees()
