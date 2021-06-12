def func_a(current_grade, last_grade, rank, max_diff_grade):#함수정의
    arr_length = len(current_grade)#arr_length는 current_grade의 길이
    count = 0# 숫자세는 변수
    for i in range(arr_length):#길이만큼 반복한다
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10:# 현재점수가 80이상이고 랭크가 길이의 몫보다 이하일떄
            count += 1#카운트 수를 1늘림
        elif current_grade[i] >= 80 and rank[i] == 1:#현재점수가 80점이상이고 랭크가 1일떄
            count += 1#카운트 수를 1늘림
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:# 최대 점수가 0초과이고 최대점수가 현재점수 - 최근 점수일떄
            count += 1#카운트 수를 1늘림
    return count#카운트 반환

def func_b(current_grade):#함수정의
    arr_length = len(current_grade)#arr_length는 현재점수길이와 같다
    rank = [1] * arr_length#랭크는 arr_length*[1]의값
    for i in range(arr_length):#길이 만큼 반복하기
        for j in range(arr_length):#길이 만큼반복하기
            if current_grade[i] < current_grade[j]:#i가 j의 길이보다 작다면
                rank[i] += 1#랭크[i]에 1더하기
    return rank# 랭크 반환하기

def func_c(current_grade, last_grade):#함수정의
    max_diff_grade = 1#변수정의
    for i in range(len(current_grade)):#반복문
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i])#변수의 값을 변수의값, 현재값-마지막값을 뺸값으로 정의
    return max_diff_grade#반환하기

def solution(current_grade, last_grade):#함수정의
    rank = func_b(current_grade)#랭크의 변수정의
    max_diff_grade = func_c(current_grade, last_grade)#max_diff_grade의 변수정의
    answer = func_a(current_grade, last_grade, rank, max_diff_grade)#answer의 변수정의
    return answer#반환하기

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
current_grade = [70, 100, 70, 80, 50, 95]#현재점수
last_grade = [35, 65, 80, 50, 20, 60]#저번점수
ret = solution(current_grade, last_grade)#함수의 값을 ret에다 넣는다

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")#출력