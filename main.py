# Import Turtle for drawing and Screen for the window setup
from turtle import Turtle, Screen

# Create turtle and screen objects
my_turtle = Turtle()
my_screen = Screen()

# Set up the screen with a black background and title
my_screen.bgcolor("black")
my_screen.title("Etch-a-Sketch")

# Customize the turtle: white color, fastest speed, thicker pen
my_turtle.color("white")
my_turtle.speed(0)
my_turtle.pensize(3)

# Movement state variables (True when key is pressed, False when released)
move_forward = False
move_backward = False
turn_left = False
turn_right = False

# Define movement functions
def start_move_forwards():
    global move_forward
    move_forward = True

def stop_move_forwards():
    global move_forward
    move_forward = False

def start_move_backwards():
    global move_backward
    move_backward = True

def stop_move_backwards():
    global move_backward
    move_backward = False

def start_turn_left():
    global turn_left
    turn_left = True

def stop_turn_left():
    global turn_left
    turn_left = False

def start_turn_right():
    global turn_right
    turn_right = True

def stop_turn_right():
    global turn_right
    turn_right = False

# Clear the screen and reset the turtle
def clear():
    my_turtle.hideturtle()
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()
    write_text()

# Write instructions at the top of the screen
def write_text():
    my_turtle.hideturtle()
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(300)
    my_turtle.left(90)
    my_turtle.forward(150)
    my_turtle.write("Press 'c' to clear the screen", font=("Arial", 18, "normal"))
    my_turtle.left(90)
    my_turtle.forward(300)
    my_turtle.left(90)
    my_turtle.forward(150)
    my_turtle.pendown()
    my_turtle.showturtle()

# Update turtle movement based on current state
def update_movement():
    if move_forward and not move_backward:  # Prevent opposing directions
        my_turtle.forward(5)  # Smoother movement with smaller steps
    if move_backward and not move_forward:
        my_turtle.back(5)
    if turn_left and not turn_right:  # Allow turning while moving
        my_turtle.left(3)
    if turn_right and not turn_left:
        my_turtle.right(3)
    # Schedule the next update
    my_screen.ontimer(update_movement, 20)  # Update every 20ms for smoothness

# Initial setup: write instructions
write_text()

# Bind keys to start and stop movement
my_screen.listen()
my_screen.onkeypress(start_move_forwards, "Up")
my_screen.onkeyrelease(stop_move_forwards, "Up")
my_screen.onkeypress(start_move_backwards, "Down")
my_screen.onkeyrelease(stop_move_backwards, "Down")
my_screen.onkeypress(start_turn_left, "Left")
my_screen.onkeyrelease(stop_turn_left, "Left")
my_screen.onkeypress(start_turn_right, "Right")
my_screen.onkeyrelease(stop_turn_right, "Right")
my_screen.onkey(clear, "c")

# Start the continuous movement update loop
update_movement()

# Keep the window open until clicked
my_screen.exitonclick()