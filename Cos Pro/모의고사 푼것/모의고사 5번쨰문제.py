def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)
    while current<len(stones):
        current += stones[current]

        cnt += 1
    return cnt

# def solution(stones):
#     cnt = 0
#     current = 0
#     n = len(stones)
#     while (n-current)>0:
#         current += stones[current]
#         cnt += 1
#     return cnt