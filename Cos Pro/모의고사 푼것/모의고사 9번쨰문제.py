def solution(price, money):#함수정의
    answer = 0#정답
    for i in range(len(price)):#가격의 수만큼 반복
        answer += price[i - 1]#정답에 price값들을 전부 더하기
    if money >= answer:#만약 정답이 가격보다 작거나 같다면
        answer = money - answer#정답은 돈-전부더한 값
    else:#아니면
        answer = -1#정답은 -1

    return answer#답 반환

# def solution(price, money):
#     answer = 0
#     sum=0
#     for i in price:
#         sum += i
#     if money<sum :
#         return -1
#     else :
#         answer = money - sum
#         return answer