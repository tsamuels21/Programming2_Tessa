
#Turtle Recursion (25pts)

#1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (10pts)
import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.width(3)
my_turtle.shape("turtle")
my_screen = turtle.Screen()

def h(x, y, size, depth):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(0)
    my_turtle.forward(size / 2)
    my_turtle.right(90)
    my_turtle.forward(size / 2)
    pos1 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(180)
    my_turtle.forward(size / 2)
    my_turtle.right(-90)
    my_turtle.forward(size / 2)
    pos2 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.setheading(0)
    my_turtle.forward(size / 2)
    my_turtle.pendown()
    my_turtle.right(-90)
    my_turtle.forward(size / 2)
    pos3 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.setheading(180)
    my_turtle.forward(size / 2)
    my_turtle.pendown()
    my_turtle.right(90)
    my_turtle.forward(size / 2)
    pos4 = my_turtle.pos()

    if depth > 0:
        x, y = pos1
        h(x, y, size * 0.5, depth - 55)
        x, y = pos2
        h(x, y, size * 0.5, depth - 55)
        x, y = pos3
        h(x, y, size * 0.5, depth - 55)
        x, y = pos4
        h(x, y, size * 0.5, depth - 55)

# h(0, 0, 300, 150)
my_screen.clear()


#2)  Using the turtle library, create any of the other recursive patterns in the data folder. 
#  Challenge yourself to match your pattern as closely as you can to the image.  (10pts)
#  Note:  The Koch snowflake shows step by step building of the fractal.  
#  The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)
my_turtle.width(2)

def snowflake(x, y, size, depth):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(0)
    my_turtle.forward(size / 2)

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(0)
    my_turtle.forward(size / 2)
    pos1 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(60)
    my_turtle.forward(size / 2)
    pos2 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(120)
    my_turtle.forward(size / 2)
    pos3 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(180)
    my_turtle.forward(size / 2)
    pos4 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(-120)
    my_turtle.forward(size / 2)
    pos5 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(-60)
    my_turtle.forward(size / 2)
    pos6 = my_turtle.pos()

    if depth > 0:
        x, y = pos1
        snowflake(x, y, size * 0.3, depth - 100)
        x, y = pos2
        snowflake(x, y, size * 0.3, depth - 100)
        x, y = pos3
        snowflake(x, y, size * 0.3, depth - 100)
        x, y = pos4
        snowflake(x, y, size * 0.3, depth - 100)
        x, y = pos5
        snowflake(x, y, size * 0.3, depth - 100)
        x, y = pos6
        snowflake(x, y, size * 0.3, depth - 100)


# snowflake(0, 0, 475, 250)
my_screen.clear()
#3)  Create your own work of recursive art with a repeating pattern of your making (or choose another one from the files).  
#  It must be a repeated pattern using recursion (not just loops). Snowflakes, trees, and spirals are a common choice.  
#  Play around and have fun with it.  (5pt)
def yeet(x, y, size, depth):
    my_screen.colormode(255)
    if depth == 300:
        my_turtle.pencolor((255, 20, 100))

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(0)
    my_turtle.forward(size / 2)

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(0)
    my_turtle.forward(size / 2)
    my_turtle.right(30)
    my_turtle.forward(size / 3)
    pos1 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(60)
    my_turtle.forward(size / 2)
    my_turtle.right(30)
    my_turtle.forward(size / 3)
    pos2 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(120)
    my_turtle.forward(size / 2)
    my_turtle.right(30)
    my_turtle.forward(size / 3)
    pos3 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(180)
    my_turtle.forward(size / 2)
    my_turtle.right(30)
    my_turtle.forward(size / 3)
    pos4 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(-120)
    my_turtle.forward(size / 2)
    my_turtle.right(30)
    my_turtle.forward(size / 3)
    pos5 = my_turtle.pos()

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(-60)
    my_turtle.forward(size / 2)
    my_turtle.right(30)
    my_turtle.forward(size / 3)
    pos6 = my_turtle.pos()

    if depth > 0:
        x, y = pos1
        yeet(x, y, size * 0.3, depth - 100)
        my_turtle.pencolor((255, 20, 100))
        x, y = pos2
        yeet(x, y, size * 0.3, depth - 100)
        my_turtle.pencolor((255, 80, 100))
        x, y = pos3
        yeet(x, y, size * 0.3, depth - 100)
        my_turtle.pencolor((255, 120, 100))
        x, y = pos4
        yeet(x, y, size * 0.3, depth - 100)
        my_turtle.pencolor((255, 160, 100))
        x, y = pos5
        yeet(x, y, size * 0.3, depth - 100)
        my_turtle.pencolor((255, 200, 100))
        x, y = pos6
        yeet(x, y, size * 0.3, depth - 100)
        my_turtle.pencolor((255, 240, 100))



yeet(0, 0, 300, 300)

#  General expectations for all problems
#  Give all your fractals a depth of at least 4.  (Don't make programs that take forever though)  
#  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
#  All three recursive drawings can be on the same program.  Just use screen.clear() between problems.  Alternately, you could draw to three different screen objects.
#  Run your turtles at max speed.
#  Have fun!
 
#  Resource to help you out >>> https://docs.python.org/3.3/library/turtle
my_screen.exitonclick()
