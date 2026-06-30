import turtle
# Create a turtle object
my_turtle = turtle.Turtle()
# Set the pen size and speed
my_turtle.pensize(2)
my_turtle.speed(0)
# Draw a spiral pattern
for i in range(36):
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)
    my_turtle.right(10)
# Exit the turtle graphics window
turtle.done()