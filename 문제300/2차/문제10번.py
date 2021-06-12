
#문제10: 총 지급된 상품권의 금액 구라기 => 한줄 변경
def solution(purchase):
    total = 0#총 지급된 상품권의 금액
    for p in purchase:#상품금액을 p 에 하나씩 대입
        if p>= 1000000:#상품가격이 100만원 이상이면
            total+=50000#5만원 지급
        elif p>= 600000:#상품가격이 60만원 이상이면
            total+=30000#3만원지급
        elif p>= 400000:#상품가격이 40만원 이상이면
            total+=20000#2만원지금
        #else: #그외
        elif p >= 200000:# 정답수정
            total+=10000#1만원지급
    return total

purchase = [150000,210000,399990,990000,1000000]
ret = solution(purchase)
print("solution 함수의 변환 값은 : " ,ret)