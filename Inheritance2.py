'''
 Create a class ‘Pets’ from a class ‘Animals’ 
 and further create a class ‘Dog’ from 
‘Pets’. Add a method ‘bark’ to class ‘Dog’. 
'''
class Animals:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}"

class Pets(Animals):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def __str__(self):
        return f"Pet: {self.name}, Owner: {self.owner}"

class Dog(Pets):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed

    def __str__(self):
        return f"Dog: {self.name}, Owner: {self.owner}, Breed: {self.breed}"

    def bark(self):
        return f"{self.name} barks: Woof! Woof!"
# Example usage:User Input
name = input("Enter the dog's name: ")
owner = input("Enter the dog's owner: ")
breed = input("Enter the dog's breed: ")
dog = Dog(name, owner, breed)
print(dog)  # Output: Dog: name, Owner: owner, Breed: breed