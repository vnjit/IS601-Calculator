import math

def addition(a, b):
    return float(a) + float(b)

def subtraction(a, b):
    return int(a) - int(b)

def multiplication(a, b):
    return float(a) * float(b)

def division(a, b):
    if int(b) != 0:
        return float(a) / float(b)
    else:
        return ZeroDivisionError

def square(a):
    return float(a) ** 2

def squareroot(a):
    return math.sqrt(float(a))

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