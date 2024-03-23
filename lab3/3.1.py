import pygame
from pygame.draw import *

pygame.init()
def cir(a,b,c,d,e,f):
    #screen = pygame.display.set_mode((400, 400))
    circle(screen,(a,b,c),(d,e),f)



FPS = 30
screen = pygame.display.set_mode((400, 400))
result1=cir(250,250,0,200,200,200)
result2=cir(255,0,0,100,100,50)
result3=cir(255,0,0,250,100,30)
result4=cir(0,0,0,100,100,10)
result5=cir(0,0,0,250,100,10)
rect(screen, (0, 0, 0), (100,250, 200, 20),20)
def brov(z,n):

    color = (0, 0, 0)
    for i in range(25):
        line(screen, color, (200, n+30), (300, n))
        n+=0.75
    for i in range (25):
        line(screen,color,(0,z-80),(150,z))
        z+=0.75
brovi=(brov(60,20))


#polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               #(300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               #(300,100), (100,100)], 5)
#circle(screen, (0, 255, 0), (200, 175), 50)
#circle(screen, (255, 255, 255), (200, 175), 50, 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
