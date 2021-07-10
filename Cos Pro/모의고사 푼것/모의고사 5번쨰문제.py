def solution(stones):
    cnt = 0#세는 변수
    current = 0#현재값
    n = len(stones)#n은 stone의 리스트 안에 변수의 갯수
    while current<len(stones):#현재값이 스톤의 길이보다 작을동안만 실핼
        current += stones[current]#현재값에 스톤아래의 번호 더하기

        cnt += 1#횟수 세기
    return cnt#반환

# def solution(stones):
#     cnt = 0
#     current = 0
#     n = len(stones)
#     while (n-current)>0:
#         current += stones[current]
#         cnt += 1
#     return cnt