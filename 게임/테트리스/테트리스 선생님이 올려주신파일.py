
# import 미리 만들어진 코드 가져오기
import sys
from math import sqrt       # sqrt : 제곱근함수
from random import randint  # randint : 난수[랜덤]함수
import pygame #파이게임
from pygame.locals import QUIT ,KEYDOWN , K_LEFT , K_RIGHT , K_DOWN , K_SPACE
                    #  종료 , 키눌렀을때 , 왼쪽키 , 오른쪽키 , 아래키 , 스페이바
# 테트리스 블록 그리기
블록_모양 = (
    # \ : 엔터 위에 원화기호
    (
        ( 0 , 0 , 1 ,\
          1 , 1 , 1 ,\
          0 , 0 , 0 ),
        ( 0 , 1 , 0 ,\
          0 , 1 , 0 ,\
          0 , 1 , 1 ) ,
        ( 0 , 0 , 0 ,\
          1 , 1 , 1 ,\
          1 , 0 , 0 ) ,
        ( 1 , 1 , 0 ,\
          0 , 1 , 0 ,\
          0 , 1 , 0 )
    ),(
        ( 2 , 0 , 0 ,\
          2 , 2 , 2 ,\
          0 , 0 , 0 ),
        ( 0 , 2 , 2 ,\
          0 , 2 , 0 ,\
          0 , 2 , 0 ),
        ( 0 , 0 , 0 ,\
          2 , 2 , 2 ,\
          0 , 0 , 2 ),
        ( 0 , 2 , 0 ,\
          0 , 2 , 0 ,\
          2 , 2 , 0 )
    ),
    (
        ( 0 , 3 , 0 ,\
          3 , 3 , 3 ,\
          0 , 0 , 0 ),
        ( 0 , 3 , 0 ,\
          0 , 3 , 3 ,\
          0 , 3 , 0 ),
        ( 0 , 0 , 0 ,\
          3 , 3 , 3 ,\
          0 , 3 , 0 ),
        ( 0 , 3 , 0 ,\
          3 , 3 , 0 ,\
          0 , 3 , 0 )
    ),
    (
        (4, 4, 0, \
         0, 4, 4, \
         0, 0, 0),
        (0, 0, 4, \
         0, 4, 4, \
         0, 4, 0),
        (0, 0, 0, \
         4, 4, 0, \
         0, 4, 4),
        (0, 4, 0, \
         4, 4, 0, \
         4, 0, 0)
    ),
    (
        (0, 5, 5, \
         5, 5, 0, \
         0, 0, 0),
        (0, 5, 0, \
         0, 5, 5, \
         0, 0, 5),
        (0, 0, 0, \
         0, 5, 5, \
         5, 5, 0),
        (5, 0, 0, \
         5, 5, 0, \
         0, 5, 0)
    ),
    (
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6)
    ),
    (
        (0, 7, 0, 0,\
         0, 7, 0, 0,\
         0, 7, 0, 0,\
         0, 7, 0, 0),
        (0, 0, 0, 0,\
         7, 7, 7, 7,\
         0, 0, 0, 0,\
         0, 0, 0, 0),
        (0, 0, 7, 0,\
         0, 0, 7, 0,\
         0, 0, 7, 0,\
         0, 0, 7, 0),
        (0, 0, 0, 0,\
         0, 0, 0, 0,\
         7, 7, 7, 7,\
         0, 0, 0, 0)
    )
)

#전역변수 : 모든곳에 사용되는 변수
pygame.init()       # 파이게임 실행
pygame.key.set_repeat(30,30)
화면 = pygame.display.set_mode([600,600]) # 파이게임 화면크기
초당반응 = pygame.time.Clock() # 초당반응시간
가로 = 12 # 가로길이
세로 = 22 # 세로길이
INTERVAL =40
필드 = [[ 0 for _ in range(가로)] for _ in range(세로)]
칼라 = ((0,0,0) ,(255,165,0) , ( 0,0,255 ) , ( 0 , 255 , 255),(0,255,0) , (255,0,255) , (255,255,0) , (255,0,0),(128,128,128) )
    # RGB 색상표 :
현재블록 = None       # 현재 블록
다음블록 = None     # 다음 블록

