'''
Write a class “Calculator” capable of finding 
square, cube and square root of a 
number.
'''
class Calculator:
    def square(self, num):
        return num ** 2

    def cube(self, num):
        return num ** 3

    def square_root(self, num):
        return num ** 0.5
# Example usage
calc = Calculator()
number = input("Enter a number: ")
number = float(number)  # Convert input to a float  
print(f"Square of {number}: {calc.square(number)}")
print(f"Cube of {number}: {calc.cube(number)}")
print(f"Square root of {number}: {calc.square_root(number)}")      
