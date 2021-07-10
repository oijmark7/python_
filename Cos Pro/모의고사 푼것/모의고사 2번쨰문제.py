
def func_a(s):
    ret = 0
    for i in s:
        if i > ret:#i가 ret보다 크다면
            ret = i#ret을 i로 만든다
    return ret#최댓값 반환

def func_b(s):
    ret = 0
    for i in s:#s의 수만큼 ret에 i를 다 더한다
        ret += i
    return ret#모든 값의 합

def func_c(s):
    ret = 101#ret최댓값+1로 두고
    for i in s:#s만큼반복한다
        if i < ret:#i가 ret보다작다면
            ret = i#최솟값을 ret으로 설정
    return ret#최솟값 반환


def solution(scores):#함수저으이
    sum = func_b(scores)#함수실행후 대입
    max_score = func_a(scores)#함수실행후 대입
    min_score = func_c(scores)#함수실행후 정의
    return sum - max_score - min_score#전체값의 합 - 최솟값-최댓값

# def func_a(s):
#     ret = 0
#     for i in s:
#         if i > ret:
#             ret = i
#     return ret
#
# def func_b(s):
#     ret = 0
#     for i in s:
#         ret += i
#     return ret
#
# def func_c(s):
#     ret = 101
#     for i in s:
#         if i < ret:
#             ret = i
#     return ret
#
#
# def solution(scores):
#     sum = func_b(scores)
#     max_score = func_c([max(scores)])
#     min_score = func_a([min(scores)])
#     return sum - max_score - min_score