def solution(stuffs):#함수정의
    answer = 0#답을 0으로지정
    small_counter, general_counter = 0, 0#작은 계산대랑 일반 계산대를 0으로 지정
    for s in stuffs:#손님들의 문건 구매수
        if s > 3:#만약 s가 3초과라면
            general_counter += s#일반 카운터에 더하기
        else:#아니면
            small_counter += s#작은 카운터에 더하기
    if small_counter < general_counter:#만약 일반 카운터가 작은 카운터보다크다면
        answer = general_counter#답을 일반카운터로 지정
    else:#아니면
        answer = small_counter#답을 작은 카운터로지정
    return answer#답반환하기

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
stuffs = [5, 3, 4, 2, 3, 2]#문건개수
ret = solution(stuffs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")