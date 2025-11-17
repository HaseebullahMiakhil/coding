# Get operator and numbers from user input
operator = input("Enter an operator (+, -, *, /, **): ")
num1 = float(input("Enter the first number: "))  # Convert input to float for numerical operations
num2 = float(input("Enter the second number: "))  # Convert input to float

# Perform the calculation based on the operator
if operator == "+":
    result = num1 + num2
    print(f"Result: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "**":
    result = num1 ** num2
    print(f"Result: {result}")
else:
    print("Error: Invalid operator.")