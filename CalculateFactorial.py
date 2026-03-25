#Write a program to calculate the factorial of a given number using for loop. 
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is:", factorial)