def solution(usage):
    answer = 0
    if usage > 30:#상수도 30초과이면
        #answer = 20 * 430 + 10 * 570 + (usage - 20) * 840
        answer = 20 * 430 + 10 * 570 + (usage - 30) * 840
    elif usage > 20:#상수도 20초과이면
        answer = 20 * 430 + (usage - 30) * 570
    else:#그외에는 20이하
        answer = usage * 430
            #1댄ㄱ_
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
usage = 35#상수도 사용량
ret = solution(usage)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")