#Write a program to find the greatest of four numbers entered by the user.
numbers = []
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

greatest = numbers[0]
for n in numbers:
    if n > greatest:
        greatest = n

print("The greatest number is:", greatest)