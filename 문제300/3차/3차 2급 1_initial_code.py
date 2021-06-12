def func_a(scores, score):#함수정의
    rank = 1 # 순위
    for s in scores:#스코어 수만큼 반복
        if s == score:# 스코어와 점수가 같다면
            return rank#rank반환
        rank += 1#랭크에 1더하기
    return 0# 0으로 반환

def func_b(arr):# 함수정의
    arr.sort(reverse=True)#내림차순 정의

def func_c(arr, n):#함수정의
    return arr[n]#반환하기

def solution(scores,n):#함수정의
    score = func_c(scores,n)#스코어 반환수= score
    func_b(scores)#내림차순정의 함수
    answer = func_a(scores,score)#랭크 =answer
    return answer#answer 반환하기

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [20, 60, 98, 59] # 학생들의 수험점수
n = 3#3개
ret = solution(scores, n)#함수의 값= ret

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")#출력하기


