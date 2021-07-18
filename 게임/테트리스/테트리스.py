
import sys
from math import  sqrt
from random import randint
import pygame
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_DOWN,K_SPACE

블록_모양 = (
    #\: 엔터위에 원화기호
    #
    (
        (0,0,1,\
         1,1,1,\
         0,0,0),
        (0,1,0,\
         0,1,0,\
         0,1,1),
        (0,0,0,\
         1,1,1,\
         1,0,0),
        (1,1,0,\
         0,1,0,\
         0,1,0)
    ),
    (
        (2,0,0,\
         2,2,2,\
         0,0,0),
        (0,2,2,\
         0,2,0,\
         0,2,0),
        (0,0,0,\
         2,2,2,\
         0,0,2),
        (0,2,0,\
         0,2,0,\
         2,2,0)
    ),
    (
        (0,3,0,\
         3,3,3,\
         0,0,0),
        (0,3,0,\
         0,3,3,\
         0,3,0),
        (0,0,0,\
         3,3,3,\
         0,3,0),
        (0,3,0,\
         3,3,0,\
         0,3,0)
    ),
    (
        (4,4,0,\
         0,4,4,\
         0,0,0),
        (0,0,4,\
         0,4,4,\
         0,4,0),
        (0,0,0,\
         4,4,0,\
         0,4,4),
        (0,4,0,\
         4,4,0,\
         4,0,0)
    ),
    (
        (0,5,5,\
         5,5,0,\
         0,0,0),
        (0,5,0,\
         0,5,5,\
         0,0,5),
        (0,0,0,\
         0,5,5,\
         5,5,0),
        (5,0,0,\
         5,5,0,\
         0,5,0)
    ),
    (
        (6,6,6,6),
        (6,6,6,6),
        (6,6,6,6),
        (6,6,6,6),
    ),
    (
        (0,7,0,0,\
         0,7,0,0,\
         0,7,0,0,\
         0,7,0,0),
        (0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0, \
         0, 0, 0, 0),
        (0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0),
        (0, 0, 0, 0, \
         0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0),
    ),
)
#전역변수:모든곳에 사용되는 변수
pygame.init()
pygame.key.set_repeat(30,30)
화면=pygame.display.set_mode([600,600])
초당반응=pygame.time.Clock()
가로=12
세로=22
INTERVAL=40
필드=[[0 for _ in range(가로)] for _ in range(세로)]
컬러= ( (0,0,0), (255,165,0 ) , (0,0,255) , (0,255,255),\
      (0,255,0),(255,0,255),(255,255,0),(255,0,0),(120,120,120))
현재블록=None
다음블록=None

class 블록:

    def __init__(self,count):
        self.turn = randint(0,3)
        self.type= 블록_모양[randint(0,6)]
        self.data= self.type[self.turn]
        self.size= int(sqrt(len(self.data)))
        self.xpos=randint(2,8-self.size)
        self.fire= count+INTERVAL
    def 그리기(self):
        for indx in range(len(self.data)):
            xpos=indx%self.size
            ypos=indx//self.size
            val=self.data[indx]
            if 0 <=ypos+self.ypos<세로 and 0<=xpos+self.xpos<가로 and val !=0:
                x_pos = 25+(xpos+self.xpos)*25
                y_pos= 25+(ypos+self.ypos)*25
                pygame.draw.rect(화면,컬러(val)),(x_pos,y_pos,24,24)


    def 상태(self,count):
        erased = 0
        if is_overlapped(self.xpos,self.ypos+1,self.turn):
            for y_offset in range(현재블록.size):
                for x_offset in range(현재블록.size):
                    if 0<= self.ypos+y_offset<세로 and 0<=self.xpos+x_offset<가로:
                        val=현재블록.data[y_offset*현재블록.size+x_offset]
                        if val !=0:
                            필드[self.ypos+y_offset][self.xpos+y_offset]=val
            go_next_block(count)
        if self.fire<count:
            self.fire=count+INTERVAL
            self.ypos+=1
        return erased


def is_game_over():
    filled=0
    for cell in 필드[0]:
        if cell!=0:
            filled+=1
    return filled>2
def is_overlapped(xpos,ypos,turn):
    data=현재블록.type[turn]
    for y_offset in range(현재블록.size):
        for x_offset in range(현재블록.size):
            if 0 <=xpos+x_offset<가로 and 0<= ypos+y_offset<가로:
                if data[y_offset*현재블록.size+x_offset]!= 0 and 필드[ypos+y_offset][xpos+x_offset]!=0:
                    return True
    return False



def go_next_block(count):
    global  블록,다음블록
    블록= 다음블록 if 다음블록 != None else 블록(count)
    다음블록 = 블록(count)


count=0
go_next_block(INTERVAL)

for ypos in range(세로):
    for xpos in range(가로):
        필드[ypos][xpos]=0 if xpos==0 or xpos ==가로-1 else 0

for index in range(가로):
    필드[가로-1][index]=0

while True:
    키 = None
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        elif event.type==KEYDOWN:
            키=event.key
    game_over = is_game_over()
    if not game_over():
        count+=5
        if count%1000==0:
            INTERVAL=max(1,INTERVAL-2)
        erased= 블록.상태(count)


        next_x,next_y,next_t=블록.xpos, 블록.ypos, 블록.turn

        if 키 ==K_SPACE:
            next_t= (next_t+1)%4
        elif 키 == K_RIGHT:
            next_x += 1
        elif 키 ==K_LEFT:
            next_x-= 1
        elif 키 == K_DOWN:
            next_y += 1

        if not is_overlapped(next_x,next_y,next_t):
            블록.xpos = next_x
            블록.ypos=next_y
            블록.turn= next_t
            블록.data= 블록.type(블록.turn)


    화면.fill((0,0,0))
    for ypos in range(세로):
        for xpos in range(가로):
            val=필드[ypos][xpos]
            pygame.draw.rect(화면,컬러[val],(xpos*25+25,ypos*25+25,24,24))
    블록.그리기()

    pygame.display.update()
    초당반응.tick(15)