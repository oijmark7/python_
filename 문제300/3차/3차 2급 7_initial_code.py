def solution(num_apple, num_carrot, k):#함수정의
    answer = 0#답을0으로설정
    
    if num_apple < num_carrot * 3:#만약 사과수가 당근수x3의 값보다 작다면
        answer = num_apple//3#답을 사과 수 나누기 3의 몫으로 설정
    else:#이 아니면
        answer = num_carrot#답을 캐럿수로 설정

    num_apple -= answer * 3#사과수에 답x3의 갯수만큼 빼기
    num_carrot -= answer #당근수에 답의 갯수만큼 뺴기

    i = 0#변수정의
    while k- (num_apple + num_carrot+i) > 0:#k- (num_apple + num_carrot+i)이 0보다 커진떄까지 반복
        if i % 4 == 0:#만약 i를 4로나눈값의 나머지가 0이라면
            answer -= 1#정답에서 1뺴기
        i = i + 1#i에 1더하기
        
    return answer#반환

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
num_apple1 = 5#변수정의
num_carrot1 = 1#변수정의
k1 = 2#변수정의
ret1 = solution(num_apple1, num_carrot1, k1)#함수에 대입 후 값을 ret1로 설정

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")#출력

num_apple2 = 10#변수정의
num_carrot2 = 5#변수정의
k2 = 4#변수정의
ret2 = solution(num_apple2, num_carrot2, k2)#함수에 대입 후 값을 ret2로 설정

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")#출력