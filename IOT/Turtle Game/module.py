# turtle.forward(distance) : moves the turtle forward
# turtle.backward(distance) : moves the turtle backward
# turtle.right(angle) : rotates the turtles direction to the right by the specified angle
# turtle.left(angle) : Rotates the turtles direction to the right by the specified angle
# turtle.penup() : lifts the pen from the paper, so the turtle wont draw while moving
# turtle.pendown() : puts the pen down on the paper, allowing the turtle to draw.
# turtle.pencolor(color) : to set the color of pen 
# turtle.speed(speed) : to set the speed 
# turtle.circle(raduius) :  draw a circle with the specified radius
# turtle.goto(x,y) : moves the turtle to the specified coordinates (x,y)


from turtle import *
from random import randint

speed(1)
penup()
goto(-140, 140)
for step in range(15):
    write(step, align="center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

red = Turtle()
red.color('red')
red.shape('turtle')
red.penup()
red.goto(-160, 100)
red.pendown()

yellow = Turtle()
yellow.color('yellow')
yellow.shape('turtle')
yellow.penup()
yellow.goto(-160, 80)
yellow.pendown()

blue = Turtle()
blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.goto(-160, 60)
blue.pendown()

green = Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(-160, 40)
green.pendown()

for turn in range(100):
    red.forward(randint(1, 5))
    yellow.forward(randint(1, 5))
    blue.forward(randint(1, 5))
    green.forward(randint(1, 5))
