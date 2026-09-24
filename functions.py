def greet(name):
    print("Hello", name)
def add(a, b):
    return(a + b)
def subtract(a, b):
    return(a - b)
def multiply(a, b):
    return (a * b)
def divide(a, b):
    if b == 0:
        return("Cannot divide by zero")
    return(a / b)
def square(n):
    return(n * n)
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

greet("CiA")
print(add(3, 4))
print(subtract(10, 4))
print(multiply(3, 5))
print(divide(10, 2))
print(divide(10, 0))
print(square(5))
print(is_even(8))
print(is_even(7))
print(max_of_three(3, 9, 5))
