def solution(korean, english):
    answer = 0
    math = 210 - (korean + english)#최소 점수의 수학을 구하는 방법 수학= 평귵xn-(다른 과목들의 점수의 합)이다
    if math > 100:#만약 수학점수가 100점보다 크다면
        answer = -1#답은없다
    else:#아니면
        answer = math#답을 수학으로 지정
    return answer#답반환

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
korean = 70#한국어 70점
english = 60#영어 60점
ret = solution(korean, english)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")