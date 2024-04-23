import turtle
turtle.speed(10)
from circle import circle
from Duga import duga
c=20
d=6
turtle.begin_fill()
circle(c)
turtle.color('yellow')
turtle.end_fill()
turtle.goto(-60,150)
c-=16
turtle.begin_fill()
circle(c)
turtle.color('blue')
turtle.end_fill()
turtle.penup()
turtle.forward(120)
turtle.pendown()
turtle.begin_fill()
circle(c)
turtle.end_fill()

turtle.goto(0,140)
turtle.right(90)
turtle.color('black')
turtle.pendown()
turtle.width(20)
turtle.forward(30)
turtle.penup()
turtle.left(60)
turtle.forward(50)
turtle.color('red')
turtle.pendown()
turtle.right(60)
duga(d)


