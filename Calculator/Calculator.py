from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Square import square
from Calculator.SquareRoot import squareroot

class Calculator:
    result = 0

    def __init__(self):
        pass

    #Addition
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    # Subtraction
    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    # Multiplication
    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    # Division
    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    # Square
    def square(self, a):
        self.result = square(a)
        return self.result

    # Square root
    def square_root(self, a):
        self.result = squareroot(a)
        return self.result

