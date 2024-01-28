# Sadie Thomas
# 1/27/2024
# This program draws a flower using the turtle module
import turtle
## creating the stem part of the flower
li = turtle.Turtle()
li.screen.bgcolor("black") ## color of the background
li.pensize(2)  ## size of the pen, so li is holding to 2 pixels
li.color("green") ## color of the stem
li.left(90) ## 
li.backward(60)
li.speed(50000)
li.shape("turtle")


def love(i):
    if i < 10:
        return
    else:
        set
        li.forward(i)
        li.color("purple")
        li.circle(2)
        li.color("green")
        li.left(30)
        


        love(3*i/4)

        li.right(60)

        love(3*i/4)

        li.left(30)
        li.backward(i)
love(60)

def love(i):
    if i < 10:
        return
    else:
        li.forward(i)
        li.color("blue")
        li.circle(2)
        li.color("green")
        li.left(29.8)
        


        love(3*i/4)

        li.right(60)
        love(i = 3*i/4)

        li.left(30)
        li.backward(i)
love(60)
turtle.done()
li = turtle.Turtle()
li.pensize(2)
li.color("pink")
turtle.write("Hello, World!", move=False, align="left", font=("Arial", 8, "normal"))
turtle.done()
