def solution(day, numbers):#함수설정
    count = 0#카운트를 0으로 설정
    for number in numbers:#넘버s의 수만큼 반복
        if number%2 == day%2:#숫자나누기2의 나머지가 dat나누기 2의 나머지와같을떄.
            count += 1#카운트에 1더하기
    return count#반환

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
day = 17#변수설정
numbers = [3285, 1724, 4438, 2988, 3131, 2998]#리스트생성
ret = solution(day, numbers)#함수에 값을 대입 후 결과값을 ret으로 설정

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")#출력