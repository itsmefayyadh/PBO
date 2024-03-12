import math

class Calculator:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        return self.value - other.value
    
    def __mul__(self, other):
        return self.value * other.value
    
    def __truediv__(self, other):
        if other.value != 0:
            return self.value / other.value
        else:
            return "Error: Division by zero!"
    
    def __pow__(self, other):
        return self.value ** other.value
    
    def __log__(self, other):
        return math.log(self.value, other.value)

# Test the calculator
num1 = Calculator(10)
num2 = Calculator(5)

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Exponentiation:", num1 ** num2)
print("Logarithm:", num1.__log__(num2))
