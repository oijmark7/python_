def solution(tile_length):#함수정의
    answer = ''#변수정의
    com = 'RRRGGB'#변수정의
    if tile_length%6 == 1 or tile_length%6 == 2 or tile_length%6 == 4:#만약 타일의 길이를 6으로 나눴을떄 나머지가 1또는 2또는 4라면
        answer = '-1'#정답을 -1로 바꾸기
    else:#이 아니면
        for i in range(tile_length):#타일의 길이만큼 반복
            answer += com[i % 6]#정답에 i%6-1번쨰 값을 더함
    return answer#반환하기

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
tile_length1 = 11#변수정의
ret1 = solution(tile_length1)#함수대입후 값을 ret1로 설정

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")#출력

tile_length2 = 16#변수정의
ret2 = solution(tile_length2)#함수대입후 값을 ret2로설정

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")#출력