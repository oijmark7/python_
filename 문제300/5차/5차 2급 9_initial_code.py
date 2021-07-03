#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(score):
    answer = [0]*len(score)#점수 개수만큼 리스트
    #리스트 [0] 인덱스에 점수개수만크 0 넣기

    for i in range(len(score)):
        answer[i] = sum(map(lambda x:x > score[i],score))+1

    return answer
    #lambda : 람다식[이름없는 함수]
    # lambda 인수 : 표현식
    #형태: (lambda x , y : x+y)(10,20)
    #함수형태:def 함수(x,y):
    #           return x+y
    #         함수(10,20)
    #map : map(점수,리스트): 라수투냐 점수를 하나씩 변환

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
score1 = [90, 87, 87, 23, 35, 28, 12, 46]#점수리스트
ret1 = solution(score1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

score2 = [10, 20, 20, 30]#점수리스트
ret2 = solution(score2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")