# calculator.py - Created by Amad Arshad
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def add(a, b):
    return a - b # Bug introduced intentionally for the CI demo!