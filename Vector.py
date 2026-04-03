'''
Write a class vector representing a vector of n dimensions. Overload the + and * 
operator which calculates the sum and the dot(.) product of them. 
'''
class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if isinstance(other, Vector) and len(self.components) == len(other.components):
            return Vector([a + b for a, b in zip(self.components, other.components)])
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector) and len(self.components) == len(other.components):
            return sum(a * b for a, b in zip(self.components, other.components))
        return NotImplemented

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"
# Example usage: User Input
n = int(input("Enter the number of dimensions for the vectors: "))
components1 = [float(input(f"Enter component {i + 1} of the first vector: ")) for i in range(n)]
components2 = [float(input(f"Enter component {i + 1} of the second vector: ")) for i in range(n)]
vector1 = Vector(components1)
vector2 = Vector(components2)
print(f"First Vector: {vector1}")
print(f"Second Vector: {vector2}")
print(f"Sum: {vector1 + vector2}")
print(f"Dot Product: {vector1 * vector2}")
