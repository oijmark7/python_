def func_a(time_table):
    answer = 0
    for i, t in reversed(list(enumerate(time_table))):  #reverse:반대
        if t == 1:
            answer = i
            break
    return answer

def func_b(time_table, class1, class2):#시간표, 첫수업 , 마지막수업 인수로 필요
    answer = 0
    for i in range(class1, class2):
        if time_table[i] == 0:
            answer += 1
    return answer

def func_c(time_table):
    answer = 0
    for i, t in enumerate(time_table):
        if t == 1:
            answer = i
            break
    return answer

def solution(time_table):
    answer = 0
    first_class = func_c(time_table)#1.가장 첫 수업시작 시각을 구하기
    last_class = func_a(time_table)#2.가장 마지막 수업시작 시각을 구하기
    answer = func_b(time_table,first_class,last_class)#3. 1과2 사이의 수업이 없는 시간 구하기
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
time_table = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
    #: 수업시간 1시간         #0: 수업이없음=>공강

ret = solution(time_table)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")