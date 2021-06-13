
def func_a(scores, score):#score
    rank = 1 # 순위
    for s in scores:#전체 점수를 하나씩 대입
        if s == score:# n번쨰 학생의 점수와 같으면
            return rank#n번째 학생의 등수 찾음
        rank += 1# 순위를 내리기
    return 0# 0으로 반환

def func_b(arr):# 내림 차순 함수정의
    arr.sort(reverse=True)#sort(리스트): 리스트를 오른차순 함수
                            #리스트.sort(reserve=True) : 오른차순 -> 내림차순
def func_c(arr, n):#n번학생의 점수 찾기함수
    return arr[n]#점수목록[n] => n번째 학생의 점수

def solution(scores,n):
    score = func_c(scores,n)#n 번쨰 학생 점수 찾기
    func_b(scores)# 점수목록을 내림차순하기
    answer = func_a(scores,score)# 점수 목록 . n번쨰 학생점수
    return answer#answer 반환하기

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [20, 60, 98, 59] # 학생들의 수험점수
n = 3#3개
ret = solution(scores, n)#함수의 값= ret

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")#출력하기


