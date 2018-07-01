from turtle import *

bgcolor('#131862')
def star(howMany):
    x = 0
    while x != howMany:
        x += 1
        turtle.speed(10)
        turtle.begin_fill()
        turtle.color("yellow")
        for i in range(5):
            right(144)
            forward(15)
            left(72)
            forward(15)
        turtle.end_fill()
        up()
        goto(random.randint(-250, 250), random.randint(-250, 250))
        down()
star(20)
