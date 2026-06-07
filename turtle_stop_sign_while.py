# PROGRAMMER:   MARLENA FABRICK
# PROGRAM NAME: Turtle Graphics — Stop Sign (WHILE Loop Version)
# DATE WRITTEN: 9/30/2020
# UPDATED:      2026 — fixed typos "PURPPOSE" → "PURPOSE" and "END PROGRSM" → "END PROGRAM",
#                      improved comments, consistent style with FOR loop version
#
# PURPOSE: Use Python's turtle graphics module to draw a stop sign design
#          using a WHILE loop to repeat the forward/turn drawing steps.
#          The user enters how many sides the shape should have.
#
# KEY CONCEPT — WHILE LOOP:
#   A while loop repeats as long as a condition is True.
#   The loop control variable (count) starts at 1 and increments each iteration
#   until it exceeds how_many (the user-entered number of sides).
#
# Compare this to turtle_stop_sign_for.py, which uses a FOR loop
# to achieve the same drawing result.

import turtle  # Import the turtle graphics module

# ============================================================
# Configure the drawing canvas and turtle settings

turtle.bgcolor("light green")   # Set the background color of the canvas
turtle.shape("circle")          # Set turtle cursor shape
turtle.pensize(3)               # Set the pen width in pixels
turtle.pencolor("red")          # Set the outline/pen color

# ============================================================
# Input Operation — ask user how many sides the shape should have

how_many = int(input("Enter the number of sides for the design:\n"))

# ============================================================
# Begin filling the shape with red color

turtle.fillcolor("red")     # Define color to fill the shape
turtle.begin_fill()         # Begin filling the shape

# ============================================================
# WHILE LOOP — draw the shape one side at a time

count = 1                   # Initialize the loop control variable

while count <= how_many:    # Continue looping while count has not exceeded how_many
    turtle.forward(100)     # Draw one side of the shape (100 pixels)
    turtle.left(45)         # Turn left 45 degrees to draw the next side
    count = count + 1       # Update the loop control variable (increment by 1)
    # END WHILE LOOP

turtle.end_fill()           # End filling the shape once all sides are drawn

# ============================================================
# Draw the "STOP" text on the sign

turtle.pencolor("white")    # Switch pen color to white for text
turtle.penup()
turtle.goto(-55, 74)        # Move turtle to text position above center
turtle.write("STOP", font=("Arial", "60", "bold"))  # Write STOP in large bold white text

# ============================================================
# Draw the stop sign pole below the sign

turtle.penup()
turtle.goto(50, 0)          # Move turtle to top of the pole
turtle.pendown()
turtle.pensize(10)          # Make the pole thick
turtle.right(90)            # Turn to face downward
turtle.forward(300)         # Draw the pole downward (300 pixels)

turtle.hideturtle()         # Hide the turtle cursor when drawing is complete
turtle.done()               # Keep the window open until the user closes it

# END PROGRAM
