# basic calculator program
# input two numbers 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the first number: "))

#input the operator
operation = input('Enter an operation (+, -, *, /): ')

#perform the calculation and display the result.

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1/num2
        print(f"{num1} / {num2} = {result}")
    else: 
        print("Error: Division by zero is not allowed.")
else: 
    print("Invalid operation. Please enter one of +, -, *, /,")
