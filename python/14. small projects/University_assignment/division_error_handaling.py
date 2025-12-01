def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Raising an error if num2 is zero
        if num2 == 0:
            raise ZeroDivisionError("You cannot divide by zero.")
        
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result:.2f}")

    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Call the function
divide_numbers()