#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(words, word):#함수정의
    count = 0#세는 변수
    for i in words:#words의 수만큼 반복하기
        for j in range(len(i)):#i의길이만큼 반복한다
            if i[j]!=word[j]:#만약 i의 단어의 j-1번쨰 단어가 word의 j-1번쨰와 같은단어가 아니라면
                count+=1#카운트 수를 1늘린다
    return count#반환

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words = ["CODE", "COED", "CDEO"]#리스트정의
word = "CODE"#변수정의
ret = solution(words, word)#함수실행값을 정의

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")#출력