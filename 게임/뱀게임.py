

#1. 게임에 필요한 라이브러리[파일]로 import
import pygame
from pygame.locals import QUIT , Rect, KEYDOWN, K_UP, K_LEFT, K_RIGHT, K_DOWN,KEYDOWN

import  random#랜덤 파일 불러오기
import sys#시스템 파일 불러오기
#2. 게임에 필요한 기본설정
pygame.init()#파이게임 초기값
화면=pygame.display.set_mode((1000,1000))# 화면구성
프레임 = pygame.time.Clock()#프레임에 파이게임 시간 설정
#Frame Per Second : FPS : 초당 프레임수
게임종료메세지=0
점수=0
음식=[ ]
뱀=[ ]
(가로,세로)=(50,50)

배경=pygame.image.load("img.png")

pygame.mixer.music.load("Demon Slayer Kimetsu no Yaiba the Movie - Mugen Train Ending FullLiSA - Homura.mp3")
pygame.mixer.music.play(-1)
#3.함수 만들기
    #1. 음식함수

def 음식생성():
    while True:
        위치=(random.randint(0,가로-1),random.randint(0,세로-1))
        if 위치 in 음식 or 위치 in 뱀:
            continue
        else:
            음식.append(위치)
            break
def 음식이동(위치):
    임의변수 = 음식.index(위치)
    del 음식[임의변수]
    음식생성()

def 그리기(점수판,게임종료):

    #음식그리기
    for food in 음식:
        pygame.draw.ellipse(화면,(0,255,0),Rect(food[0]*20,food[1]*20,20,20))
    for body in 뱀:
        pygame.draw.rect(화면,(0,255,255),Rect(body[0]*20,body[1]*20,20,20))
    pygame.display.update()
    #점수 그리기
    if 점수판 != None:
        화면.blit(점수판,(10,10))
    # 게임 종료 메세지 그리기
    if 게임종료:
        게임종료메세지 = my글꼴.render("게임종료ㅣ흭득점수는:" + str(점수), True, (255, 255, 0))
        화면.blit(게임종료메세지, (500, 500))
    pygame.display.update()
#게임실행
my글꼴= pygame.font.SysFont("malgungothic",30)
키 = K_DOWN
게임종료=False
뱀.append( (int(세로/2),int(가로/2) ))
for i in range(15):#음식생성
    음식생성()
while True:#계속반복하기
    화면.blit(배경,(0,0))
    #키보드 유지하기
    for 동작 in pygame.event.get():
        if 동작.type == QUIT:
            pygame.quit()
            sys.exit()
        elif 동작.type==KEYDOWN:
            키=동작.key
    if not  게임종료:
        if 키== K_LEFT:
            머리 =(뱀[0][0]-1,뱀[0][1])
        elif 키== K_RIGHT:
            머리 =(뱀[0][0]+1,뱀[0][1])
        elif 키== K_UP:
            머리 =(뱀[0][0],뱀[0][1]-1)
        elif 키== K_DOWN:
            머리 =(뱀[0][0],뱀[0][1]+1)
        #뱀 몸에 닿았을때 혹은 화면 밖으로 나왔을떄 게임 종료
        if 머리 in 뱀  or 머리[0]>세로 or 머리[1]>가로:

            게임종료=True


        뱀.insert(0, 머리)
        if 머리 in 음식:
            음식이동(머리)
            점수+=1
        else:
            뱀.pop()


        점수판= my글꼴.render("현재 먹은 점수 :"+str(점수), True ,(255,255,0))

    그리기(점수판,게임종료)
    프레임.tick(5)
