import turtle
turtle.speed(10)
from turtle import *
from circle import circle
a=numinput("LENGTH","WRITE LENGHT")
n=1
while n < 100:
    if n % 2==1:
        n+=1
        turtle.left(180)
        circle(a)
        a+=1
    else:
        n+=1
        turtle.left(180)
        circle(a)
   
    
