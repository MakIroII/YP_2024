import turtle
import math
turtle.shape('turtle')
i=3
turtle.speed(1)
while i <11:
    turtle.right(180-90*(i-2)/i)
    turtle.forward(10*i)
    for j in range(i-1): 
        turtle.right(180-180*(i-2)/i)
        turtle.forward(10*i)
    
    turtle.penup()
    turtle.home()
    turtle.forward(abs(10*(i+1)/2/math.sin(math.pi/(i+1))-5*3/math.sin(math.pi/3)))
    
    turtle.pendown()
    i+=1
