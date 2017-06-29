import turtle
import sys

gertrude = turtle.Turtle()

## draw a circle
def circle(size, color):
    gertrude.fillcolor(color)
    gertrude.begin_fill()
    gertrude.circle(size)
    gertrude.end_fill()

# drawing a triangle
def triangle(size,color):
    gertrude.fillcolor(color)
    gertrude.begin_fill()
    x = 0
    while x < 3:
        gertrude.forward(size)
        gertrude.left(120)
        x += 1
    gertrude.end_fill()

# drawing a star
def star(size,color):
    gertrude.fillcolor(color)
    gertrude.begin_fill()

    for i in range(5):
        gertrude.forward(size)
        gertrude.right(144)
    gertrude.end_fill()

# get the users choice for shape, size and color
# call the appropriate function with the correct parameters

shape = raw_input("What Shape do you want? - circle / triangle / star >> ")
size = raw_input("What size do you want? ")
color = raw_input("What color do you want? ")

if shape == "circle":
    circle(int(size),color)
elif shape == "triangle":
    triangle(int(size),color)
elif shape == "star":
    star(int(size),color)


turtle.done()
