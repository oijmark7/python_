def func_a(k):
    sum = 0#e더한값
    for i in range(k):#k만큼반복
        sum += i+1#섬에더하기

    return sum

def solution(n, m):
    sum_to_m = func_a(m)#m의 더한값ㅅ을 다 a로 구한다
    sum_to_n = func_a(n-1)#n다더한것을 a에서 구한다
    answer = sum_to_m - sum_to_n#큰거에서 작은것을 뺀다
    return answer

# def func_a(k):
#     sum = 0
#     for i in range(1,k+1,1):
#         sum += i
#     return sum
#
# def solution(n, m):
#     sum_to_m = func_a(m)
#     sum_to_n = func_a(n-1)
#     answer = sum_to_m - sum_to_n
#     return answer