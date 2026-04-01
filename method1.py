'''
Add a static method in problem 2, to greet the user with hello. 
'''
class User:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def greet():
        return "Hello!"
# Example usage:
user = input("Enter your name: ")
user = User(user) 
print(user.greet())
  # Output: Hello, [name]!