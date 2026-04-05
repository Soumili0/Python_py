'''
Write a list comprehension to print
a list which contains the multiplication table of a 
user entered number. 
'''
number = int(input("Enter a number to generate its multiplication table: "))
multiplication_table = [number * i for i in range(1, 11)]
print(f"Multiplication table of {number}: {multiplication_table}")
#output
# Enter a number to generate its multiplication table: 5
# Multiplication table of 5: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
