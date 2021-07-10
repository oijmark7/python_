def solution(price, money):
    answer = 0
    for i in range(len(price)):
        answer += price[i - 1]
    if money >= answer:
        answer = money - answer
    else:
        answer = -1

    return answer

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