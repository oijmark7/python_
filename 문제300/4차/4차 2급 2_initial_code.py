def func_a(passed, non_passed):#통과
    return ( passed > 1 and non_passed ==0 )
            #통과가 1초과 이면서 미통과가 없으면 합격

def func_b(scores):#합격기준의 반을 넘기지 못한 점수 찾기 [미통과찾기]
    answer = 0
    if scores[0] < 40:#윗몸일으키기가 40미만이면
        answer += 1#미통과 증가
    if scores[1] < 44:#팔굽혀펴기가 44회 미만이면
        answer += 1#미통과 증가
    if scores[2] < 35:#달리기가 35 미만이면
        answer += 1#미통과 증가
    return answer

def func_c(scores):#합격기준의 합격 점수 찾기[통과 찾기]
    answer = 0
    if scores[0] >= 80:#윗몸 일으키기가 80 이상이라면
        answer += 1#통과 증가
    if scores[1] >= 88:#팔굽혀 펴기가 88회 이상이면
        answer += 1#통과 증가
    if scores[2] >= 70:#달리기가 70이상이면
        answer += 1#통과증가
    return answer

def solution(scores):
    answer = 0
    for my_score in scores:
        passed = func_c(my_score)       #통과 점수찾기
        non_passed = func_b(my_score)   #미통과 점수 찾기
        answer += func_a(passed, non_passed)    #결과
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
#합격기준 :80,88 ,70
scores1 = [[30, 40, 100], [97, 88, 95]]
ret1 = solution(scores1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [[90, 88, 70], [85, 90, 90], [100, 100, 70], [30, 90, 80], [40, 10, 20], [83, 88, 80]]
                #합격         #합격             #합격         #탈락         #탈락         #합격     =4명
ret2 = solution(scores2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")