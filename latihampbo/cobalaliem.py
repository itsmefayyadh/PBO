class Employee:
    def __init__(self, uid=None, name=None, age=None, salary=None):
        self.name = name
        self.age = age
        self.id = uid
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, {self.age}, {self.id}, {self.salary}"

    def set_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.id = int(input("Enter id: "))
        self.salary = int(input("Enter salary: "))

if __name__ == '__main__':
    # Empty list containing our employees
    employees = []
    # We loop 5 times.
    for i in range(2):
        # We create an employee
        employee = Employee()
        # We set the data
        employee.set_data()
        # We append our brand-new employee into the list
        employees.append(employee)

    # Now we display our data :
    for employee in employees:
        # We just need to print the object thanks to __str__ method
        print(employee)