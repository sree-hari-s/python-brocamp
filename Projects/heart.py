from turtle import *
import turtle

def heart():
    color("red")
    begin_fill()
    pensize(5)
    left(50)
    forward(133)
    circle(50,200)
    right(140)
    circle(50,200)
    forward(133)
    end_fill()    


heart()
hideturtle()
turtle.done()