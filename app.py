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

def math(x,y):
    print(x + y)
math(13,2)

def message(input):
    print(input)
message("Hello world!")
message("Good bye")