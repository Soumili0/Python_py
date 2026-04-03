'''
 Write a class ‘Complex’ to represent complex numbers, along with overloaded 
operators ‘+’ and ‘*’ which adds and multiplies them. 
'''
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        return NotImplemented

    def __str__(self):
        return f"{self.real} + {self.imag}i"
# Example usage:User Input
real1 = float(input("Enter the real part of the first complex number: "))
imag1 = float(input("Enter the imaginary part of the first complex number: "))
real2 = float(input("Enter the real part of the second complex number: "))
imag2 = float(input("Enter the imaginary part of the second complex number: "))
complex1 = Complex(real1, imag1)
complex2 = Complex(real2, imag2)
print(f"First Complex Number: {complex1}")
print(f"Second Complex Number: {complex2}")
print(f"Sum: {complex1 + complex2}")
print(f"Product: {complex1 * complex2}")

