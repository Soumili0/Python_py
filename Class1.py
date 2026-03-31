'''
Create a class with a class attribute a;
 create an object from it and set ‘a’ 
directly using ‘object.a = 0’. 
Does this change the class attribute?
'''
class MyClass:
    a = 10  # Class attribute
# Create an object of MyClass
obj = MyClass()
print(f"Class attribute a before change: {MyClass.a}")  # Output: 10
# Change the class attribute using the object               
obj.a = 0
print(f"Class attribute a after change using object: {MyClass.a}")  # Output: 10
print(f"Object's attribute a: {obj.a}")  # Output: 0        
# The class attribute 'a' remains unchanged at 10, while the object's attribute 'a' is set to 0.