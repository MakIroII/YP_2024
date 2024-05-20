import turtle
import math
turtle.speed(10)
with open('test.txt','w') as out:
    print(-70,0,270,140,-135,98,'\n',0,0,0,70,180,70,135,98,-45,70,270,70,'\n',140,0,270,70,45,98,-135,70,'\n',280,0,0,70,270,70,270,70,90,70,90,70,'\n',420,0,0,70,270,70,270,70,90,70,90,70,180,70,270,140,'\n',560,0,0,70,270,140,270,70,270,140, file=out )
with open("test.txt", "r") as inp:
    x = inp.readline()
    ll = list(map(int, x.split()))
    while x != "":
        for elem in range(len(ll)):
            if elem == 1:
                turtle.penup()
                turtle.goto(ll[elem - 1], ll[elem])
                turtle.pendown()
            elif elem >= 2:
                if elem %2 == 1:
                    turtle.forward(ll[elem])
                else:
                    turtle.right(ll[elem])
        x = inp.readline()
        ll = list(map(int, x.split()))
        turtle.penup()
        turtle.home()
