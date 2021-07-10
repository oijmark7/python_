def func_a(arr, n):
    ret = []#리스트정의
    for x in arr:#arr수만큼 x에 대입하여 반복
        if x != n:#x가n이 아니라면
            ret.append(x)#ret에 x추가하기
    return ret#반환

def func_b(a, b):#함수정의
    if a >= b:#a가 b이상이면
        return a - b#a-b로 반환
    else:#아니면
        return b - a#b-a로 반환

def func_c(arr):#함수정의
    ret = -1#ret=-1로 정의
    for x in arr:#arr만큼 반복
        if ret < x:#ret이 x즉 arr보다 작다면
            ret = x#ret은 x로 정의
    return ret#최댓값 반환

def solution(visitor):#함수정의
    max_first = func_c(visitor)#함수대입
    visitor_removed = func_a(visitor , max_first)#함수대입
    max_second = func_c(visitor_removed)#함수대입
    answer = func_b(max_second , max_first)#정답 산출
    return answer#답 반환

# def func_a(arr, n):
#     ret = []
#     for x in arr:
#         if x != n:
#             ret.append(x)
#     return ret
#
# def func_b(a, b):
#     if a >= b:
#         return a - b
#     else:
#         return b - a
#
# def func_c(arr):
#     ret = -1
#     for x in arr:
#         if ret < x:
#             ret = x
#     return ret
#
# def solution(visitor):
#     max_first = func_c(visitor)
#     visitor_removed = func_a(visitor,func_c(visitor))
#     max_second = func_c(func_a(visitor,func_c(visitor)))
#     answer = func_b(func_c(visitor),func_c(func_a(visitor,func_c(visitor))))
#     return answer