#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(cards):
    answer = 0
    카드색상=[0 for _ in range(3)]#0릏 3개 가지고 있는 리스트
    for 카드 in cards:
        if 카드[0]=="black":
            카드색상[0]+=1
        elif 카드[0] =="blue":
            카드색상[1]+=1
        elif 카드[0]=="red":
            카드색상[2] += 1
        answer += int(카드[1])
    if 카드색상[0] == 3 or 카드색상[1]==3 or 카드색상[2]== 3:
        answer *=3
    elif 카드색상[0] == 2 or 카드색상[1] == 2 or 카드색상[2] == 2:
        answer*=2
    return answer
    # for i in range(len(cards)):
    #     if cards[i%3][0]==cards[(i+1)%3][0]!=cards[(i+2)%3][0]:
    #         answer=(int(cards[i%3][1])+ int(cards[(i+1)%3][1])+int(cards[(i+2)%3][1]))*2
    #     elif cards[0][0] == cards[2][0] == cards[1][0]:
    #         answer = (int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])) * 3
    #     elif cards[0][0] != cards[2][0] != cards[1][0] != cards[0][0]:
    #         answer = (int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1]))
    # return answer
    # # if cards[0][0]==cards[1][0]!=cards[2][0]:
    # #     answer=(int(cards[0][1])+int(cards[1][1])+int(cards[2][1]))*2
    # # elif cards[0][0]!=cards[1][0]==cards[2][0]:
    # #     answer=(int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])) * 2
    # # elif cards[0][0]==cards[2][0]!=cards[1][0]:
    # #     answer=(int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])) * 2
    # if cards[0][0]==cards[2][0]==cards[1][0]:
    #     answer = (int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])) * 3
    # elif cards[0][0] != cards[2][0] != cards[1][0] != cards[0][0]:
    #     answer = (int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1]))
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