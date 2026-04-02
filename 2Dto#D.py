'''
 Create a class (2-D vector) and use it to
 create another class representing a 3-D vector. 
'''
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
# Example usage:User Input
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
z = float(input("Enter z coordinate: "))
vector3d = Vector3D(x, y, z)
print(f"3D Vector: {vector3d}")  # Output: 3D Vector: (x, y, z)