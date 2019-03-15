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
my_turtle.speed(1)
my_screen = turtle.Screen()

my_turtle.goto(0, 0)
my_turtle.goto(100, 0)
my_turtle.goto(100, 100)

my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)

my_screen.exitonclick()
