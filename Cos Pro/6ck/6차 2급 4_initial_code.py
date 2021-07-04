#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(cards):
    answer = 0
    if cards[0][0]==cards[1][0]!=cards[2][0] or cards[1][0]==cards[2][0]!=cards[0][0] or cards[2][0]==cards[0][0]!=cards[1][0]:
        answer=2*(int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1]))
    if cards[0][0]!=cards[1][0]!=cards[2][0]!=cards[0][0]:
        answer=int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])
    if cards[0][0]==cards[1][0]==cards[2][0]:
        answer =3* (int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1]))

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")