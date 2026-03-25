''' Write a program to print multiplication table of n using for loops in reversed 
order.'''
n = int(input("Enter a number: "))
print("Multiplication table of", n, "in reversed order:")
for i in range(10, 0, -1):
    print(n, "x", i, "=", n * i)
'''    Output:
Enter a number: 5
Multiplication table of 5 in reversed order:
5 x 10 = 50
5 x 9 = 45
5 x 8 = 40
5 x 7 = 35
5 x 6 = 30
5 x 5 = 25
5 x 4 = 20
5 x 3 = 15
5 x 2 = 10
5 x 1 = 5'''
