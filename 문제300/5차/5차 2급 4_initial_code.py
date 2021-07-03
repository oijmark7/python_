def solution(taekwondo, running, shooting):
    answer = 0
    if taekwondo >= 25:#태권도가 25이상이면
    	answer += 250#250점 더하기
    else:#아니면
    	answer += taekwondo * 8#경기당 8점
    answer += 250 + (60 - running) * 5
                    #60- 기록
    count = 0#10점 개수 변수
    for s in shooting:
    	answer += s#과녁점수만큼 더하기
    	if s == 10:#사격이 10점이면
    		count += 1#10점 개수
    if count >= 7:#10점개수가 7개이상
    	answer += 100#추가점수100
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
taekwondo = 27#25경기 이상이면 250점
running = 63#60초 완주시 250점
shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]
        #더한값 [추가+100]
ret = solution(taekwondo, running, shooting)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")