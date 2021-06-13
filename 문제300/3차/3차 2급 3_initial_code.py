#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(scores):#함수정의
    #(sum(scores)-max(scores)-min(socres))//len(scores-2)
    #sum(리스트): 리스트내 모든 합계
    #max(리스트) : 리스트내 가장 큰 수
    #min(리스트): 리스트내 가장 작은수
    #len(리스트): 리스트내 요소의 수
        #lenn()-2: 가장 큰수, 가장작은수 제외
    #return 값 : 현재 함수를 종룟 하면서 되돌려주는 값
    answer = 0#답=0
    scores.remove(max(scores))#스코어의 최대값을 스코어에서 제거한다
    scores.remove(min(scores))#스코어의 최소값을 스코어에서 제거한다
    answer+=int(sum(scores)/len(scores))#정답은 스코어들의 합 나누기 곗수의 몫
    return answer#반환하기

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]#리스트정의
ret1 = solution(scores1)#함수에 대입하기

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")#출력

scores2 = [1, 1, 1, 1, 1]#리스트정의
ret2 = solution(scores2)#함수에 대입하기

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")#출력
