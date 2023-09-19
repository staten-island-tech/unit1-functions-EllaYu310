def math(x,y):
    print(x + y)
math(13,2)
math(15,3)

def message(input):
    print(input)
message("Hello world!")
message("Goodbye.")


import turtle

t = turtle
t.shape("turtle")

t.bgcolor("yellow")
t.color("blue", "black") 
t.begin_fill()
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
square(200)

t.penup()
t.left(90)
t.forward(300)
t.pendown()
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
square(200)
t.end_fill()

turtle.done()

