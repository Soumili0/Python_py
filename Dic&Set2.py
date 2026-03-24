#Write a program to input eight numbers from the user and display all the unique numbers (once). 
# Input 8 numbers from user
numbers = []

for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Get unique numbers
unique_numbers = list(set(numbers))

# Display result
print("Unique numbers are:")
for num in unique_numbers:
    print(num)