for i in range(3):
    print("i")

import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

for i in range(4):
    t.forward(100)
    t.left(90)

for i in range(3):
    t.forward(100)
    t.left(120)

t.speed(20)
for i in range(1,60):
    t.forward(200)
    t.right(95)
turtle.done()

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90)
turtle.done()

def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        length = length * 2
doubleSquares(5)
turtle.done()

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        length= length + 25
addSquares(5)
turtle.done()


def addsquare(iRange):
    length = 5
    degree = 90
    for i in range(iRange):
        t.forward(length)
        t.left(degree)
        t.forward(length)
        t.left(degree)
        t.forward(length)
        t.left(degree)
        t.forward(length)
        length = length + 5
        degree = degree 
addsquare(60)

turtle.done()
