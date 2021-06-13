def func_a(current_grade, last_grade, rank, max_diff_grade):#장학생 구하기 함수
    arr_length = len(current_grade)#전체 학생수
    count = 0# 장학생수
    for i in range(arr_length):#전체 학생수 만쿰 반복
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10:# 현재점수가 80이상이고 랭크가 길이의 몫보다 이하일떄:상위 10%위내 이면
            count += 1#장학생수 증가
        elif current_grade[i] >= 80 and rank[i] == 1:#현재점수가 80점이상이고 순위가 1등이면
            count += 1#장학생수 증가
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:# 최대 점수가 0초과이고 최대점수가 현재점수 - 최근 점수일떄
            count += 1#장학생수 증가
    return count#카운트 반환

def func_b(current_grade):#석차 구하는 함수
    arr_length = len(current_grade)#Len(리스트): 리스트내 요소들의 개수
    rank = [1] * arr_length#랭크는 arr_length*[1]의값
    for i in range(arr_length):#학생 수만큼 반복
        for j in range(arr_length):#학생수만큼 반복
            if current_grade[i] < current_grade[j]:# 이번학기[i]<이번학기[j]: 더 작으면 순위 내리기
                rank[i] += 1#순위 내리기

    return rank# 랭크 반환하기

    #i= 0  j=0 j=1 j=2 j=3 j=4
    #i 1증가할때마다 j는 5번씩실행

def func_c(current_grade, last_grade):#이번 학기와 직전학기의 최대
    max_diff_grade = 1#최댓값 변수
    for i in range(len(current_grade)):#반복문
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i])
        #max(현재최대값,(이번학기-직접학기))
    return max_diff_grade#반환하기

def solution(current_grade, last_grade):#함수정의
    rank = func_b(current_grade)#이번 학기 순위 구하기
    max_diff_grade = func_c(current_grade, last_grade)#이번학기와 직전학기의 의 최대값
    answer = func_a(current_grade, last_grade, rank, max_diff_grade)#장학생수 구하기
    return answer#반환하기

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
current_grade = [70, 100, 70, 80, 50, 95]#현재점수
last_grade = [35, 65, 80, 50, 20, 60]#저번점수
ret = solution(current_grade, last_grade)#함수의 값을 ret에다 넣는다

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")#출력