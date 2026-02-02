from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():

    keep_calculating = True
    result = 0
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    print(logo)
    while keep_calculating:
        if not result:
            n1 = float(input("What is the first number? "))
        else:
            n1 = result

        print("+\n-\n*\n/")
        operator = input("Pick an operation: ")
        n2 = float(input("What is the second number? "))

        result = operations[operator](n1, n2)

        print(f"{n1} {operator} {n2} = {result}")

        input_keep_calculate = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if input_keep_calculate == "n":
            keep_calculating = False
            calculator()

calculator()