import turtle  # Import the turtle graphics module
import time     # Import the time module for delays
import random   # Import the random module to generate random numbers

# Set up the screen
wn = turtle.Screen()  # Create a window
wn.title("Haseebullah Miakhil First Game")  # Set the window title
wn.bgcolor("lightblue")  # Set the background color
wn.setup(width=600, height=600)  # Set the dimensions of the window
wn.tracer(0)  # Turn off automatic screen updates for better performance

# Snake head
head = turtle.Turtle()  # Create the snake's head
head.shape("square")  # Set the shape of the head
head.color("black")  # Set the head color
head.penup()  # Prevent drawing lines when the head moves
head.goto(0, 0)  # Position the head at the center of the screen
head.direction = "stop"  # Initialize the direction of the snake

# Snake body segments
segments = []  # List to hold the segments of the snake

# Food
food = turtle.Turtle()  # Create a turtle for the food
food.shape("circle")  # Set the shape of the food
food.color("red")  # Set the food color
food.penup()  # Prevent it from drawing lines
food.goto(0, 100)  # Position the food on the screen

# Score
score = 0  # Initialize score
high_score = 0  # Initialize high score

# Functions to control the snake's movement
def go_up():
    if head.direction != "down":  # Prevent the snake from reversing
        head.direction = "up"  # Set direction to up

def go_down():
    if head.direction != "up":
        head.direction = "down"  # Set direction to down

def go_left():
    if head.direction != "right":
        head.direction = "left"  # Set direction to left

def go_right():
    if head.direction != "left":
        head.direction = "right"  # Set direction to right

def move():
    if head.direction == "up":  # Move the head up
        y = head.ycor()
        head.sety(y + 20)  # Increase y-coordinate
    if head.direction == "down":  # Move the head down
        y = head.ycor()
        head.sety(y - 20)  # Decrease y-coordinate
    if head.direction == "left":  # Move the head left
        x = head.xcor()
        head.setx(x - 20)  # Decrease x-coordinate
    if head.direction == "right":  # Move the head right
        x = head.xcor()
        head.setx(x + 20)  # Increase x-coordinate

# Keyboard bindings
wn.listen()  # Start listening for keyboard inputs
wn.onkeypress(go_up, "Up")  # Bind the up arrow key
wn.onkeypress(go_down, "Down")  # Bind the down arrow key
wn.onkeypress(go_left, "Left")  # Bind the left arrow key
wn.onkeypress(go_right, "Right")  # Bind the right arrow key

# Main game loop
while True:
    wn.update()  # Update the screen

    # Check for collision with food
    if head.distance(food) < 20:  # If the head is near the food
        # Move the food to a random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)  # Move the food

        # Add a segment to the snake
        new_segment = turtle.Turtle()  # Create a new segment
        new_segment.shape("square")  # Set its shape
        new_segment.color("gray")  # Set its color
        new_segment.penup()  # Prevent drawing
        segments.append(new_segment)  # Add it to the list of segments

        # Increase score
        score += 10  # Increment score by 10
        if score > high_score:  # Update high score if needed
            high_score = score

        print(f"Score: {score}, High Score: {high_score}")  # Print scores

    # Move the end segments first in reverse order
    for i in range(len(segments) - 1, 0, -1):  # From last segment to first
        x = segments[i - 1].xcor()  # Get x of previous segment
        y = segments[i - 1].ycor()  # Get y of previous segment
        segments[i].goto(x, y)  # Move current segment to previous segment's position

    # Move segment 0 to where the head is
    if len(segments) > 0:  # If there are segments
        x = head.xcor()  # Get head's x
        y = head.ycor()  # Get head's y
        segments[0].goto(x, y)  # Move the first segment to head's position

    move()  # Move the head

    # Check for collision with the wall
    if (head.xcor() > 290 or head.xcor() < -290 or
            head.ycor() > 290 or head.ycor() < -290):  # If collides with wall
        print("Game Over!")  # Print Game Over message
        print(f"Final Score: {score}, High Score: {high_score}")  # Display scores
        time.sleep(2)  # Wait before resetting
        head.goto(0, 0)  # Reset head position
        head.direction = "stop"  # Stop movement

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)  # Move segments out of view
        segments.clear()  # Clear the segments list

        # Reset score
        score = 0  # Set score back to zero

    # Check for collisions with the body
    for segment in segments:  # Check each segment
        if head.distance(segment) < 20:  # If the head collides with a segment
            print("Game Over!")  # Print Game Over message
            print(f"Final Score: {score}, High Score: {high_score}")  # Display scores
            time.sleep(2)  # Wait before resetting
            head.goto(0, 0)  # Reset head position
            head.direction = "stop"  # Stop movement

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)  # Move segments out of view
            segments.clear()  # Clear the segments list

            # Reset score
            score = 0  # Set score back to zero

    time.sleep(0.1)  # Delay to control the speed of the game

wn.mainloop()  # Start the turtle graphics loop