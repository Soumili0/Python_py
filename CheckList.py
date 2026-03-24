#Write a program which finds out whether a given name is present in a list or not. 
names = ["Alice", "Bob", "Charlie", "David"]
name = input("Enter a name: ")
if name in names:
    print("The name is present in the list.")
else:
    print("The name is not present in the list.")