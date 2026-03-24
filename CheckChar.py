#Write a program to find whether a given username contains less than 10 
# characters or not.
# Input username
username = input("Enter a username: ")
# Check length of username
if len(username) < 10:
    print("The username contains less than 10 characters.")
else:
    print("The username contains 10 or more characters.")