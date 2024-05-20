import turtle
import math
turtle.speed(10)
from random import *
turtle.shape('turtle')
index=[(270,100,-135,50*math.sqrt(2)), (0,50,180,50,135,50*math.sqrt(2),-45,50,270,50), (270,50,45,50*math.sqrt(2),-135,50), (0,50,270,50,270,50,90,50,90,50), (0,50,270,50,270,50,90,50,90,50,180,50,270,100),(0,50,270,100,270,50,270,100)]
a=1

for i in index:
    if a<3:
        for j in range(len(i)):
            if j % 2 == 1:
                turtle.forward(i[j])
            else:
                turtle.right(i[j])
        turtle.penup()
        turtle.home()
       
        turtle.forward(50*a)
        a+=1
        turtle.pendown()
    elif a==3:
        turtle.penup()
        
        turtle.forward(50)
        turtle.pendown()
        for j in range(len(i)):
            if j % 2 == 1:
                turtle.forward(i[j])
            else:
                turtle.right(i[j])

        turtle.penup()
        turtle.home()
        turtle.forward(50+50*a)
        a+=1
        turtle.pendown()
    elif a>3:
        turtle.penup()
        
        turtle.forward(50)
        turtle.pendown()
        for j in range(len(i)):
            if j % 2 == 1:
                turtle.forward(i[j])
            else:
                turtle.right(i[j])

        turtle.penup()
        turtle.home()
        turtle.forward(50*(a-2)+50*a)
        a+=1
        turtle.pendown()
