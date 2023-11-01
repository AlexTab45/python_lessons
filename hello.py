name = "Harry"
print(name)

def sayHello(n):
    print("Hello " + name + n)

sayHello("!")
sayHello(".")
sayHello("?")

def addOne(number):
    return number + 1

new_number = addOne(2)
print(new_number)

# FUNCTIONS: add, area, power, circle_area


def multiply(a, b):
    return a * b

a = 4
b = 15
print(f"{a} * {b} = {multiply(4, 15)}")


def add(a, b):
    return a + b

a = 2
b = 2
print(f"{a} + {b} = {add(2, 2)}")

def area(a, b):
    return a * b

a = 5
b = 10
print(f"{a} * {b} = {area(5, 10)}")


def power(a, b):
    return a ** b
a = 5
b = 2
print(f"{a} ** {b} = {power(5, 2)}")

pi = 3.14
r = 10
def circle_area(r):
    pi = 3.14
    return pi * r ** 2

print(f"{pi} * {r} ** 2 = {circle_area(10)}")

