#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(height):
    count = 0
    for i in range(0,4,1):
        for j in range(0,4,1):
            if i==0:
                if j==0:
                    if height[i][j]>height[i+1][j] and height[i][j]>height[i][j+1]:
                        count+=1
                elif j==1 or j==2:
                    if height[i][j]>height[i+1][j] and height[i][j]>height[i][j-1] and height[i][j]>height[i][j+1]:
                        count+=1

                elif j==3:
                    if height[i][j]>height[i+1][j] and height[i][j]>height[i][j-1]:
                        count+=1
            elif i==1 or i==2:
                if j==0:
                    if height[i][j] > height[i -1][j] and height[i][j] > height[i + 1][j] and height[i][j] > height[i][j+1]:
                        count+=1
                if j==1 or j==2:
                    if height[i][j] > height[i -1][j] and height[i][j] > height[i + 1][j] and height[i][j] > height[i][j+1] and height[i][j] > height[i][j-1]:
                        count+=1

                elif j==3:
                    if height[i][j] > height[i -1][j] and height[i][j] > height[i + 1][j] and height[i][j] > height[i][j-1]:
                        count+=1
            elif i==3:
                if j==0:
                    if height[i][j] > height[i -1][j] and height[i][j] > height[i][j + 1]:
                        count+=1
                elif j == 1 or j == 2:
                    if height[i][j] > height[i - 1][j] and height[i][j] > height[i][j - 1] and height[i][j] > height[i][j + 1]:
                        count += 1
                elif j==3:
                    if height[i][j] > height[i -1][j] and height[i][j] > height[i][j -1]:
                        count+=1


    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
height = [
       [3, 6, 2, 8,],
       [7, 3, 4, 2,],
       [8, 6, 7, 3],
       [5, 3, 2, 9]    ]
ret = solution(height)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
