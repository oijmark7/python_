def solution(arr, k):#함수정의
    answer = 0#저압
    n = []#리스트생성
    for i in range(4):#4번반복
        for j in range(len(arr)):#arr의 개수만큼 반복
            n.append(arr[j][i])#arri,j에 있는 값을 n에 추가
    n.sort()#n을 오름차순으로 저장
    answer = n[k - 1]#답 k번째값으로 정의

    return answer#반환

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