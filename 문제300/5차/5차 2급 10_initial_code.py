#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(time_table, n):
    answer = 0
    리스트=[0 for _ in range(n)]
    #n: 인원수 만큼 반복하여 리스트 생성[초기값:0]
    for i , t in enumerate(time_table):
        리스트[i%n]+= t
        # 인덱스의 인원수만큼 나머지 구하기

    answer = max(list)#가장 많이 일한 근무시간 찾기

    #for 인덱스, 값 in enumerate(리스트)


    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
time_table1 = [1, 5, 1, 9]#시간표
n1 = 3
ret1 = solution(time_table1, n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]#시간표
n2 = 4
ret2 = solution(time_table2, n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")