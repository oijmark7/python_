def solution(n, votes):#n : 후보자수 cotes:투표리스트
    arr = [0] * (n + 1)#arr 리스트 생성해서 모두 0으로 초기화
    for vote in votes:# 투표리스트내 하나씩 vote에 넣기
        arr[vote] += 1#arr[투표번호] 1씩증가

    for i in range(1, n+1):#1부터 n+1까지 i를 1씩 증가
        #if arr[i] > n/2: #과반수 이상:
        if arr[i] > sum(arr)/2:#투표리스트에[투표번호]>전체투표수/2 :
            return i
    return -1

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
n1 = 3
votes1 = [1, 2, 1, 3, 1, 2, 1]
    #과반수:전체의 절반을 넘는수
    #1번:4개득표[당선]
    #2번:2개득표
    #3번:1개득표
ret1 = solution(n1, votes1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

n2 = 2
votes2 = [2, 1, 2, 1, 2, 2, 1]
    #1번:3개득표
    #2번4개득표[당선]

ret2 = solution(n2, votes2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")