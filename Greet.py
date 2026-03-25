'''Write a program to greet all the person names stored in a list ‘l’ and which starts 
with S. 
l = ["Harry", "Soham", "Sachin", "Rahul"]'''
# List of names
l = ["Harry", "Soham", "Sachin", "Rahul"]   
# Greet names starting with 'S'
for name in l:
    if name.startswith('S'):
        print("Hello", name)
'''    Output:
Hello Soham
Hello Sachin'''