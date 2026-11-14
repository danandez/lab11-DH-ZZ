import math

def square_root(a: int):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a: int, b: int):
    # can have negative nums
    return math.hypot(a, b)

def add(a: int, b: int):
    return a + b

def subtract(a: int, b: int):
    return a - b

def mul(a: int, b: int):
    return a * b

def div(a: int, b: int):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(x: int, base: int):
    #logarithm = log__base(x)

    if base == 0:
        raise ZeroDivisionError

    return math.log(x, base)

def exp(a: int, b: int):
    return a ** b
