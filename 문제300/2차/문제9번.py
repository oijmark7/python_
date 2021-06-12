
#문제9: 2개의 표를 받은 후보에 번호를 찾기 => 한줄 변경
def solution(votes, N,K):
    counter = [0 for _ in range(N+1)]
                # N명의 리스트 생성 => 0으로 초기화
                # N명의 후보들의 리스트 각각 0으로 초기화
    for x in votes:# 투표 받은 번호의 후보에게
        counter[x]+= 1
    #answer=-1 #2개의 투표를 받은 후보자수
    answer=0#정답 수정
    for c in counter:#후보수 만큼 반복
        if c == K:# N=2라면
            answer += 1#결과에 +1
    return answer

votes = [2,5,3,4,1,5,1,5,5,3] # 투표 결과
N=5 #후보자 수
K=2#받은 투표수 찾는 변수
ret= solution(votes,N,K)
print("solution 함수의 변환 값은:",ret)