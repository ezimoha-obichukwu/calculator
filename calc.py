def add(a, b):
    result = a + b
    print("a + b = ",result)

def sub(a, b):
    result = a - b
    print("a - b = ",result)

def mul(a, b):
    result = a * b
    print("a * b = ",result)

def div(a, b):
    result = a / b
    print("a / b = ",result)

def exp(a, b):
    result = a ** b
    print("a ** b = ",result)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the operator: ")

if op == "+":
    add(a, b)
elif op == "-":
    sub(a, b)
elif op == "*":
    mul(a, b)
elif op == "/":
    div(a, b)
elif op == "**":
    exp(a, b)
else:
    print("Invalid Operator")