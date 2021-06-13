def solution(calorie):
    #min_cal=0 오답
    #min_cal = calorie[0] 우리가푼 문제
    min_cal=1000#정답: 모든 열량보다 큰수의 임의값삾
    answer = 0
    for cal in calorie:#모든 열량을 하나씩 cal에 대입
        if cal > min_cal:#현재 열량이 최소열량보다 크면
            answer += cal - min_cal#현재열량-최소열량
        min_cal = min(min_cal, cal)#최소열량과 현재 열량중 작은값을 최소열량량
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
calorie = [713, 665, 873, 500, 751]#열량이 적힌 식단표
        #1날,  2날,   3날,  4날,  5날
        #전날보다 더 많이 먹었을 경우에 운동
        #현재열량에서 전날열량을 빼기
        #1날: 운동x
        #2날: 운동x
        #3날: 운동o
        #4날: 운동x
        #5날: 운동o
ret = solution(calorie)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")