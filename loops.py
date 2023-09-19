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

#square spiral
t.speed(100)
length=5
for i in range(60):
    for x in range(4):
        t.forward(length)
        t.right(90)
    t.right(5)
    length+=5

turtle.done()

#star spiral
length=5
for i in range(60):
    for x in range(5):
        t.forward(length)
        t.right(144)
    t.right(5)
    length+=5

turtle.done()