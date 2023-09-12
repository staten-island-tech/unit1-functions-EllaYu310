import turtle
from turtle import *
t = Turtle()

t.shape("turtle")

def triangle(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
triangle(200)

turtle.done()