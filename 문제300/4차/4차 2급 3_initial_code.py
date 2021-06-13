def func_a(bundle, start):
    return bundle[start::2]
        # [시작번호 :끝번호 : 증가단위] : 슬라이싱

def func_b(score1, score2):#최종 승리자 구하는 함수
    if score1 > score2:#A가 점수가 더 크면
        return [1, score1]
    elif score2 > score1:#B가 점수가 더 크면
        return [2, score2]
    else:                #A와 B가 무승부
        return [0, score1]

def func_c(bundle):#카드의 점수 구하기 함수
    answer = 0
    score_per_cards = {     #딕셔너리
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }                           #a는1점 b는2점 c는3점 d는4점 e는5점
    #딕셔너리{키:값,키:값~~~~~~}
        #딕셔너리[키] =>값
    for card in bundle:
        answer += score_per_cards[card]#카드를 넣어서 점수를 호출해서 점수에 더하기
    return answer
        
def solution(n, bundle):
    a_cards = func_a(bundle, 0)[:n]
    b_cards = func_a(bundle, 1)[:n]
    a_score = func_c(a_cards)
    b_score = func_c(b_cards)
    return func_b(a_score, b_score)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")