import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a Turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set the maximum drawing speed

# Draw the sun
t.color("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

screen.exitonclick()
