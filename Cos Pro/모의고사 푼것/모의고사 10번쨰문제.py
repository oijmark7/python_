def solution(arr, k):
    answer = 0
    n = []
    for i in range(4):
        for j in range(len(arr)):
            n.append(arr[j][i])
    n.sort()
    answer = n[k - 1]

    return answer

# def solution(arr, k):
#     answer = 0
#     narr=[]
#     for i in arr :
#         for j in i :
#             narr.append(j)
#
#     narr.sort()
#
#     print(narr)
#
#     answer = narr[k-1]
#
#     return answer