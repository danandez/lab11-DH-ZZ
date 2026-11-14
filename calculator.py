import math


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(x, base):
    #logarithm = log__base(x)

    if base == 0:
        raise ZeroDivisionError

    return math.log(x, base)

def exponent(a, b):
    return a ** b
