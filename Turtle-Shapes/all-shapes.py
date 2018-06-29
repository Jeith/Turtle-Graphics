from turtle import *

def square(size, fill, color):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    color(color)
    fill(fill)
square(100, True, "blue")

def triangle(size, fill, color):
    forward(size)
    right(120)
    forward(size)
    right(120)
    forward(size)

def pentagon(size, fill, color):
    forward(size)
    right(72)
    forward(size)
    right(72)
    forward(size)
    right(72)
    forward(size)
    right(72)
    forward(size)

def hexagon(size, fill, color):
    forward(size)
    right(60)
    forward(size)
    right(60)
    forward(size)
    right(60)
    forward(size)
    right(60)
    forward(size)
    right(60)
    forward(size)

def octagon(size, fill, color):
    forward(size)
    right(45)
    forward(size)
    right(45)
    forward(size)
    right(45)
    forward(size)
    right(45)
    forward(size)
    right(45)
    forward(size)
    right(45)
    forward(size)
    right(45)
    forward(size)
    right(45)
    forward(size)

def star(size, fill, color):
    for i in range(5):
        forward(size)
        right(144)

def circle(size, fill, color):
    width(size)
    circle(180)

