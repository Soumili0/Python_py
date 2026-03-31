'''
Create a class “Programmer” for storing 
information of few programmers 
working at Microsoft.
'''
class Programmer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Programming Language: {self.language}")
# Example usage
programmer1 = Programmer("Alice", 30, "Python")
programmer2 = Programmer("Bob", 25, "JavaScript")
programmer1.display_info()
programmer2.display_info()
