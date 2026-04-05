'''
Write a program to display a/b where a and b are integers. If b=0, display infinite by 
handling the ‘ZeroDivisionError’. 
'''
try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")