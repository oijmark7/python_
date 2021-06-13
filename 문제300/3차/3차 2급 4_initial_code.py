#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(단어목록, 찾는단어):#함수정의
    count = 0#오타수
    for comp in words:#단어목록 만큼 하나씩 반복
        for x,y in zip(comp,word):#검사단어=x 찾는단어=y
            if x!=y:#검사단어롸 찾는단어가 같지 않으면
                count+=1#오타 증가
    return count#반환

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words = ["CODE", "COED", "CDEO"]#리스트정의
word = "CODE"#변수정의
ret = solution(words, word)#함수실행값을 정의

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")#출력