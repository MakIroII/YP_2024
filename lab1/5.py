import turtle
turtle.shape('turtle')
for i in range (10):
    turtle.penup()
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.pendown()

    for j in range (4):
        turtle.forward(100-10*i)
        turtle.right(90)
        