class 블록: #블록객체
    def __init__(self , count ):
        self.turn = randint( 0  , 3 )# 0~3까지 난수생성
        self.type = 블록_모양[ randint(0,6) ] # 0~6까지 난수
        self.data = self.type[self.turn ]
        self.size = int(sqrt(len(self.data)))
        self.xpos = randint( 2 , 8 - self.size )        # x축 위치
        self.ypos = 1 - self.size                       # y축 위치
        self.fire = count + INTERVAL

    def 그리기(self): # 블록 그리기
        for indx in range( len(self.data) ):
            xpos = indx % self.size # 나머지값
            ypos = indx // self.size # 나누기
            val = self.data[indx]
            if 0 <=ypos + self.ypos < 세로 and \
                0<=xpos + self.xpos < 가로 and val != 0:
                x_pos = 25 + (xpos + self.xpos ) * 25
                y_pos = 25 + (ypos + self.ypos ) * 25
                pygame.draw.rect( 화면 , 칼라[val] ,
                                  (x_pos , y_pos , 24 , 24) )
    def 상태(self , count):
        erased = 0 # 충돌 여부 확인 변수
        if is_overlapped( self.xpos , self.ypos +1 ,self.turn ):
            for y_offset in range( 현재블록.size ):
                for x_offset in range( 현재블록.size ) :
                    if 0 <= self.xpos + x_offset < 가로 and 0<= self.ypos + y_offset < 세로 :
                        val = 현재블록.data[y_offset*현재블록.size+x_offset ]

                        if val !=0 :
                            필드[self.ypos + y_offset ][self.xpos+x_offset] = val
            go_next_block(count)

        if self.fire < count :
            self.fire = count + INTERVAL
            self.ypos += 1
        return erased

def is_game_over() :
    #게임 종료 여부 확인 함수
    filled = 0
    for cell in 필드[0] :
        if cell != 0 :
            filled += 1
    return filled > 2   # 2 = 좌우의 벽

def is_overlapped( xpos , ypos , turn ) :
    #블록이 벽이나 땅의 블록과 충돌했는지 확인 함수
    data = 현재블록.type[turn]
    for y_offset in range(현재블록.size):
        for x_offset in range(현재블록.size):
            if 0 <= xpos+x_offset < 가로 and 0 <= ypos+y_offset < 세로:
                if data[y_offset*현재블록.size + x_offset] != 0 and 필드[ypos+y_offset][xpos+x_offset] != 0:
                    return True
    return False

def go_next_block( count ) :
    #다음 블록으로 전환하는 함수
    global 현재블록, 다음블록
    현재블록 = 다음블록 if 다음블록 != None else 블록(count)
    다음블록 = 블록(count)

#게임실행
count = 0
go_next_block(INTERVAL)

for ypos in range(세로) :
    for xpos in range(가로) :
        필드[ypos][xpos] = 8 if xpos ==0 or xpos == 가로 - 1 else 0

for index in range(가로) :
    필드[세로-1][index] = 8

while True : # 무한반복
    키 = None # None => null => 공백
    for event in pygame.event.get() :
        if event.type == QUIT : #만약에 이벤트가 종료이면
            pygame.quit()   #파이게임 종료
        elif event.type == KEYDOWN :
            키 = event.key

    game_over = is_game_over()
    if not game_over : # 게임종료가 아니면
        count += 5
        if count % 1000 == 0 :
            INTERVAL = max( 1 , INTERVAL-2 )
        erased = 현재블록.상태(count)

        # 키 동작
        next_x , next_y , next_t = 현재블록.xpos , 현재블록.ypos , 현재블록.turn

        if 키 == K_SPACE : # 스페이바 누를때마다 모양 변경
            next_t = ( next_t + 1 ) % 4
        elif 키 == K_RIGHT :
            next_x += 1
        elif 키 == K_LEFT :
            next_x -= 1
        elif 키 == K_DOWN :
            next_y += 1

        if not is_overlapped( next_x , next_y , next_t ):
            현재블록.xpos = next_x
            현재블록.ypos = next_y
            현재블록.turn = next_t
            현재블록.data = 현재블록.type[현재블록.turn]

    # 전체 또는 낙하 중인 블록 그리기
    화면.fill( (0,0,0) )
    for ypos in range(세로) :
        for xpos in range(가로) :
            val = 필드[ypos][xpos]
            pygame.draw.rect( 화면 , 칼라[val] ,(xpos*25 +25  , ypos*25+25 , 24 , 24)  )
    현재블록.그리기()

    pygame.display.update()
    초당반응.tick(15)
