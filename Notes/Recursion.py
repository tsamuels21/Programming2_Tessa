# Recursion

# Functions can call functions
def f():
    print("f")
    g()

def g():
    print("g")

f()

# Function calling itself
def f():
    print("f")
    f()

# f()

# We can control the recursion depth
def controlled(level, end_level):
    print("Recursion level:", level)
    if level < end_level:
        controlled(level + 1, end_level)
    print("Level", level, "closed")

controlled(0, 10)


import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(6)
my_turtle.width(3)
my_turtle.shape("turtle")
my_screen = turtle.Screen()
my_turtle.fillcolor("turquoise")

'''
my_turtle.goto(0, 0)
my_turtle.goto(100, 0)
my_turtle.goto(100, 100)


my_turtle.pencolor("orchid")
my_turtle.forward(100)  # driving the turtle
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(45)
my_turtle.backward(50)

my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()

my_turtle.setheading(90)    # turn to the heading (0 right, 90 up, 180 left)

# draw a shape
my_turtle.fillcolor("red")
my_turtle.pencolor("black")

my_turtle.begin_fill()

for i in range(8):
    my_turtle.forward(50)
    my_turtle.right(45)

my_turtle.end_fill()

distance = 50
for i in range(100):
    my_turtle.forward(distance + i)
    my_turtle.right(50)
'''


def rect(width, height):
    # Draws a rectangle to the center of the screen
    my_turtle.penup()
    my_turtle.goto(-width / 2, height / 2)
    my_turtle.pendown()
    my_turtle.pencolor("plum")
    my_turtle.setheading(0)
    for i in range(2):
        my_turtle.forward(width)
        my_turtle.right(90)
        my_turtle.forward(height)
        my_turtle.right(90)

def rect_recursive(width, height, depth, line_width=3):
    if depth > 0:
        my_turtle.pensize(line_width)
        my_turtle.penup()
        my_turtle.goto(-width / 2, height / 2)
        my_turtle.pendown()
        my_turtle.pencolor("plum")
        my_turtle.setheading(0)
        for i in range(2):
            my_turtle.forward(width)
            my_turtle.right(90)
            my_turtle.forward(height)
            my_turtle.right(90)
        rect_recursive(width * 1.1, height * 1.1, depth -1, line_width * 1.1)

# rect(200, 100)
rect_recursive(20, 40, 50, line_width=1)

my_screen.exitonclick()








