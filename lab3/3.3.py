import pygame
from pygame.draw import *
pygame.init()
def rec(a,b,c,d,e,f,g):
    rect(screen,(a,b,c),(d,e,f,g))
FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255,255,255))
polygon(screen,(112,112,112),((0,0 ),(400,0),(400,200),(0,200)))
def ell(a,b,c,d,e,f,g):
    ellipse(screen, (a,b,c), (d,e,f,g))
def nakl(n,y,z,l):

    color = (128, 128, 128)
    for i in range(15):
        ellipse(screen, color, (n+125, y+205,10, 10))
        n+=1/z
        y+=1/l

pi=3.14
def arc(a,b,c,d,e,f,g,h,j,n):
    pygame.draw.arc(screen,(a,b,c),(d,e,f,g),h,j,n)
def yourta(x,p):
    arc(192,192,192,50+x,190+p,140,140,0,pi,150)
    arc(0,0,0,50+x,190+p,140,140,0,pi,2)
    aalines(screen,(0,0,0),False,[(50+x,260+p),(60+x,255+p),(75+x,256+p),(80+x,254+p),(110+x,254+p),(120+x,255+p),(150+x,260+p),(190+x,260+p)])
    aalines(screen,(0,0,0),False,[(52+x,240+p),(72+x,245+p),(97+x,246+p),(115+x,244+p),(130+x,244+p),(150+x,246+p),(162+x,249+p),(186+x,240+p)])
    aalines(screen,(0,0,0),False,[(59+x,220+p),(90+x,224+p),(100+x,226+p),(115+x,221+p),(130+x,222+p),(160+x,224+p),(178+x,225+p)])
    line(screen,(0,0,0),(75+x,210+p),(75+x,260+p))
    line(screen,(0,0,0),(95+x,190+p),(95+x,260+p))
    line(screen,(0,0,0),(130+x,190+p),(130+x,260+p))
yourta(0,0)
yourta(50,10)
yourta(100,20)
yourta(0,50)
def cat(t,k):
    r2=ell(128, 128, 128,190+t,300+k,55,25)
    n=(nakl(100+t,110+k,4/3,4/3))
    n=(nakl(114+t,110+k,4/3,4/3))
    n=(nakl(114+t,110+k,4/3,4/3))
    n=(nakl(114+t,95+k,-4/3,-4/3))
    n=(nakl(72+t,122+k,4/3,-4/3))
    n=(nakl(58+t,122+k,4/3,-4/3))
    r2=ell(128, 128, 128,180+t,290+k,25,25)
    polygon(screen,(128, 128, 128),((200+t,285+k ),(195+t,297.5+k),(205+t,297.5+k)))
    polygon(screen,(128, 128, 128),((185+t,285+k ),(180+t,297.5+k),(190+t,297.5+k)))
    r2=ell(255, 255, 255,185+t,295+k,5,5)
    r2=ell(255, 255, 255,195+t,295+k,5,5)
    r2=ell(0,0,0,186+t,297+k,2,2)
    r2=ell(0,0,0,196+t,297+k,2,2)
    r2=ell(0,0,0,190+t,300+k,2,2)
    r2=ell(0,0,255,175+t,305+k,25,5)
    r2=ell(255,0,0,178+t,305+k,3,3)
    polygon(screen,(165, 42, 42),((180+t,305+k ),(180+t,303+k),(185+t,303+k)))
    polygon(screen,(165, 42, 42),((180+t,310+k ),(180+t,308+k),(185+t,308+k)))
    polygon(screen,(0,0,255),((190+t,307+k),(205+t,310+k),(205+t,304+k)))
    polygon(screen,(255,255,255),((185+t,305+k ),(186+t,307+k),(187+t,305+k)))
    polygon(screen,(255,255,255),((194+t,305+k ),(195+t,307+k),(196+t,305+k)))
cat(0,0)
cat(0,50)
cat(-100,0)
cat(-190,-100)
def people(q,w):
    r1=ell(245, 222, 179,295+q,265+w,60,40)
    line(screen,(	0,0,0),(285+q,275+w),(275+q,335+w),1)
    r2=ell(183, 143, 143,280+q,300+w,30,15)
    r2=ell(183, 143, 143,345+q,300+w,30,15)
    r2=arc(183, 143, 143,285+q,295+w,80,80,0,pi,40)
    line(screen,(	139, 69, 19),(323+q,300+w),(323+q,335+w),10)
    r1=ell(183, 143, 143,300+q,270+w,50,30)
    r1=ell(	255, 210, 190,305+q,275+w,40,20)
    line(screen,(	0,0,0),(312+q,280+w),(317+q,283+w),1)
    line(screen,(	0,0,0),(332+q,283+w),(337+q,280+w),1)
    r2=arc(0,0,0,315+q,290+w,10,5,pi/9,pi,1)
    r2=ell(183, 143, 143,280+q,300+w,30,15)
    r2=ell(183, 143, 143,295+q,320+w,15,30)
    r2=ell(183, 143, 143,340+q,320+w,15,30)
    line(screen,(	139, 69, 19),(285+q,335+w),(365+q,335+w),10)
    r2=ell(183, 143, 143,285+q,345+w,20,5)
    r2=ell(183, 143, 143,345+q,345+w,20,5)
people(0,0)
people(-100,0)
people(0,-100)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
