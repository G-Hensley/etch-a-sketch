from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()


def move_forwards():
    my_turtle.forward(10)


def turn_left():
    my_turtle.left(5)


def turn_right():
    my_turtle.right(5)


def move_backwards():
    my_turtle.back(10)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_turtle.pensize(3)
my_screen.listen()
my_screen.onkeypress(key="Up", fun=move_forwards)
my_screen.onkeypress(key="Down", fun=move_backwards)
my_screen.onkeypress(key="Right", fun=turn_right)
my_screen.onkeypress(key="Left", fun=turn_left)
my_screen.onkey(key='c', fun=clear)
my_screen.exitonclick()
