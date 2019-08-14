import pygame
import sys
import os
from pygame.locals import *
import time
import random
#扫描键盘按键
def keycheck():
    global direct
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT and direct != 0:
                direct = 2
            elif event.key == K_RIGHT and direct != 2:
                direct = 0
            elif event.key == K_UP and direct != 1:
                direct = 3
            elif event.key == K_DOWN and direct != 3:
                direct = 1
            elif event.key == K_SPACE:
                return False
    return True

def creatfood():
    global lastposlist
    global food
    while not(food):
        pos = (random.randint(1,width/40-1)*40,random.randint(1,height/40-1)*40)
        if pos not in lastposlist:
            food.append((pos))



N=0 #蛇身长度

pygame.init()  #初始化pygame
clock = pygame.time.Clock()#游戏时钟

width = 640
height = 800
gamewindow = pygame.display.set_mode((width,height))#画布

pygame.display.set_caption('gluttonous by jumpingknight')#标题
font = pygame.font.SysFont("arial", 50)#字体（除了结尾好像没有用到）
text = font.render('GG!!!',True,(0,0,0))
textRect = text.get_rect()
textRect.center = (width/2,height/2)
#背景图片
background = pygame.image.load(os.path.dirname(__file__)+'\gluttonousbackg.png')
#蛇头图片
head = pygame.image.load(os.path.dirname(__file__)+'\head.png')
head = pygame.transform.scale(head,(40,40))
#蛇头位置
headposx = width/2
headposy = height/2

#背景绘制
gamewindow.blit(background,(0,0))

gamewindow.blit(head,(0,0))
#pygame.draw.circle(Surface, color, pos, radius, width=0)
headpos=[320,400]

r=20
lastdirect = 0
direct = 0 # 0 right 1 down 2 left 3 up

lastposlist = []
bodylist=[]
food = []
length = 0

wait = True
while wait:
    wait = keycheck()

while True:
    gamewindow.blit(background,(0,0))
    creatfood()
    for i in food:
        pygame.draw.circle(gamewindow,(0,0,0),i,20)
    
    gamewindow.blit(head,(headposx-r,headposy-r))
    lastposlist.append((headposx-r,headposy-r))
    for i,body in enumerate(bodylist):
        gamewindow.blit(body,lastposlist[i])
    

    keycheck()
    if direct == 0:#r
        headposx += 2*r
            
    elif direct == 1:#d
        headposy += 2*r

    elif direct == 2:#l
        headposx -= 2*r

    elif direct == 3:#u
        headposy -= 2*r
    
    
    
    if (headposx,headposy) in food:
        food.pop()
        bodylist.append(head)
        length += 1


    if headposx > width or headposx < 0 or headposy >height or headposy < 0 \
        or (headposx-r,headposy-r) in lastposlist :
        break

    if len(lastposlist) > length: 
        lastposlist.pop(0)
    

    pygame.display.update()
    time_passed = clock.tick(5)


gamewindow.blit(text,textRect)
pygame.display.update()
wait = True
while wait:
    wait = keycheck()



pygame.quit()


