'''
 Create a class ‘Employee’ and add salary and increment properties to it. 
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
which changes the value of increment based on the salary. 
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self._increment = 0

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, amount):
        if amount < 0:
            raise ValueError("Increment cannot be negative.")
        self._increment = amount

    @property
    def salary_after_increment(self):
        return self.salary + self._increment

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary},Increment: {self._increment}, Salary after Increment: {self.salary_after_increment}"
# Example usage:User Input
name = input("Enter employee's name: ") 
salary = float(input("Enter employee's salary: "))
employee = Employee(name, salary)
increment_amount = float(input("Enter increment amount: "))
employee.increment = increment_amount
print(employee)  # Output: Employee: name, Salary: salary, Increment: increment_amount, Salary after Increment: salary + increment_amount