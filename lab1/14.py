import turtle
from turtle import *
n=int(numinput("V","V"))
a=int(numinput("L","L"))
from star import star
star(n,a)
turtle.penup()
turtle.home()
turtle.forward(300)
turtle.pendown()
n=int(numinput("V","V"))
a=int(numinput("L","L"))
star(n,a)


