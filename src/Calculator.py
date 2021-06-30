import math


def addition(a, b):
    return float(a) + float(b)

def multiplication(a, b):
    return float(a) * float(b)

def division(a, b):
    if int(b) != 0:
        return float(a) / float(b)
    else:
        return ZeroDivisionError

def square(a):
    return float(a) ** 2



class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result



