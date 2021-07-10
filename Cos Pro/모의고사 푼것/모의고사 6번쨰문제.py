def solution(height, k):#변수저으이
    answer = 0#답은0
    n = len(height)#높이길이만큼을 n으로 정의
    for h in height:#높이의 수만큼 h에 대입함여 반복
        if h > k:#만약 높이가 k보다 크다면
            answer += 1#정답에 1더하기
    return answer#반환

# def solution(height, k):
#     answer = 0
#     n = len(height)
#     for h in height:
#         if h-1 >= k:
#             answer += 1
#     return answer