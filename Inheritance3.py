'''
Create a class ‘Employee’ and add salary 
and increment properties to it. 
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment(self, amount):
        self.salary += amount

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"
# Example usage:User Input
name = input("Enter employee's name: ")
salary = float(input("Enter employee's salary: "))
employee = Employee(name, salary)
increment_amount = float(input("Enter increment amount: "))
employee.increment(increment_amount)
print(employee)  # Output: Employee: name, Salary: salary + increment_amount