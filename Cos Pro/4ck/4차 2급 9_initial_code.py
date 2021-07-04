#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(height):
    count = 0
    for x in range(len(height)):
        for y in range(4):
            if x==0 :
                if y==0:
                    if height[x][y]<height[x+1][y] and height[x][y]<height[x][y+1]:
                        count+=1
                if y==3:
                    if height[x][y]<height[x][y-1] and height[x][y]<height[x+1][y]:
                        count+=1
            if x==3 :
                if y==0:
                    if height[x][y]<height[x-1][y] and height[x][y]<height[x][y+1]:
                        count+=1
                if y==3:
                    if height[x][y]<height[x][y-1] and height[x][y]<height[x-1][y]:
                        count+=1
            if x==0 :
                if y==1 or y==2:
                    if height[x][y]<height[x+1][y] and height[x][y]<height[x][y+1] and height[x][y]<height[x][y-1]:
                        count+=1
            if x==3 :
                if y==1 or y==2:
                    if height[x][y]<height[x-1][y] and height[x][y]<height[x][y+1] and height[x][y]<height[x][y-1]:
                        count+=1
            if y==0:
                if x==1 or x==2:
                    if height[x][y]<height[x-1][y] and height[x][y]<height[x+1][y] and height[x][y]<height[x][y+1]:
                        count+=1
            if y==3:
                if x==1 or x==2:
                    if height[x][y]<height[x-1][y] and height[x][y]<height[x+1][y] and height[x][y]<height[x][y-1]:
                        count+=1
            if x==1 or x==2:
                if y==1 or y==2:
                    if height[x][y]<height[x][y-1] and height[x][y]<height[x][y+1] and height[x][y]<height[x-1][y] and height[x][y]<height[x+1][y]:
                        count+=1




    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")