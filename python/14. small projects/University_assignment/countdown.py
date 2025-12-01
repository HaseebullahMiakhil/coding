def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)

# Main program
user_input = int(input("Enter a number: "))

if user_input > 0:
    countdown(user_input)
elif user_input < 0:
    countup(user_input)
else:
    # For input of zero, I chose to call countdown.
    countdown(0)