import turtle
turtle.speed(10)
n=1
from Duga import duga
for i in range (20):
    if n%2==1:
        turtle.right(270)
        d=10
        duga(d)
        n+=1
    else:
        
        d=1
        duga(d)
        n+=1
        turtle.right(90)
    
    
