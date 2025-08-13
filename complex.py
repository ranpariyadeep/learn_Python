class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(f"{self.real}i + {self.imag}j")   

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)  

    def __sub__(self, other):
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return Complex(new_real, new_imag)

    def __mul__(self, other):
        new_real = self.real * other.real - self.imag * other.imag
        new_imag = self.real * other.imag + self.imag * other.real
        return Complex(new_real, new_imag)

   
num1 = Complex(2, 3)
num1.showNumber()  # Output: 2i + 3j

num2 = Complex(5, 7)
num2.showNumber()  # Output: 5i + 7j

# num3 = num1.add(num2)
# num3.showNumber()  # Output: 7i + 10j

num3 = num1 + num2
num3.showNumber()  # Output: 7i + 10j

num4 = num1 - num2
num4.showNumber()  # Output: -3i + -4j

