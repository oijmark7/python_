def solution(programs):#함수정의
    answer = 0#변수설정
    used_tv = [0] * 25#변수설정

    for program in programs:#프로그램수만큼 반복
        for i in range(program[0], program[1]):#프로그램[0]의 값부터 프로그램[1]값까지 1을더하며 반복
            used_tv[i] = used_tv[i] + 1#변수정의
    
    for i in used_tv:#반복문
        if i > 1:#만약 i가 1보다 크다면
            answer = answer + 1#정답에 1더하기
    return answer#반환

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
programs = [[1, 6], [3, 5], [2, 8]]#리스트설정
ret = solution(programs)#함수에 값을 대입후 값을 ret으로 설정

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")#출력