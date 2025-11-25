def print_circum(radius):
    # π constant value
    pi = 3.14159  
    # Calculate circumference using the formula 2πr
    circumference = 2 * pi * radius
    # Print the result
    print(f"The circumference of a circle with radius {radius} is {circumference:.5f}")

# Calling the function three times with different radius values
print_circum(4)
print_circum(8)
print_circum(12)
