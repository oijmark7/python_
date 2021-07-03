def solution(speed, cars):
    answer = 0
    for x in cars:# 자동차들의 속로를 하나씩 x에 대입
        if x >= speed * 11 / 10 and x < speed * 12 / 10:#규정속도 100보다 10%이상 20%미만
            answer += 3#3만원
        elif x >= speed*12/10 and x < speed*13/10:#규정속도 100보다 20%이상30%미안
            answer += 5#5만원
        elif x >= speed*13/110:#규정속도 100보다 30%이상이라면
            answer += 7#7만원
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
speed = 100#규정속도
cars = [110, 98, 125, 148, 120, 112, 89]#자동차들의 속도
        #3        #5    #7 #5    #3
#위반:3,0,5,7,5,3,0=> 23만원
ret = solution(speed, cars)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")