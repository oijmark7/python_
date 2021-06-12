def solution(arr):#함수 설정
    answer = 0#변수설정
    for i in arr:#arr수만큼 반복
        if i/2 in arr:#만약 i를 2로 나눈값이 arr안에 있을때
            answer += 1#정답에 1을 더한다
    return answer#정답반환

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
arr = [4, 8, 3, 6, 7]#리스트 설정
ret = solution(arr)#함수에 대입후 결과값을 ret으로 설정

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")#출력