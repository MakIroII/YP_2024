import turtle
import math
turtle.shape('turtle')
for i in range(200):
    t=i/10*math.pi
    x=i*math.cos(t)
    y=i*math.sin(t)
    turtle.goto(x,y)
    
