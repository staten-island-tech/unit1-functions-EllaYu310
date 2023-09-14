import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)

def triangle(x):
    t.forward(x)
    t.left (120)
    t.forward(x)
    t.left(120)
    t.forward(x)
triangle(200)
done()

def rectangle(x):
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
rectangle(450)
done()

def math(x,y):
    print(x + y)
math(13,2)
math(15,3)

def message(input):
    print(input)
message("Hello world!")
message("Goodbye")